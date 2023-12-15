# Use an official Python runtime as the base image
FROM python:3.10-slim-buster

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE ekkbaz_containers.settings

# Create and set the working directory
WORKDIR /app


# Install system packages required for popular Python libraries
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev gcc git postgresql postgresql-contrib&&\
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# ... [Your existing Dockerfile content]

# Define build arguments
ARG GIT_BRANCH
ARG GIT_REPO="github.com/navinelahi/EkkBaz" # Default repo name, change if needed

# Clone the repo using the arguments

# ... [Rest of your Dockerfile content]


RUN git clone -b $GIT_BRANCH https://$GIT_REPO /app/


# Install Python dependencies
#COPY requirements.txt /app/
RUN cd myproject_original && pip install --upgrade pip && pip install -r requirements.txt

# Copy the current directory contents into the container at /app
#COPY . /app/

# Expose the port the app will run on
EXPOSE 8002