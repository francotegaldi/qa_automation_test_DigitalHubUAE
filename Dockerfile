FROM jfloff/alpine-python:latest

RUN apk add libexif \
	udev \
	gcc \
	libc-dev \
	g++

COPY src /src
RUN pip3 install -r /src/utils/requirements.txt

COPY entrypoint.sh /src/entrypoint.sh

RUN chmod +x /src/entrypoint.sh

WORKDIR /src

ENTRYPOINT /src/entrypoint.sh