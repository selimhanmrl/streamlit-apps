FROM python:3.11.4-slim as base

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/selimhanmrl/streamlit-apps .

RUN pip install -r streamlit-apps/Regression/requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "stock.py", "--server.port=8501", "--server.address=0.0.0.0"]
