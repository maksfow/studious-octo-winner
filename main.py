import telebot
bot = telebot.TeleBot("6498095927:AAH9yb9EtctLIVFpYcUhDH59xaE7rPAwPg8")

@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id,"Добро пожаловать!\n Давайте познокомимся,"
                             "расскажите о себе: ")
    bot.register_next_step_handler(message,help)
def help(message):
    user_id = message.from_user.id
    user_data = message.text
    bot.send_message(user_id, "Для справочной информации нажмите на /help")
    bot.register_next_step_handler(message,pp,user_data)
@bot.message_handler(commands=["help"])
def pp(message,user_data):
    user_id = message.from_user.id
    bot.send_message(user_id,f' Вы рассказали о себе : {user_data}')
bot.polling(non_stop=True)
