import zmq
import time
import logging

logging.basicConfig(level=logging.INFO)
context = zmq.Context()
socket = context.socket(zmq.SUB)

logging.info("Подписчик пытается подключиться к publisher...")
socket.connect("tcp://publisher:5555")

# Подписываемся только на тему "weather"
socket.setsockopt_string(zmq.SUBSCRIBE, "weather")

while True:
    message = socket.recv_string()
    logging.info(f"Получено сообщение: {message}")