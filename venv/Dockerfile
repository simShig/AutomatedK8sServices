FROM ubuntu:latest
LABEL authors="Simon"

ENTRYPOINT ["top", "-b"]

FROM python:3.9-slim
WORKDIR /app
COPY bitcoin_service.py .
RUN pip install requests
CMD ["python", "bitcoin_service.py"]
