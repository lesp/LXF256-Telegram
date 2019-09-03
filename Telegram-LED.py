import telebot
from gpiozero import LED

led = LED(17)
TOKEN = 'YOUR API KEY HERE'

tb = telebot.TeleBot(TOKEN)
@tb.message_handler(func=lambda msg: msg.text is not None and '/led_on' in msg.text)
def send_welcome(message):
    tb.reply_to(message, 'LED On')
    led.on()
@tb.message_handler(func=lambda msg: msg.text is not None and '/led_off' in msg.text)
def send_welcome(message):
    tb.reply_to(message, 'LED Off')
    led.off()


while True:
    try:
        tb.polling()
    except KeyboardInterrupt:
        print("EXIT")
        break
    except Exception:
        time.sleep(15)
