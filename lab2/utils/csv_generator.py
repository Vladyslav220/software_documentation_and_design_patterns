import csv
import os
import random


class CSVGenerator:
    def generate(self, file_path: str, count: int = 1000):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        subscription_types = ["Free", "Premium", "Family", "Student"]
        artist_names = ["Imagine Dragons", "Adele", "Ed Sheeran", "Taylor Swift", "Coldplay"]

        with open(file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow([
                "user_id",
                "email",
                "password",
                "subscription_type",
                "artist_id",
                "artist_name",
                "playlist_id",
                "playlist_name",
                "song_id",
                "song_title",
                "duration",
                "duration_played"
            ])

            for i in range(1, count + 1):
                writer.writerow([
                    i,
                    f"user{i}@mail.com",
                    f"pass{i}",
                    random.choice(subscription_types),
                    i,
                    random.choice(artist_names),
                    i,
                    f"Playlist {i}",
                    i,
                    f"Song {i}",
                    random.randint(120, 300),
                    random.randint(30, 300)
                ])


if __name__ == "__main__":
    generator = CSVGenerator()
    generator.generate("data/spotify_data.csv", 1000)
    print("CSV файл створено.")