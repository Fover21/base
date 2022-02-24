#FROM blackice1414/python395-fastapi:latest
FROM rackspacedot/python38:latest

RUN sed -i 's/deb.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list

#RUN apt-get update && apt-get -y install openssh-server vim apt-utils && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /usr/src/app/log

WORKDIR /usr/src/app
ENV PYTHONPATH /usr/src/app


COPY requirements.txt /usr/src/app/requirements.txt

RUN pip install -i https://pypi.douban.com/simple pip==20.2.1 virtualenv==16.1.0 virtualenv-clone==0.4.0 setuptools==39.0.1
#RUN pip3 install -i https://pypi.douban.com/simple --upgrade pip3
RUN pip install -i https://pypi.douban.com/simple -r requirements.txt

COPY . /usr/src/app

EXPOSE 8080
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo '$TZ' > /etc/timezone

CMD ["python", "/usr/src/app/main.py"]
