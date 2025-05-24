from fastapi import FastAPI
from services.translation_service import TranslationService

translation_service = TranslationService()

app = FastAPI(
        title="Langchain Server",
        version="1.0",
        description="A simple API server using Langchain runnable interfaces"
    )

@app.get("/")
async def root():
    return {"message": "Welcome to the Langchain Server API!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/translate")
async def run_chain(language: str = "English", text: str = "Hello, world!"):
    return translation_service.run_chain(language, text)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8282)