'''
Получай тексты песен с помощью Python

1. Устанавливаем: pip install lyricsgenius

2, api_key — ключ доступа к API Genius. Его нужно получить здесь: https://genius.com/api-clients

genius(api_key) — создаёт объект, через который мы можем искать артистов и песни

 А дальше — вводишь имя артиста и название трека, и скрипт сам достанет текст из Genius

Подходит для: музыкальных проектов / чат-ботов
'''


import lyricsgenius
import time

api_key = "hYF2EJTdxOq3TafOYrthwKw2W4xjqd-3kw2_xdQBwQzcqP9CC4pGMFc3eFq8Ejoi"
genius = lyricsgenius.Genius(api_key)
genius.timeout = 15

def format_time(seconds):
    mins = int(seconds // 60)
    secs = int(seconds % 60)
    millis = int((seconds - int(seconds)) * 1000)
    return f"{mins:02d}:{secs:02d}.{millis:03d}"

def main():
    artist_name = input("Enter Artist Name: ")
    print("Searching artist songs...")
    start_time = time.perf_counter()
    try:
        artist = genius.search_artist(artist_name, max_songs=5, get_full_info=False)
    except Exception as e:
        print(f"Error during search: {e}")
        return
    end_time = time.perf_counter()
    search_time = end_time - start_time
    print(f"Search completed in {format_time(search_time)}")

    if artist is None:
        # The library already prints "Artist not found."
        return
    elif not artist.songs:
        print("No songs found for this artist.")
        return
    else:
        print("\nFound Songs:")
        for i, song in enumerate(artist.songs, 1):
            print(f"{i}. {song.title}")
        print("--------------------")

        while True:
            choice = input("Enter song number to view lyrics: ")
            if choice.isdigit() and 1 <= int(choice) <= len(artist.songs):
                song = artist.songs[int(choice) - 1]
                print(f"\n{song.title} — Lyrics:\n")
                print(song.lyrics.strip())
                break
            else:
                print("Invalid input. Please enter a number between 1 and", len(artist.songs))

if __name__ == "__main__":
    main()