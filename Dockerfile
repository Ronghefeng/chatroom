FROM python:3.9

LABEL maintainer="rhf"

RUN mkdir -p /home/rhf/app
WORKDIR /home/rhf/app

ADD ./requirements.txt /home/rhf/app/requirements.txt 

# RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip 
RUN pip3 install --upgrade pip 
RUN pip3 install -r requirements.txt 

ADD . /home/rhf/app 

CMD python manage.py

