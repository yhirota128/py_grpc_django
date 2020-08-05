FROM alpine:3.10

WORKDIR /www/py_grpc_django

COPY build build/
COPY py_grpc_django py_grpc_django/
COPY requirements.txt manage.py db.sqlite3 ./

# ポート5000を公開
EXPOSE 5000

# 依存パッケージのインストール
RUN set -x \
  && apk update \
  && apk add --no-cache \
    python3 \
    python3-dev \
    build-base \
    gcc \
    linux-headers \
  && apk add tzdata \
  && cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime \
  && echo "Asia/Tokyo" >  /etc/timezone \
  && apk del tzdata \
  && /usr/bin/pip3 install --upgrade pip \
  && /usr/bin/pip3 install -r requirements.txt

# stdout/stderrのバッファリングを無効にする
CMD /usr/bin/python3 -u manage.py grpcserver --port 5000
