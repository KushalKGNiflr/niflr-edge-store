# Base image
FROM python:3.9-slim-buster


# Set working directory
WORKDIR /app

ENV TZ=Asia/Kolkata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Copy requirements.txt to working directory
COPY env .

COPY code .

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy code to working directory

# Expose port 8000
EXPOSE 8000

# Start the server
CMD ["python3", "manage.py", "runserver"]
