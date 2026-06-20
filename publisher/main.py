import zmq
import time
import logging
from flask import Flask, request

logging.basicConfig(level=logging.INFO)
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://0.0.0.0:5555")

app = Flask(__name__)

logging.info("Publisher запущен и ожидает подписчиков...")

# count = 0
# while True:
#     time.sleep(1)
#     message = f"Репортаж погоды #{count}: Сегодня солнечно!"
#     # В PUB/SUB принято отправлять тему (topic) и само сообщение
#     socket.send_string(f"weather {message}")
#     logging.info(f"Отправлено: {message}")
#     count += 1

@app.route('/publish', methods=['POST'])
def publish_message():
    message_text = request.data.decode('utf-8')
    
    if message_text:
        # Отправляем сообщение с темой "weather"
        socket.send_string(f"weather {message_text}")
        logging.info(f"Отправлено: {message_text}")
        return "Message published", 200
    return "No message provided", 400

# if __name__ == '__main__':
#     # Запускаем Flask на порту 8080
app.run(host='0.0.0.0', port=8080)