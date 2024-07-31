FROM python:3.6-slim
COPY . /app
RUN pip install --no-cache-dir -r /app/requirements.txt
WORKDIR /app
CMD ["python", "main.py"]
