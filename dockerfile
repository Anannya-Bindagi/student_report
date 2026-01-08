FROM python:3.11

WORKDIR /se

COPY . .

CMD ["python", "student.py"]
