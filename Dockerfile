# Use a slim Python 3.12 base image to reduce size
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker caching
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port (Render assigns dynamically, but good practice)
EXPOSE 8020

# Run FastAPI with uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8020"]
