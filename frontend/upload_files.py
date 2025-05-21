import streamlit as st
import os, requests

from backend.app.services.new_upload import upload_docs_from_files


def uploading_files(BASE_URL:str):

    uploaded_files = st.file_uploader("Choose files",  type=["pdf","jpg"],accept_multiple_files=True)

    if st.button("Upload Files"):
        
        if uploaded_files:
            with st.spinner("Uploading documents..."):
                save_dir = "uploaded_pdfs"
                os.makedirs(save_dir, exist_ok=True)

                file_paths = []
                for uploaded_file in uploaded_files:
                    path = os.path.join(save_dir, uploaded_file.name)
                    file_paths.append(path)
                    with open(path, "wb") as f:
                                f.write(uploaded_file.getvalue())

                # Prepare multipart form-data
                files = [('files', (os.path.basename(path), open(path, 'rb'))) for path in file_paths]

                #resp = requests.post(f"{BASE_URL}/upload", files=files)
                resp = uploaded_files(file_paths=files)
                if resp.status_code == 200:
                        st.success(f"{resp.json().get('message', '')}")
                else:
                    st.error("Failed to cache documents")
        else:
            st.warning("Please upload one or more files")