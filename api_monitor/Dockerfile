FROM python:3.10-slim

# Set environment
WORKDIR /app

# Copy files
COPY . /app

# Install dependencies 
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port for the API 
EXPOSE 5050

# Run the API
CMD ["python", "app.py"]
