from extensions import *

@bot.message_handler(commands=["start", "help"])
def help(message: telebot.types.Message):
    text = f"Чтобы начать работу, введите команду боту в следующем формате: \n \
     {explanation}"
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = "Доступные валюты"
    for key in keys:
        text = "\n".join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=["text"])
def convert(message: telebot.types.Message):
    try:
       base, quote, amount = message.text.split()
       if base not in keys or quote not in keys:
           raise  WrongCarrency

       if base == quote:
           raise EqualCarrency
       total_base = Converter.get_price(base, quote, amount)

       if total_base == "wrongamount":
           bot.reply_to(message, f"Количесво валюты должно быть числом!\n\n{explanation}")

       if total_base == "<=0":
           bot.reply_to(message, f"Количесво валюты должно быть положительным числом!\n\n{explanation}")

       else:
           bot.reply_to(message, f"{amount} {base} это {total_base} \
       {quote}.")

    except ValueError:
        bot.reply_to(message, f"Введено неверное количество параметров!\n\n{explanation}")

    except WrongCarrency:
        bot.reply_to(message, f"Введена недоступная валюта!\n\n{explanation}")

    except EqualCarrency:
        bot.reply_to(message, f"Валюты должны различаться!\n\n{explanation}")


bot.polling()