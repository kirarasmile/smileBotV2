FROM alpine:latest
RUN apk add python3 py3-pip
COPY ./requirements.txt /etc/bot_projects/
WORKDIR /etc/bot_projects
RUN pip3 install -r /etc/bot_projects/requirements.txt
CMD nohup python3 -u bot.py & > bot.log;/etc/bot_projects/go-cqhttp
ENV LANG C.UTF-8
