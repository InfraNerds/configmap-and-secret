FROM python:alpine3.15
COPY . .
RUN pip install -r requirements.txt

COPY lib/step-codefresh.py /step-codefresh.py

CMD ["python","u","/step-codefresh.py"]
