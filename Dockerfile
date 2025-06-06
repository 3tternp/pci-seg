FROM python:3.10-slim

# Set environment to avoid prompts during install and ensure consistent behavior
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies (nmap, gcc, etc.)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    nmap \
    gcc \
    libffi-dev \
    libxml2-dev \
    libxslt1-dev \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files into container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Define the command to run your main script
CMD ["python", "main.py"]
