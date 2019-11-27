FROM python:3.8.0-alpine

RUN pip install pytest

RUN mkdir /app
WORKDIR /app
COPY *.py /app/

RUN pytest palindrome_checker_test.py