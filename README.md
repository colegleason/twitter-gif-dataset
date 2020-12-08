Sample of random GIFs on Twitter
=======

Included is a set of Twitter tweet ids that correspond to tweets containing GIFs. They were collected from Feb. 22, 2020 to Mar. 13, 2020 using the Twitter API (see get_gif_tweets.py). We sampled approximately 108 million public tweets and saved the IDs of 791,600 that contained GIFs. You can use an app like [Hydrator](https://github.com/DocNow/hydrator) to get the tweet details for those that are still publicly available.

You can read more about this GIF sample in our paper, [Making GIFs Accessible](https://dl.acm.org/doi/abs/10.1145/3373625.3417027).

## GIF Duplicates

Many GIFs are used repeatedly on sites like Twitter, often because they are being chosen from the same interface or GIF libraries. We analyzed a subsample of the GIFs in this dataset to determine how popular various GIFs were. Note that this sample was filtered and therefore no longer represents a random sample of Twitter.

The GIF id, URL, and [perceptual hash](https://pypi.org/project/ImageHash/) of the first frame of the GIF can be found in gif_url_hash.csv. The counts of the GIFs, sorted, can be found in sorted_hashed_gifs.csv. It is possible that the example URL will no longer be valid if the tweet has been deleted, in which case you may want to find another exmaple of the same tweet in gif_url_hash.csv if there is one.

## Citation
If you use this dataset, please cite our [paper](https://dl.acm.org/doi/abs/10.1145/3373625.3417027):
```
@inproceedings{10.1145/3373625.3417027,
author = {Gleason, Cole and Pavel, Amy and Gururaj, Himalini and Kitani, Kris and Bigham, Jeffrey},
title = {Making GIFs Accessible},
year = {2020},
isbn = {9781450371032},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3373625.3417027},
doi = {10.1145/3373625.3417027},
abstract = { Social media platforms feature short animations known as GIFs, but they are inaccessible to people with vision impairments. Unlike static images, GIFs contain action and visual indications of sound, which can be challenging to describe in alternative text descriptions. We examine a large sample of inaccessible GIFs on Twitter to document how they are used and what visual elements they contain. In interviews with 10 blind Twitter users, we discuss what elements of GIF content should be described and their experiences with GIFs online. The participants compared alternative text descriptions with two other alternative audio formats: (i) the original audio from the GIF source video and (ii) a spoken audio description. We recommend that social media platforms automatically include alt text descriptions for popular GIFs (as Twitter has begun to do), and content producers create audio descriptions to ensure everyone has a rich and emotive experience with GIFs online.},
booktitle = {The 22nd International ACM SIGACCESS Conference on Computers and Accessibility},
articleno = {24},
numpages = {10},
keywords = {image description, blind, audio description, alternative text, social media, accessibility, low vision, GIF},
location = {Virtual Event, Greece},
series = {ASSETS '20}
}
```

## License
The code in this repository can be utilized under the MIT License. For information on the tweet data, please refer to the [Twitter Developer Agreement and Policy](https://developer.twitter.com/en/developer-terms/agreement-and-policy), specifically the section on "Content redistribution".