FROM python:3.12
WORKDIR /app

COPY . .
RUN pip install --upgrade pip && pip install --upgrade setuptools && pip install -r requirements.txt

RUN chmod +x entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]