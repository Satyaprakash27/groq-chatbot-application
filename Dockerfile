
# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set working directory in container
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Make the entrypoint script executable
RUN chmod +x entrypoint.sh

# Create a non-root user to run the application
RUN useradd -m appuser
USER appuser

# Set environment variables
# Set to either STREAMLIT or FASTAPI
ENV APPLICATION_TYPE=STREAMLIT 
# Add your GROQ API key here or pass it at runtime
ENV GROQ_API_KEY=your_api_key_here

# Expose ports
# FastAPI runs on 8282, Streamlit on 8501
EXPOSE 8282 8501

# Set the entrypoint script
ENTRYPOINT ["./entrypoint.sh"]