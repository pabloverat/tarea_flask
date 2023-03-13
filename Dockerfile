FROM python:latest

WORKDIR /opt
COPY requirements.txt .
RUN pip install -r /opt/requirements.txt

COPY app.py .
COPY templates ./templates/
COPY README.md .

CMD ["python", "app.py"]

