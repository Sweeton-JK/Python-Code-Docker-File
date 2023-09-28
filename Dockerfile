FROM python:3.9

COPY . .

RUN pip install numpy matplotlib

CMD ["python", "mandelbrot.py"]
