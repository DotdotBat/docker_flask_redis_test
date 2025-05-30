FROM python:3.9-alpine
WORKDIR /app
COPY requirements.txt /app/
RUN pip3 install -r requirements.txt
COPY app.py /app/
EXPOSE 5000
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]