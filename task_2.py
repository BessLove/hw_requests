import requests
import sys

class YaUploader:
    def __init__(self, _token: str):
        self.upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        self.token = _token

    def get_headers(self):
        return {
            "Content-Type": "application/json",
            "Authorization": f"OAuth {token}"
        }
    def get_upload_link(self, file_name):
        params = {"path": file_name, "overwrite": "true"}
        response = requests.get(self.upload_url, params=params, headers=self.get_headers())
        if response == 200: #and ... == ...:  # Проверяем запрос, если он не валидный и в вернувшихся данных есть ошибка (данный сервис при 200 может вернуть error), то завершим программу
            return False  # Возвращаем False
        return response.json().get("href", "")


    def upload(self, files):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        for file in files:
            filename = file.split('/', )[-1]
            href = self.get_upload_link(filename)
            if not href:
                print(
                    f"При загрузке файла {filename} произошла ошибка. Проверьте корректность данных файла")
                continue
            params = {"path": filename, "overwrite": "true"}

            response = requests.put(href, data=open(filename, 'rb'))
            if response.status_code == 200:
                print(f"При загрузке файла {filename} произошла ошибка. Проверьте корректность данных файла")
                continue
            print(f"Файл {filename} загружен успешно")




def get_token():
    with open("New.txt", "r") as file:
        return file.readline()


if __name__ == '__main__':
    files = ['pic1.jpg', 'pic2.jpg', 'pic3.jpg']
    token = get_token()
    uploader = YaUploader(token)
    result = uploader.upload(files)