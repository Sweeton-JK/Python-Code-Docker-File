FROM python:3.10.0
CMD ["apt-get", "python3-pip"]

RUN apt-get update && apt-get install -y openjdk-8-jdk
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "euler.py"]

EXPOSE 8888