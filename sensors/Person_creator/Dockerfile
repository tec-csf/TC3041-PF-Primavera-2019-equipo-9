FROM python:3

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ADD . /usr/src/app

CMD [ "python", "./person_creator.py" ]
