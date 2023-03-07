# Pull official base Python Docker image
FROM python:3.10.6
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# Create group and user
RUN addgroup --g 1000 groupcontainer
RUN adduser -u 1000 -G groupcontainer -h /home/containeruser -D containeruser
USER containeruser
# Set work directory
WORKDIR /home/containeruser/code
# Install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /home/containeruser/code/
RUN pip install -r requirements.txt
# Copy the Django project
COPY . /home/containeruser/code/




