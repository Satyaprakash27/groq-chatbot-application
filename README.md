# Groq Chatbot Application

A chatbot application that leverages the Groq Large Language Model (LLM) for interactive conversations.

## Overview
This application provides an interface to interact with Groq's language model, enabling natural language conversations and AI-powered responses.

## Features
- Integration with Groq LLM
- Interactive chat interface
- Natural language processing capabilities

## Getting Started
### Generate the Groq API Key
1. Sign up for a Groq account at [Groq's website](https://console.groq.com).
2. Generate your API key from the Groq console.
3. Create a `.env` file in the project root directory.
4. Add your API key to the `.env` file:
    ```
    GROQ_API_KEY=your_api_key_here
    ```
5. Keep your `.env` file secure and never commit it to version control.

### Running and hosting the application locally
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/groq-chatbot-application.git
    cd groq-chatbot-application
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

#### For Fast API application
4. Start the FastAPI server:
    ```bash
    uvicorn fastapi_app:app --reload
    ```

5. Access the application:
    - Open your browser and navigate to `http://localhost:8282`
    - The API documentation is available at `http://localhost:8282/docs`

#### For Streamlit application
4. Start the Streamlit application:
    ```bash
    streamlit run streamlit_app.py
    ```

5. Access the application:
    - Open your browser and navigate to `http://localhost:8501`
    - The application will automatically reload when you make changes to the code

### Creating Docker image
1. Build the Docker image:
    ```bash
    docker build -t groq-chatbot-app .
    ```

3. Run the container:
    ```bash
    # To run as FastAPI:
    docker run -e APPLICATION_TYPE=FASTAPI -p 8282:8282 groq-chatbot-app
    
    # To run as Streamlit:
    docker run -e APPLICATION_TYPE=STREAMLIT -p 8501:8501 groq-chatbot-app
    ```

4. Access the application:
    - For FastAPI: Navigate to `http://localhost:8282`
    - For Streamlit: Navigate to `http://localhost:8501`

## Requirements
- Groq API access
