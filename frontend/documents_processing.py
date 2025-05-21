import streamlit as st
import requests

def process(BASE_URL:str):

    if st.button("Start Processing"):
        with st.spinner("📄 Processing..."):
            resp = requests.get(f"{BASE_URL}/process")
            st.write(resp.json()['message'])
            if resp.status_code == 200:
                st.success(f"{resp.json().get('message', '')}")
            else:
                st.error("Failed to process documents")
