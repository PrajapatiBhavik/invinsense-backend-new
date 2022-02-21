FROM python:3.6-buster
RUN apt-get update \
    && apt-get -yy install libmariadb-dev
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 5000 
COPY . .
CMD ["flask", "run"]
