FROM python:alpine3.14

COPY . .
RUN chmod -R 777 /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]