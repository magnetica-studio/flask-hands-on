
FROM python:3.7.4
WORKDIR /app
COPY . .
RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN pip install PyMySQL[rsa]
ENV FLASK_APP ./src/app.py
ENV FLASK_RUN_HOST 0.0.0.0
CMD ["flask", "run"]