#!/bin/bash
# This script serves as the entrypoint for the Docker container
# It will run either uvicorn for FastAPI or streamlit based on APPLICATION_TYPE

set -e

# Check application type and run appropriate command
if [ "$APPLICATION_TYPE" = "FASTAPI" ]; then
    echo "Starting application in FastAPI mode..."
    # Using the adapter file that loads the FastAPI app
    exec uvicorn fastapi_app:app --host 0.0.0.0 --port 8282 --reload
elif [ "$APPLICATION_TYPE" = "STREAMLIT" ]; then
    echo "Starting application in Streamlit mode..."
    exec streamlit run streamlit_app.py --server.port 8501 --server.address 0.0.0.0
else
    echo "Error: Invalid APPLICATION_TYPE value. Must be FASTAPI or STREAMLIT."
    exit 1
fi
