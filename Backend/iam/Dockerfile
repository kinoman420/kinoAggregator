# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install virtualenv
RUN pip install virtualenv

# Create a virtual environment
RUN virtualenv .venv

# Install dependencies in the virtual environment
RUN .venv/bin/pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Ensure the virtual environment's Python is used
ENV PATH="/app/.venv/bin:$PATH"

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--reload"]
