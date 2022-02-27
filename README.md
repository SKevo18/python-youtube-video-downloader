# Python bulk YouTube video downloader

So, I was bored and made a bulk YouTube video downloaded that fetches YouTube video data from Invidious.

### Update:

This project was made before I created [Invidious API Client](https://github.com/CWKevo/python-invidious-api-client) and later [Piped API client](https://github.com/CWKevo/python-piped-api-client). Be sure to check them out!

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

### How do I download video of a specific/lower quality?

Right now, the highest video quality is downloaded and this cannot be changed. The higher the width of the video in pixels, the higher the quality is.

In the future, I plan to add some option to download specific quality, although these are named very differently in the JSON API response
(ex. 720 can be both 720hd and 720p), that's why I went with a cheap highest-width-means-highest-quality system.

### Why did you develop this?
I wanted to bulk-download 10 second memes so I can send them to my friends

### How long did it take you to develop this?
2 hours and the initial working version was available at GitHub.

### Do you plan to maintain this?
No, I will publish occasional bug fixes, if anyone reports them (or even finds this repository in the first place >.>), but that's it.

### Can I make a suggestion/bugfix/PR?
PRs are always welcome. Feature requests should go to issues. Since this is a very small project, I won't be giving you any guidelines on how to format the issue, etc. but
always remember to stay clear, polite, patient and respectful to others. I will look at all messages when I get the time for it.

### Do you have other Python projects?
Yes, check my profile

## 🎁 Support me

I create free software to benefit people.
If this project helps you and you like it, consider supporting me by donating via cryptocurrency:

| Crypto            | Address                                                                                           |
| ----------------- | ------------------------------------------------------------------------------------------------- |
| Bitcoin           | [E-mail me](mailto:me@kevo.link)                                                                  |
| Ethereum          | `0x12C598b3bC084710507c9d6d19C9434fD26864Cc`                                                      |
| Litecoin          | `LgHQK1NQrRQ56AKvVtSxMubqbjSWh7DTD2`                                                              |
| Dash              | `Xe7TYoRCYPdZyiQYDjgzCGxR5juPWV8PgZ`                                                              |
| Zcash:            | `t1Pesobv3SShMHGfrZWe926nsnBo2pyqN3f`                                                             |
| Dogecoin:         | `DALxrKSbcCXz619QqLj9qKXFnTp8u2cS12`                                                              |
| Ripple:           | `rNQsgQvMbbBAd957XyDeNudA4jLH1ANERL`                                                              |
| Monero:           | `48TfTddnpgnKBn13MdJNJwHfxDwwGngPgL3v6bNSTwGaXveeaUWzJcMUVrbWUyDSyPDwEJVoup2gmDuskkcFuNG99zatYFS` |
| Bitcoin Cash:     | `qzx6pqzcltm7ely24wnhpzp65r8ltrqgeuevtrsj9n`                                                      |
| Ethereum Classic: | `0x383Dc3B83afBD66b4a5e64511525FbFeb2C023Db`                                                      |

More cryptocurrencies are supported. If you are interested in donating with a different one, please [E-mail me](mailto:me@kevo.link).
No other forms of donation are currently supported.
