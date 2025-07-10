FROM python:3.11-slim 

# Set the working directory in the container
WORKDIR /app 

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . . 

# Expose the port that FastAPI will run on
EXPOSE 8080

# Command to run the FastAPI application
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8080"]