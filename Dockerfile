FROM python:3.6-slim
COPY ./requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY . /app
WORKDIR /app
CMD ["python", "main.py"]
