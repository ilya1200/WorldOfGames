# Use an official Python runtime as a parent image
FROM moditamam/selenium:python3

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container as /app
COPY . /app

# Install requirements
RUN pip install -r requirements.txt
RUN pip3 install pyvirtualdisplay

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONUNBUFFERED=1

# Make port 5001 available to services on the same docker network
EXPOSE 5001

ENV FLASK_APP=MainScores.py

# Run app.py when the container launches
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]