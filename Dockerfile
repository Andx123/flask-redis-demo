# lightweight Python base image
FROM python:3.10-slim
# set working directory inside the container
WORKDIR /app
# copy application code
COPY app/ ./
RUN pip install -r requirements.txt

# start the Flask app
CMD ["python", "app.py"]
