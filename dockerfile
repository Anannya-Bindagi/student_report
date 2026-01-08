FROM python:3.11-slim

WORKDIR /stud_record

COPY student.py .
COPY test_student.py .

RUN pip install --no-cache-dir pytest

CMD ["bash"]
