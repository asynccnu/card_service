FROM python:3.6
MAINTAINER Card

ENV DEPLOP_PATH /card

RUN mkdir -p $DEPLOP_PATH
WORKDIR $DEPLOP_PATH

ADD requirements.txt requirements.txt
RUN pip install --index-url http://pypi.doubanio.com/simple/ -r requirements.txt --trusted-host=pypi.doubanio.com

ADD . .