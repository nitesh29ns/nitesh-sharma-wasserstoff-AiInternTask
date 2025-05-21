from langchain_community.document_loaders import PyPDFLoader
from db.mongodb import database
import config
import easyocr
import os
import shutil

# OCR Reader
reader = easyocr.Reader([config.OCR_LANGUAGE])

# MongoDB
coll = database[config.DOCUMENT_COLLECTION]

def upload_docs_from_files(file_paths: list):
    for file_path in file_paths:
        filename = os.path.basename(file_path).lower()
        collection = {}

        if filename.endswith(".pdf"):
            try:
                loader = PyPDFLoader(file_path)
                document = loader.load()
                doc = [page.page_content for page in document]
                meta = [page.metadata for page in document]
                collection['filename'] = filename
                collection['documents'] = doc
                collection['metadatas'] = meta
            except Exception as e:
                print(f"❌ PDF processing failed: {filename}, Error: {e}")
                continue

        elif filename.endswith((".jpg", ".jpeg")):
            try:
                result = reader.readtext(file_path)
                extracted_text = ' '.join([text for _, text, _ in result])
                collection['filename'] = filename
                collection['documents'] = extracted_text
                collection['metadatas'] = {'source': filename}
            except Exception as e:
                print(f"❌ OCR failed for: {filename}, Error: {e}")
                continue
        else:
            print(f"⚠️ Unsupported file format: {filename}")
            continue

        coll.insert_one(collection)
        print(f"✅ Inserted {filename} into MongoDB")

    return f"{len(file_paths)} files processed and stored successfully."
