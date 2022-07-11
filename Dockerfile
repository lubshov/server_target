FROM python:3.9.7
ENV PYTHONUNBUFFERED=1

RUN apt-get update

RUN mkdir /code


COPY . /code/
WORKDIR /code
RUN pip install -r requirements.txt

WORKDIR /code/todoapp/todoapp
EXPOSE 8000/udp

ENTRYPOINT ["python3"]
#RUN python3 ../manage.py migrate
#RUN python3 ../manage.py runserver
#CMD ["../Hello.py"]
#CMD ["../manage.py", "makemigrations"]
#CMD ["../manage.py", "migrate"]
CMD ["../manage.py", "runserver"]

