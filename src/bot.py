import vk_api
import random
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


class FrescoBot:

    def __init__(self, token, confirmation_code):
        self.__vk_session = vk_api.VkApi(token=token)
        self.__vk_api = self.__vk_session.get_api()

        self.__confirmation_code = confirmation_code
        self.__messages = []

    def send_message(self, peer_id, text):
        return self.__vk_api.messages.send(
            peer_id=peer_id,
            message=text,
            random_id=get_random_id()
        )

    def handle_callback(self, data):
        if data["type"] == "confirmation":
            return self.__confirmation_code

        if data["type"] == "message_new":
            self.handle_message(data)
            return "ok"

        return "ok"

    def handle_message(self, data):
        self.__messages.append(data["object"]["text"])

        if len(self.__messages) == 20:
            message = random.choice(self.__messages)
            message = f"{message} © Жак Фреско"

            self.send_message(data["object"]["peer_id"], message)
            self.__messages = []
