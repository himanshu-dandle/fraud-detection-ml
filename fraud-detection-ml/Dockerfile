# Use the official Python image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy project files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir fastapi uvicorn joblib pandas numpy scikit-learn xgboost


# Expose the correct port for Google Cloud Run
EXPOSE 8080

# Run FastAPI on port 8080
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]

