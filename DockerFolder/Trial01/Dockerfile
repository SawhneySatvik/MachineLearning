# Use an official Python runtime as a parent imag
FROM python:3.8-alpine

# Copy all the files and folders from the current directory to the /app directory in the container
COPY . /app

# Set the working directory to /app
WORKDIR /app

# Install the necessary dependencies
RUN pip install -r requirements.txt

# Expose the port that the application will run on
CMD python app.py