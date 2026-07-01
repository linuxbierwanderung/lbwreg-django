FROM python:3.12
LABEL maintainer="lbedford@lbedford.org"

ENV PROJECT_ROOT /app
ENV PYTHONUNBUFFERED 1

RUN mkdir $PROJECT_ROOT
RUN mkdir -p /var/www/content
WORKDIR $PROJECT_ROOT

RUN apt update && apt install -y build-essential libmariadb-dev && apt clean
ADD . $PROJECT_ROOT/
RUN pip install -r requirements.txt

CMD /app/startup.sh
