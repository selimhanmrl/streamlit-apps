FROM python:3.11.4-slim as base

WORKDIR /app

EXPOSE 8501

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt


COPY . .

#HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "stock.py"]
