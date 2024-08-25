FROM ubuntu:latest
LABEL authors="Simon"

ENTRYPOINT ["top", "-b"]


FROM python:3.9-slim

WORKDIR /app
COPY . /app
RUN pip install Flask
EXPOSE 5000
ENV FLASK_APP=hello_massage.py

CMD ["flask", "run", "--host=0.0.0.0"]
