from abc import ABC, abstractmethod


class ISpotifyService(ABC):
    @abstractmethod
    def process_csv(self, file_path: str):
        pass