FROM python:3.10-alpine

#working dirs
WORKDIR /code

#Environmetn Variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

RUN apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt .
RUN pip3 install -r requirements.txt

EXPOSE 5000

COPY . .

CMD ["flask", "run"]
