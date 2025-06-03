FROM python:3.10-slim

# Install system dependencies including Nmap
RUN apt-get update && \
    apt-get install -y nmap python3-venv && \
    apt-get clean

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set default command
CMD ["python", "main.py"]
