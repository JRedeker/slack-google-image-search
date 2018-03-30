FROM tiangolo/uwsgi-nginx-flask:flask


RUN apt-get update -y \
	&& apt-get install -y python-pip python-dev build-essential 


# clean up installs
RUN rm -rf /var/lib/apt/lists/*

COPY ./app /app

COPY requirements.txt /tmp

WORKDIR /tmp

RUN pip install -r requirements.txt

WORKDIR /app

ENTRYPOINT ["python"]

CMD ["/app/app.py"]
