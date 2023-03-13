FROM python:latest

WORKDIR /opt
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .
COPY templates .

CMD ["python", "app.py"]

