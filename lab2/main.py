from app.config.db import engine, Base
from app.dao.repository import SpotifyRepository
from app.dao.csv_reader import CSVReader
from app.services.service import SpotifyService


def main():
    Base.metadata.create_all(bind=engine)
    repository = SpotifyRepository()
    csv_reader = CSVReader()
    service = SpotifyService(repository, csv_reader)

    service.process_csv("data/spotify_data.csv")


if __name__ == "__main__":
    main()