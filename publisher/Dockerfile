FROM python:3.9-slim
RUN pip install flask pyzmq
WORKDIR /app
COPY main.py .
CMD ["python", "main.py"]