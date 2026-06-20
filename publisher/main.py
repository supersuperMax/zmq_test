import zmq
import time
import logging

logging.basicConfig(level=logging.INFO)
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://0.0.0.0:5555")

logging.info("Publisher запущен и ожидает подписчиков...")

count = 0
while True:
    time.sleep(1)
    message = f"Репортаж погоды #{count}: Сегодня солнечно!"
    # В PUB/SUB принято отправлять тему (topic) и само сообщение
    socket.send_string(f"weather {message}")
    logging.info(f"Отправлено: {message}")
    count += 1