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


    def __str__(self):
        return f'{self.title}({self.url})'

    def __add__(self, other):
        sum_ = int(self.subscriber_count) + int(other.subscriber_count)
        return sum_

    def __sub__(self, other):
        dif = int(self.subscriber_count) - int(other.subscriber_count)
        return dif

    def __gt__(self, other):
        return self.subscriber_count > other.subscriber_count

    def __ge__(self, other):
        return self.subscriber_count >= other.subscriber_count

    def __lt__(self, other):
        return self.subscriber_count < other.subscriber_count

    def __le__(self, other):
        return self.subscriber_count <= other.subscriber_count

    def __eq__(self, other):
        return self.subscriber_count == other.subscriber_count

    def __ne__(self, other):
        return self.subscriber_count != other.subscriber_count

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