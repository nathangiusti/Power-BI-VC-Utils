  
FROM python:3

COPY . .

CMD [ "python", "/src/main.py" ]
