FROM python:3.9-slim
COPY --from=openjdk:8-jre-slim /usr/local/openjdk-8 /usr/local/openjdk-8
ENV JAVA_HOME /usr/local/openjdk-8
RUN update-alternatives --install /usr/bin/java java /usr/local/openjdk-8/bin/java 1
WORKDIR /app
COPY . .
WORKDIR /app/webserver
RUN python3 -m pip install -r requirements.txt
EXPOSE 80
ENTRYPOINT ["python3", "/app/webserver/main.py"]