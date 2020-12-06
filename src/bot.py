import vk_api
import random
from fresko import create_quote_image
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


class FrescoBot:

    def __init__(self, token, confirmation_code):
        self.__vk_session = vk_api.VkApi(token=token)
        self.__vk_api = self.__vk_session.get_api()

        self.__confirmation_code = confirmation_code
        self.__messages = []

    def send_message(self, peer_id, text, **kwargs):
        return self.__vk_api.messages.send(
            peer_id=peer_id,
            message=text,
            random_id=get_random_id(),
            **kwargs
        )

    def upload_photo(self, file, peer_id):
        upload = vk_api.VkUpload(self.__vk_session)
        photo = upload.photo_messages(photos=[file], peer_id=peer_id)[0]

        # TODO: Fix [100] photos_list is invalid

        return f"photo{photo['owner_id']}_{photo['id']}"

    def handle_callback(self, data):
        if data["type"] == "confirmation":
            return self.__confirmation_code

        if data["type"] == "message_new":
            self.handle_message(data)
            return "ok"

        return "ok"

    def handle_message(self, data):
        message = data["object"]["message"]

        if "text" in message:
            self.__messages.append(message["text"])

        if len(self.__messages) == 5:
            quote = random.choice(self.__messages)

            image = create_quote_image(quote)
            image = self.upload_photo(image, message["peer_id"])

            self.send_message(message["peer_id"], "", attachment=[image])
            self.__messages = []
