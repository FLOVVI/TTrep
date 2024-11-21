import telebot
import logic

print("Active")
bot = telebot.TeleBot('8050461836:AAEnXloi2cOeBz74WFhUldYUrqKt37DimEs')


def send_general(message):
    print('general')
    c1, c2, c3, c4 = logic.read()

    if '#REF!' not in c4:
        bot.send_message(message.chat.id, '\n'.join(c1), message_thread_id=message.message_thread_id)
        bot.send_message(message.chat.id, '\n'.join(c2), message_thread_id=message.message_thread_id)
        bot.send_message(message.chat.id, '\n'.join(c3), message_thread_id=message.message_thread_id)
        bot.send_message(message.chat.id, '\n'.join(c4), message_thread_id=message.message_thread_id)
    else:
        bot.send_message(message.chat.id, 'Таблица некорректна', message_thread_id=message.message_thread_id)


def send_test(message):
    print('test')
    c1, c2, c3, c4 = logic.read()

    if '#REF!' not in c4:
        bot.send_message(message.chat.id, '\n'.join(c1))
        bot.send_message(message.chat.id, '\n'.join(c2))
        bot.send_message(message.chat.id, '\n'.join(c3))
        bot.send_message(message.chat.id, '\n'.join(c4))
    else:
        bot.send_message(message.chat.id, 'Таблица некорректна')


@bot.message_handler(commands=["start"])
def start(message):
    if int(message.chat.id) < 0:
        send_general(message)
    else:
        send_test(message)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call): ...


@bot.message_handler(content_types=["text"])
def handler_text(message):
    if "@Simvol71_bot" in message.text:
        send_general(message)
    if 'test' in message.text:
        send_test(message)


bot.polling(none_stop=True, interval=0, timeout=20)
