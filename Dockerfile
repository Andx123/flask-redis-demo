FROM python:3.10-slim  # lightweight Python base image

WORKDIR /app           # set working directory inside the container
COPY app/ ./           # copy application code
RUN pip install -r requirements.txt

CMD ["python", "app.py"]  # start the Flask app
