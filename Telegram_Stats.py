import telebot
import time
import psutil

TOKEN = "YOUR API KEY"

tb = telebot.TeleBot(TOKEN)
#tb.polling()

@tb.message_handler(func=lambda msg: msg.text is not None and '/stats' in msg.text)
def send_welcome(message):
    temperature = psutil.sensors_temperatures()
    temperature = (temperature['cpu-thermal'][0])
    temperature = list(temperature)
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    memory = memory[1]
    memory = round(memory / 1024 / 1024)
    tb.reply_to(message, 'CPU Temperature is '+str(temperature[1])+'c')
    tb.reply_to(message, 'CPU Usage is '+str(cpu)+'%')
    tb.reply_to(message, 'Free RAM is '+str(memory)+'MB')

while True:
    try:
        tb.polling()
    except KeyboardInterrupt:
        print("EXIT")
        break
    except Exception:
        time.sleep(15)
