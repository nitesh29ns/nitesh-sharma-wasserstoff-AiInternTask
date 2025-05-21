import streamlit as st
import requests
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.app import config
from documents_processing import process
from document_selector import show_document_selector
from upload_files import uploading_files
from llm_query import llm_response

BASE_URL = config.BASE_URL  # change if your FastAPI is hosted elsewhere
def main():
    
    st.set_page_config(layout="wide")

    # about me 
    with st.sidebar:
        st.header("About")
        st.write("""
            My Name is Nitesh Sharma. I am using llama-3.3-70b-versatile model.
            ***
            github :- https://github.com/nitesh29ns/nitesh-sharma-wasserstoff-AiInternTask
                
            linkdin :- https://www.linkedin.com/in/nitesh-sharma-0a260b183/
            """)


    st.title("Business Document AI")

    # Step 1: Upload files
    st.header("Upload Documents")
    uploading_files(BASE_URL=BASE_URL)


    # Step 2: Trigger processing
    st.header("Process Uploaded Documents")
    process(BASE_URL=BASE_URL)


    # Step 3: Get extracted file list and select files
    st.header("Select Documents for Query")
    show_document_selector(BASE_URL=BASE_URL)


    # Step 4: Enter query and get response
    st.header("Ask Question")
    llm_response(BASE_URL=BASE_URL)



if __name__ == "__main__":
    main()