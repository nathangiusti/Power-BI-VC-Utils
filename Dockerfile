# Container image that runs your code
FROM python:3.9-alpine

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY entrypoint.sh /entrypoint.sh
COPY $1 /$1
COPY run.py /run.py

# Code file to execute when the docker container starts up (`entrypoint.sh`)
CMD ["python", "run.py", "$1"]
