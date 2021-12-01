FROM python:3.8-slim-buster

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENV TRANSFORMERS_OFFLINE 1
ENV PYTHONPATH "${PYTHONPATH}:/happy_gramformer"

ENTRYPOINT ["python3", "src/main.py"]