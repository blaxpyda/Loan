FROM python:3.13-alpine

WORKDIR /app

COPY ../requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY frontend/main.py .

EXPOSE 8501

CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]