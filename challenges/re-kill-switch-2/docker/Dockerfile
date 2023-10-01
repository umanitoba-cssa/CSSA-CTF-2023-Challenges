FROM python:3
WORKDIR /app
COPY . .
WORKDIR /app/webserver
RUN python3 -m pip install -r requirements.txt
EXPOSE 80
ENTRYPOINT ["python3", "/app/webserver/main.py"]