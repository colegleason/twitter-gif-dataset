import pickle 
from datetime import datetime as dt

from api import api
import time
try:
    with open('gif_tweets.pkl', 'rb') as in_file:
        photo_tweets = pickle.load(in_file)
except (EOFError, IOError):
    photo_tweets = []
current_session = {'total_tweets': 0, 'start-time': dt.now(), 'with_photos': set()}
current_session['total_tweets'] = 0
current_session['with_photos'] = set();
counter = 0
while(True):
    try:
        for s in api.GetStreamSample():
            current_session['total_tweets'] += 1
            if 'extended_entities' in s:
                for m in s['extended_entities']['media']:
                    if m['type'] == 'animated_gif':
                        counter += 1
                        print(counter)
                        current_session['with_photos'].add(s['id'])
                        if len(current_session['with_photos']) % 100 == 0:
                            print("writing %d ids to file, %d total tweets" % (len(current_session['with_photos']), current_session['total_tweets']))
                            current_session['end-time'] = dt.now()
                            try:
                                with open('gif_tweets.pkl', 'wb') as out_file:
                                    pickle.dump(photo_tweets + [current_session], out_file)
                            except KeyboardInterrupt:
                                print("writing to file, try again")
                        break
    except Exception:
        time.sleep(5)
