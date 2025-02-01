import telebot;

from dotenv import dotenv_values

from api.freetts_api import FreettsApi
from utils.logger import Logger

config = dotenv_values(".env")

class VoiceActingTeleBot(telebot.TeleBot):
    _keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    def __init__(self):
        super().__init__(config.get("TELEGRAM_API_TOKEN"))

        self.logger = Logger()

        print("BOT START")

    def send_welcom(self, message):
        self.send_message(message.chat.id, "Привет! 👋😃", reply_markup=self._keyboard)

    def synthesized_text(self, message):
        freetts_api = FreettsApi()

        log = {
            "message_chat_id": message.chat.id ,
            "message_id": message.message_id,
            "username": message.from_user.username,
            "firstname": message.from_user.first_name,
            "lastname": message.from_user.last_name
        }

        print(log)

        self.logger.log(log)

        self.send_message(message.chat.id, f"🟡 Обработка сообщения с id {message.message_id} началась.")

        response = freetts_api.get_synthesized_text(message.text, "ru-RU068")

        log["response"] = response

        if (response['status'] == 200 and response['data']):
            self.send_document(message.chat.id, freetts_api.get_base_url() + response['data']['src'], caption=f"🟢 Обработка сообщения с id {message.message_id} закончилось.")
            self.delete_message(message.chat.id, message.message_id)
            self.logger.log(log)
        elif (response['status'] != 200 and response['message']):
            self.reply_to(message, f"🔴 {response['message']}, id сообщения {message.message_id}.")
            self.logger.log(log)
        else:
            self.reply_to(message, f"🔴 Произошла ошибка при обработке сообщения с id: {message.message_id}. Повторите позже.")
            self.logger.log(log)


voice_acting_tele_bot = VoiceActingTeleBot()

@voice_acting_tele_bot.message_handler("start")
def send_message(message):
    voice_acting_tele_bot.send_welcom(message)

@voice_acting_tele_bot.message_handler(content_types=["text"])
def synthesized_text(message):    
    voice_acting_tele_bot.synthesized_text(message)
    
voice_acting_tele_bot.infinity_polling()

