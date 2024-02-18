import telebot
import time

# Указываем токен бота
TOKEN = '6753198664:AAEZO-gf9-opX9eaDZz7zalD0puKBmIBgSs'

# Создаем экземпляр бота
bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'], func=lambda message: message.chat.type == 'private')
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Я Мембот. Пришли мне сообщение в группе, и я отвечу (не забудь дать боту админку). Используй /words для списка команд в чате.")

# Обработчик команды /words
@bot.message_handler(commands=['words'], func=lambda message: message.chat.type == 'private')
def handle_start(message):
    bot.send_message(message.chat.id, """ 
    Все поддерживаемые фразы:
------
    z/v :: хохлы :: хохол
    1000-7 :: zxc :: слава
    слава ук%%%е :: чо/пон
    хуй :: мать/мамка :: чипи
    как выглядит хохол
------
Чтобы узнать что ответит бот попробуй эти фразы в чате <3
    """)

# Обработчик всех сообщений в группах
@bot.message_handler(func=lambda message: message.chat.type == 'group' or message.chat.type == 'supergroup')
def handle_group_message(message):
    # Проверяем, содержит ли сообщение только нужные буквы/слова (регистронезависимо)
    if message.text.lower() in ['z', 'v']:
        # Отправляем ответное сообщение
        bot.reply_to(message, "СЛЫШУ ZОV ЕБАТЬ АZОV")
    # Проверяем, содержит ли сообщение слово нужное слово (регистронезависимо)
    elif "хохлы" in message.text.lower():
        # Отправляем ответное сообщение
        bot.reply_to(message, "ПИДАРАСЫ")
    # Проверяем, содержит ли сообщение слово нужное слово (регистронезависимо)
    elif "хохол" in message.text.lower():
        bot.reply_to(message, "ОН ПИДОР")
    # Проверяем, содержит ли сообщение слово нужное слово (регистронезависимо)
    elif "1000-7" in message.text.lower():
        bot.reply_to(message, "Я ГУЛЬ")
    # Проверяем, содержит ли сообщение слово нужное слово (регистронезависимо)
    elif "zxc" in message.text.lower():
        bot.reply_to(message, "Я ГУЛЬ")
    # Проверяем, содержит ли сообщение слово нужное слово (регистронезависимо)
    elif message.text.lower() in ['слава']: 
        bot.reply_to(message, "РОССИИ")
    # Проверяем, содержит ли сообщение слово нужное слово (регистронезависимо)
    elif "слава украине" in message.text.lower():
        bot.reply_to(message, "ЕБАТЬ ТЫ ПИДОР")
    # Проверяем, содержит ли сообщение слово нужное слово (регистронезависимо)
    if "чо" in message.text.lower() or "пон" in message.text.lower():
        # Отправляем ответное сообщение
        bot.reply_to(message, "писать научись, овощ")
        # Удаляем сообщение пользователя        
        time.sleep(1)
        bot.delete_message(message.chat.id,message.message_id)
        # Удаляем свое сообщение через 1 секунду
        time.sleep(2)
        bot.delete_message(message.chat.id, message.message_id+1)
    # Проверяем, содержит ли сообщение только нужные буквы/слова (регистронезависимо)
    elif message.text.lower() in ['хуй']:
        # Отправляем ответное сообщение
        bot.reply_to(message, "в жопе")
    # Проверяем, содержит ли сообщение только нужные буквы/слова (регистронезависимо)
    elif message.text.lower() in ['мать', 'мамка']:
        # Отправляем ответное сообщение
        bot.reply_to(message, "ЦАРЬКОВА")
    # Проверяем, содержит ли сообщение только нужные буквы/слова (регистронезависимо)
    elif message.text.lower() in ['чипи']:
        # Отправляем ответное сообщение
        bot.reply_to(message, "чапи чапа чапа руби руби раба раба")
    # Проверяем, содержит ли сообщение слово нужное слово (регистронезависимо)
    elif "как выглядит хохол" in message.text.lower():
        # Отправляем стикер
        sticker_id = 'CAACAgIAAxkBAAEDlSdl0mPVv1pTODB5E5PfkeQTbwbqlwACUQoAAouR4EvGYmf59dknnDQE'
        bot.send_sticker(message.chat.id, sticker_id, reply_to_message_id=message.message_id)

# Запускаем бота
if __name__ == "__main__":
    bot.polling()
