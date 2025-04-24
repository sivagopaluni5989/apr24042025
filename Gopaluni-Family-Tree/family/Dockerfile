# Use a lightweight Python image as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application file into the container
COPY app.py .
COPY templates/ ./templates/
COPY static/ ./static/


# Install Flask via pip
RUN pip install flask

# Expose port 5000 so that the container is accessible on that port
EXPOSE 5000

# Set the command to run the application
CMD ["python", "app.py"]

