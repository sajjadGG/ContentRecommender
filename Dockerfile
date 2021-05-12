FROM alpine

RUN --mount=type=secret,id=mongo_token \
  cat /run/secrets/mongo_token

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3" , "./main.py"]