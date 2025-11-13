# Use official Python image
FROM python:3.12

# Create and set working directory
WORKDIR /app

# Copy dependency file first (spelling fixed: requirements.txt)
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all remaining project files
COPY . .

# Expose the app port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
