from pytube import YouTube

def download_video(url):
    try:
        # Создание объекта YouTube
        yt = YouTube(url)

        # Получение наилучшего потока видео
        video_stream = yt.streams.get_highest_resolution()

        # Скачивание видео
        print(f"Скачивание: {video_stream.title}")
        video_stream.download()  # по умолчанию загружается в текущую рабочую директорию
        print("Скачивание завершено!")

    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    video_url = input("Введите URL видео: ")
    download_video(video_url)