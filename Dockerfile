FROM python:2.5-alpine
MAINTAINER Sam Gabrail
RUN apk update && pip install bottle \
    && mkdir /app
WORKDIR /app
COPY . .
EXPOSE 22
CMD ["python", "-u", "sysdigCool.py"]
