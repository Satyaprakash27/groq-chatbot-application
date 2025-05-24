import streamlit as st
from services.translation_service import TranslationService

translation_service = TranslationService()

def host_streamlit_app():
    st.title("Text translation service")
    st.write("This app allows you to translate text into different languages using a simple interface.")
    
    language = st.text_input("Enter the language", "English")
    text = st.text_area("Enter your text", "Hello, world!")
    
    if st.button("Process"):
        result = translation_service.run_chain(language, text)
        st.write("Result:", result)

if __name__ == "__main__":
    host_streamlit_app()