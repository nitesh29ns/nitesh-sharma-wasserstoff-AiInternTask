# nitesh-sharma-wasserstoff-AiInternTask

## Task Details -- Document Research & Theme Identification Chatbot

## Dataset 
Collect Data from World Bank using there API `https://search.worldbank.org/api/v3/wds` on `Business Domian`.
---
## 1. Document Upload and Knowledge Base Creation

Accepts 75+ documents including PDFs and scanned images, Process `PDF` using `from langchain_community.document_loaders import PyPDFLoader` and `scanned images` using `easyOCR`, Text content extract accurately.

Using `NoSql Database` `mongdb` for storing extracted text with their document name and metadata.


## 2. Document Management & Query Processing

Frontend build using `Streamlit` which is very simmple user friendly. User can `select` the `desired documents` from which he wants to extract information. 

Intigrating the `frontend` with the `backend` using `FastAPI`.

Using `ThreadPoolExecutor` for `fast processing` of text, using `chromadb` for vector stage to get the `similarity_search` based on the theme was extracted. `compress` the `vector db` to store in the `mongodb` for `reuse`.

Accept query in `Nature language` and utilizing `llama-3.3-70b-versatile` llm model through `groq` to get desired result.
`Final output` is in the `specified format`.


## 3. Theme Identification & Cross-Document Synthesis

Through `llm` Analyze responses from all documents collectively and `identify the coherent themes` across the` multiple documents`.

Output is `structured` like `document_id`, `Extracted answer`, `Citation` and `Final synthesized response`.

Update the existing collection of each pdf containing meta data with summary and keywords. use the existing pickle objects that we generate from summarization.py and keyword.py .
