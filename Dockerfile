FROM python:3.10.0
CMD ["apt-get", "python3-pip"]

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "euler.py"]