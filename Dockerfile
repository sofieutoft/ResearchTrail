# Use Python base image with specific version
FROM python:3.11

# Set working directory inside the container
WORKDIR /app

# Copy requirements.txt to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy all files from the current directory to the container
COPY . .

# Update EXPOSE and CMD in Dockerfile
EXPOSE 1024
CMD ["python", "app.py", "--port", "1024"]
