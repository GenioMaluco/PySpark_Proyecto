﻿FROM bitnami/spark:3.5.0

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/

CMD ["spark-submit", "--master", "local[*]", "/app/src/main.py"]
