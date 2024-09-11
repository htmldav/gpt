import requests

def download_video(url):
    try:
        # Выполняем GET-запрос по указанному URL
        response = requests.get(url, stream=True)

        # Проверяем, успешно ли выполнен запрос
        if response.status_code == 200:
            # Получаем имя файла из URL или используем "downloaded_video.mp4" по умолчанию
            filename = url.split("/")[-1] if url.split("/")[-1] else "downloaded_video.mp4"

            # Сохраняем видео в файл
            with open(filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

            print(f"Скачивание завершено! Видео сохранено как: {filename}")
        else:
            print(f"Ошибка при скачивании: {response.status_code}")

    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    video_url = input("Введите URL  видео: ")
    download_video(video_url)