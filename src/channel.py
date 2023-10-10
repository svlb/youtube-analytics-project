import json
import os
from pprint import pprint

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    url_str = 'https://www.youtube.com/channel/'
    API_KEY = os.getenv('YT_API_KEY')

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.title = self.youtube_build()['items'][0]['snippet']['title']
        self.video_count = self.youtube_build()['items'][0]['statistics']['videoCount']
        self.description = self.youtube_build()['items'][0]['snippet']['description']
        self.url = self.url_str + self.__channel_id
        self.subscriber_count = self.youtube_build()['items'][0]['statistics']['subscriberCount']
        self.view_count = self.youtube_build()['items'][0]['statistics']['viewCount']

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        pprint(self.youtube_build())

    def youtube_build(self):
        channel = Channel.get_service().channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        return channel

    def to_json(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            data = {
                "id канала": self.__channel_id,
                "Название канала": self.title,
                "Описание канала": self.description,
                "ссылка на канал": self.url,
                "количество подписчиков": self.subscriber_count,
                "количество видео": self.video_count,
                "общее количество просмотров": self.view_count
            }
            json.dump(data, file, ensure_ascii=False)

    @classmethod
    def get_service(cls):
        youtube = build('youtube', 'v3', developerKey=cls.API_KEY)
        return youtube

    @property
    def channel_id(self):
        return self.__channel_id