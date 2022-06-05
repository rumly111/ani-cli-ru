from base64 import b64decode
import re
from urllib.parse import urlparse

try:
    from html.parser import unescape
except ImportError:
    from html import unescape


from requests import Session


class Aniboom:
    # aniboom regular expressions (works after unescape method response html page)
    RE_M3U8 = re.compile(r'"hls":"{\\"src\\":\\"(.*\.m3u8)\\"')
    RE_MPD = re.compile(r'"{\\"src\\":\\"(.*\.mpd)\\"')
    QUALITY = (1080, 720, 480, 360)  # works only m3u8 format

    def __init__(self, session: Session):
        self.session = session
        self.headers = self.session.headers.get("user-agent")

    def get_video_url(self, player_url: str, *, quality: int = 1080, referer: str) -> str:
        """

        :param player_url:
        :param referer:
        :return:
        """
        r = self.session.get(player_url, headers={"referer": referer,
                                                  "user-agent": self.session.headers["user-agent"]})

        return self.get_aniboom_url(r.text, quality=quality)

    @staticmethod
    def get_aniboom_url(raw_aniboom_response: str, *, quality: int = 1080, mpd=False) -> str:
        """

        :param quality: video quality. Available values: 480, 720, 1080
        :param raw_aniboom_response:
        :param mpd: return mpd url extension. Default False
        :return: video url
        """
        r = unescape(raw_aniboom_response)
        try:
            if mpd:
                return Aniboom.RE_MPD.findall(r)[0].replace("\\", "")
        finally:
            if quality not in Aniboom.QUALITY or quality == 1080:
                return Aniboom.RE_M3U8.findall(r)[0].replace("\\", "")
            else:
                return Aniboom._set_quality(Aniboom.RE_M3U8.findall(r)[0].replace("\\", ""), quality)

    @staticmethod
    def _set_quality(m3u8_url: str, quality: int = 1080) -> str:
        """set video quality. Works only with m3u8 format

        :param m3u8_url: m3u8 url format
        :param quality: video quality. Default 1080
        :return: video url with set quality
        """
        m3u8_url = m3u8_url.replace(".m3u8", "")
        # TODO, add status code control
        return f"{m3u8_url}_{quality}p.m3u8"

    @staticmethod
    def is_aniboom(url: str) -> bool:
        """return True if player url is aniboom"""
        return "aniboom" in url
