# USE A BASE IMAGE
FROM alpine
# INSTALL DEPENDENCY
RUN apk add python3 py3-pip
RUN apk add --update redis
ADD index.html /index.html
# RUN WHICH PRGM
CMD ["python", "-m", "http.server", "8080"]
EXPOSE 8080