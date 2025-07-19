FROM redhat/ubi8

RUN yum upgrade -y && \
    yum install python3-pip -y && \
    pip3 install flask

WORKDIR /webApp

COPY ./CI_CD_Automation/dev/app.py /webApp

EXPOSE 5000

CMD [ "python3", "/webApp/app.py" ]


