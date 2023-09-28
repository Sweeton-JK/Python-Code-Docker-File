FROM python:3.8

WORKDIR /app

COPY kmeans.py .

RUN pip install numpy scikit-learn matplotlib

CMD ["python", "kmeans.py"]