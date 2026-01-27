FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
# Match the Flask port
EXPOSE 5005
CMD ["python", "app.py"]
