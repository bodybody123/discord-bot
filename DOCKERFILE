FROM python:3.10
WORKDIR /cornifer
COPY requirements.txt /cornifer/
RUN pip install -r requirements.txt
COPY . /cornifer
CMD python cornifer.py