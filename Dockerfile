# Use an official Python runtime as a parent image
FROM python:3.8-slim
RUN apt-get update && apt-get install -y procps less wget curl net-tools

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container as /app
COPY . /app

# Install requirements
RUN pip install -r requirements.txt

# Make port 5001 available to services on the same docker network
EXPOSE 5001

# Run app.py when the container launches
CMD python MainScores.py