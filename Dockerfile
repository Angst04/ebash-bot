FROM python:3.9 

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    automake \
    libtool \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]