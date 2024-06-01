# Use the official TensorFlow image based on Debian
FROM tensorflow/tensorflow:2.5.0

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the requirements file to the working directory
COPY requirements.txt ./

# Install additional dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY src ./src
COPY templates ./templates

# Expose the port the Flask app runs on
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "src/app.py"]

