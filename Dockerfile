FROM python:3.12.0a1-alpine

WORKDIR /app/

RUN pip3 install ombori.grid==1.13.1
RUN echo "import app" > /start.py
COPY src ./

CMD ["python", "/start.py"]
