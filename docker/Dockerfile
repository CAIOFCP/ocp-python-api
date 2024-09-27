FROM registry.access.redhat.com/ubi9/python-39:1-117.1684741281
MAINTAINER caiofcp@br.ibm.com
RUN apt-get update
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN python3 -m pip install -r requirements.txt
COPY ./src /app/src
EXPOSE 8081/tcp
CMD ["python3" , "app.py"]
