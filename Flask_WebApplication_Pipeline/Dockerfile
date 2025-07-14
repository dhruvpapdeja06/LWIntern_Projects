FROM redhat/ubi8

RUN yum -y update && \
    yum install python3-pip -y && \
    yum clean all 

RUN pip3 install flask

WORKDIR /webApp

COPY ./app.py /webApp/

EXPOSE 5000

CMD [ "python3","/webApp/app.py" ]