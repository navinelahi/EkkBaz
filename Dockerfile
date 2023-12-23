# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /usr/src/app

# Install system dependencies for PostGIS
RUN apt-get update && apt-get install -y \
    binutils \
    libproj-dev \
    gdal-bin \
    postgresql-client \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Clone the specific branch of your repository from GitHub
RUN git clone -b branch5_ec2_working https://github.com/navinelahi/EkkBaz.git .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8001

# Define environment variable
ENV PYTHONUNBUFFERED 1

# Start the Django application
CMD ["python", "myproject_original/manage.py", "makemigrations", "authorize"]
CMD ["python", "myproject_original/manage.py", "migrate", "authorize"]
CMD ["python", "myproject_original/manage.py", "makemigrations", "business"]
CMD ["python", "myproject_original/manage.py", "migrate", "business"]
CMD ["python", "myproject_original/manage.py", "runserver", "0.0.0.0:8001"]
