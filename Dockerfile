FROM python:3.7-alpine

ENV FLASK_APP mock-api-server.py

WORKDIR /usr/src/mock-api-server

COPY mock-api-server.py requirements.txt ./
COPY config /etc/mock-api-server
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD [ "python", "-m", "flask", "run", "--host", "0.0.0.0", "--port", "8080" ]
