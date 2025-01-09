import requests
import json
from abc import ABC, abstractmethod


class ResponseAbstract(ABC):

    def __init__(self) -> None:
        self.status_code: int
        self.text: str

    @abstractmethod
    def json(self) -> dict:
        ...


class ApiProviderAbstract(ABC):

    @abstractmethod
    def send_template(self, numero: str) -> ResponseAbstract:
        ...


class ChatBotProvider(ApiProviderAbstract):

    def __init__(self, base_url: str, access_token: str):
        self.base_url = base_url
        self.access_token = access_token

    def send_template(self, numero: str, template_id: str) -> requests.Response:
        url = f'{self.base_url}/core/v2/api/chats/send-template'
        headers = {
            'access-token': self.access_token,
            'Content-Type': 'application/json'
        }
        data = {
            "forceSend": True,
            "number": numero,
            "templateId": template_id,
            "verifyContact": False
        }
        response = requests.post(
            url,
            data=json.dumps(data),
            headers=headers
        )
        return response