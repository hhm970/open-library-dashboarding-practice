FROM python:latest

WORKDIR ./app

COPY requirements.txt

RUN pip3 install -r requirements.txt

COPY extract.py .

COPY wrangle.py .

COPY diagrams.py .

COPY main.py .

CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]