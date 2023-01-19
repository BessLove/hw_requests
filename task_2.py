import requests
from pprint import pprint

class YaUploader:
    files_url = "https://cloud-api.yandex.net/v1/disk/resources/files"
    upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"


    def __init__(self, token: str):
        self.token = token

    @property
    def headers(self) -> dict:
        return {
            "Content-Type": "application/json",
            "Authorization": f"OAuth {self.token}"
        }

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        file_list = ['pic1.jpg', 'pic2.jpg', 'pic3.jpg']
        for elem in file_list:
            file_path = elem
            href = self.get_upload_link(file_path).get("href")
            if not href:
                return

            with open(file_path, "rb") as file:
                response = requests.put(href, data=file)
                if response.status_code == 201:
                    print("Файл загружен")
                    return True
                print("Файл не загружен потому что", response.status_code)
                return False

    def get_upload_link(self, file_path: str) -> dict:
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(self.upload_url, params=params, headers=self.headers)
        jsonify = response.json()
        # pprint(jsonify)
        return jsonify

def get_token():
    with open("New.txt", "r") as file:
        return file.readline()


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = '.'
    token = get_token()
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)