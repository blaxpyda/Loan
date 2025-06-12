FROM python:3.13-alpine

# set up working directory
WORKDIR /app

# Copy and install dependencies
COPY ../requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# copy source
COPY backend/main.py .

# expose port
EXPOSE 8000

# start the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]