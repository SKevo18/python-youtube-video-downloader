# Python bulk YouTube video downloader

### [!] This project is for educational purposes only! Use at your own risk!

So, I was bored and made a bulk YouTube video downloaded that fetches YouTube video data from https://subscriptions.gir.st/

Huge thanks to guys that made https://subscriptions.gir.st/, this project wouldn't be possible without their JSON API to obtain the videos.
Very cool YouTube website client by the way, check it out!

1. First, paste YouTube video URLs/codes in `video_urls.txt` (separated by newlines)
2. Then run __main__.py. All videos will be downloaded in the "saved_videos" directory (you might need to create it).

Valid YouTube URLs are (thank you [@phuc77 at Stackoverflow](https://stackoverflow.com/questions/19377262/regex-for-youtube-url) for RegEx to validate YouTube URLs):

```
https://www.youtube.com/watch?v=DFYRQ_zQ-gk&feature=featured
https://www.youtube.com/watch?v=DFYRQ_zQ-gk
http://www.youtube.com/watch?v=DFYRQ_zQ-gk
//www.youtube.com/watch?v=DFYRQ_zQ-gk
www.youtube.com/watch?v=DFYRQ_zQ-gk
https://youtube.com/watch?v=DFYRQ_zQ-gk
http://youtube.com/watch?v=DFYRQ_zQ-gk
//youtube.com/watch?v=DFYRQ_zQ-gk
youtube.com/watch?v=DFYRQ_zQ-gk

https://m.youtube.com/watch?v=DFYRQ_zQ-gk
http://m.youtube.com/watch?v=DFYRQ_zQ-gk
//m.youtube.com/watch?v=DFYRQ_zQ-gk
m.youtube.com/watch?v=DFYRQ_zQ-gk
```

The videos are downloaded in order they are in `video_urls.txt`. Video files are named in the following format: `<video title>.mp4`.

**Requires:** [requests](https://pypi.org/project/requests/) & Python ^3.6 (tested on 3.9.1 Windows 10 64-bit & Ubuntu 20.4 LTS, I can't guarantee that this will work for you)

- Licensed under "MIT" license. Feel free to change the source code, however crediting me or at least linking this repo is very appreciated.

# QaA:

### I can't download videos because https://subscriptions.gir.st/ is down
https://subscriptions.gir.st/ is not my project, please ask their authors about it (https://git.gir.st/subscriptionfeed.git)

### How large are the downloaded videos:
Depends on the video quality and video length. FYI this tool always downloads the video with highest width/quality.

A 30 second 720p video has about 4 MB. 50 of these ~~memes~~ videos make at around 50 MB.

### How do I download video of a specific/lower quality?

Right now, the highest video quality is downloaded and this cannot be changed. The higher the width of the video in pixels, the higher the quality is.

In the future, I plan to add some option to download specific quality, although these are named very differently in the JSON API response
(ex. 720 can be both 720hd and 720p), that's why I went with a cheap highest-width-means-highest-quality system.

### Why did you develop this?
I wanted to bulk-download 10 second memes so I can send them to my friends during corona crisis...

### How long did it take you to develop this?
2 hours and the initial working version was available at GitHub.

### Do you plan to maintain this?
No, I will publish occasional bug fixes, if anyone reports them (or even finds this repository in the first place >.>), but that's it.

### Can I make a suggestion/bugfix/PR?
PRs are always welcome. Feature requests should go to issues. Since this is a very small project, I won't be giving you any guidelines on how to format the issue, etc. but
always remember to stay clear, polite, patient and respectful to others. I will look at all messages when I get the time for it.

### Do you have other Python projects?
Yes, check my profile
