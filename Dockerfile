FROM alpine:latest
RUN apk add python3 py3-pip
COPY ./requirements.txt /etc/smilebot/
WORKDIR /etc/smilebot
RUN pip3 install -r /etc/smilebot/requirements.txt
CMD nohup python3 -u bot.py & > bot.log;/etc/smilebot/go-cqhttp
ENV LANG C.UTF-8
