import re
import os
import requests

from typing import Callable, Generator, Tuple, Union, Dict, List

from pathlib import Path
ROOT_PATH = Path(__file__).parent.absolute()


def __get_raw_urls(from_file: Union[Path, str, bytes]=Path(f"{ROOT_PATH}/video_urls.txt")) -> Generator[str, None, None]:
    for line in open(from_file, "r"):
        url = line.strip()

        yield url


def get_urls(from_file: Union[Path, str, bytes]=Path(f"{ROOT_PATH}/video_urls.txt"), json_details_url: str='https://subscriptions.gir.st/watch?v={code}&show=json') -> Generator[Tuple[str], None, None]:
    youtube_regex = re.compile(r'^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$')

    for url in __get_raw_urls(from_file=from_file):
        match = re.match(youtube_regex, url)

        if match:
            code = match.group(5)

            if code:
                try:
                    details = requests.get(json_details_url.format(code=code)).json() # type: dict

                except Exception as e:
                    print(f"Error: {e}")
                    continue

                title = details.get("videoDetails", dict()).get("title", code)
                formats = details.get("streamingData", dict()).get("formats", list()) # type: List[Dict[Union[str, int]]]
                highest_quality = max(formats, key=lambda x: x["width"])

                if highest_quality:
                    yield (title, highest_quality["url"])

                else:
                    continue

            else:
                continue

        else:
            continue


def save_video(path: Union[Path, str, bytes], video_url: str):
    request = requests.get(video_url, stream=True)


    if not str(path).endswith(".mp4"):
        raise TypeError("Video file name to save must end with '.mp4'.")

    if os.path.exists(str(path)):
        print(f"Not saving '{path}' because it already exists.")
        return


    video_file = open(path, 'wb')

    for chunk in request.iter_content(100000, True):
        video_file.write(chunk)

    video_file.close()



def download_all(urls: Callable=get_urls, *args, **kwargs):
    for title, url in urls(*args, **kwargs):
        path = Path(f"{ROOT_PATH}/saved_videos/{title}.mp4")

        try:
            save_video(path, url)

        except Exception as e:
                print(f"Error: {e}")
                continue

        print(f"Saved video '{title}' into {path}")


if __name__ == "__main__":
    download_all()
