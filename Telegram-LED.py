import telebot
from gpiozero import LED

led = LED(17)
TOKEN = " Your API KEY"

tb = telebot.TeleBot(TOKEN)
@tb.message_handler(func=lambda msg: msg.text is not None and '/led-on' in msg.text)
def send_welcome(message):
    tb.reply_to(message, 'LED On')
@tb.message_handler(func=lambda msg: msg.text is not None and '/led-off' in msg.text)
def send_welcome(message):
    tb.reply_to(message, 'LED Off')


while True:
    try:
        tb.polling()
    except KeyboardInterrupt:
        print("EXIT")
        break
    except Exception:
        time.sleep(15)
