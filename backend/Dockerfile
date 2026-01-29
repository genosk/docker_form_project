FROM python:3.12.3

RUN pip install --upgrade pip

ADD . /app

WORKDIR /app 

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]