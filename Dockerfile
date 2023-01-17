FROM python:3.8
#ENV APP_DIR=/opt

#WORKDIR $APP_DIR

COPY main.py extract.py requirements.txt ./
RUN apt-get update
RUN apt-get install -y default-jdk
RUN pip install -r requirements.txt

EXPOSE 8080/tcp
CMD python3 main.py

