FROM ubuntu:latest
RUN apt-get update && apt-get install -y python3
COPY index.html /index.html
CMD ["python3", "-m", "http.server", "8080"]
EXPOSE 8080

FROM python:3
COPY index.html /index.html
CMD ["python3", "-m", "http.server", "8080"]
EXPOSE 8080