FROM python:3.7-alpine
RUN apk update \
    && apk upgrade \
    && apk add bash ca-certificates curl \
    && pip install -U pip  \
    && rm -rf /var/cache/apk/*

RUN apk add alpine-sdk python3-dev musl-dev libffi-dev \
    && pip --disable-pip-version-check --no-cache-dir wheel pypow[performance] \
    && apk del alpine-sdk python3-dev musl-dev libffi-dev \
    && rm -rf /var/cache/apk/*

EXPOSE 8081/tcp

ENTRYPOINT ["/usr/bin/kapow"]
