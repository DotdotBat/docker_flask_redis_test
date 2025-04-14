FROM python:3.9-alpine
COPY requirements.txt /
RUN pip3 install -r requirements.txt
COPY app.py /
EXPOSE 5000
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]

