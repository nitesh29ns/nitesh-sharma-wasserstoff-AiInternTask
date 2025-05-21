import streamlit as st
import requests


def show_document_selector(BASE_URL:str):
    # Load button
    if st.button("Load Document List"):
        with st.spinner("Loading documents..."):
            resp = requests.get(f"{BASE_URL}/extractfiles")
            if resp.status_code == 200:
                st.session_state['files_list'] = resp.json()
                st.session_state['selected_docs'] = set()
                st.session_state['page'] = 0
                # Reset all checkbox states
                for doc in st.session_state['files_list']:
                    st.session_state[f"doc_checkbox_{doc}"] = False
                st.success("Documents loaded")
            else:
                st.error("Failed to load documents")

    files_list = st.session_state.get('files_list', [])
    selected_docs = st.session_state.get('selected_docs', set())
    page = st.session_state.get('page', 0)
    PAGE_SIZE = 10
    total_pages = (len(files_list) - 1) // PAGE_SIZE + 1

    if files_list:
        # Pagination boundaries
        start = page * PAGE_SIZE
        end = start + PAGE_SIZE
        current_docs = files_list[start:end]

        # Select/Deselect All
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("Select All"):
                for doc in files_list:
                    st.session_state[f"doc_checkbox_{doc}"] = True
                st.session_state['selected_docs'] = set(files_list)

        # Document checkboxes
        for doc in current_docs:
            checked = st.checkbox(doc, key=f"doc_checkbox_{doc}")
            if checked:
                st.session_state['selected_docs'].add(doc)
            else:
                st.session_state['selected_docs'].discard(doc)

        # Pagination controls
        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            if st.button("Previous") and page > 0:
                st.session_state['page'] -= 1
        with col3:
            if st.button("Next") and page < total_pages - 1:
                st.session_state['page'] += 1
        with col2:
            st.markdown(f"<center>Page {page + 1} of {total_pages}</center>", unsafe_allow_html=True)

        # Show selected docs
        st.markdown("**Selected Documents:**")
        st.code(list(st.session_state['selected_docs']))

        # Submit selection
        if st.button("Cache Selected Documents"):
            with st.spinner("Cache Selected Documents..."):
                if st.session_state['selected_docs']:
                    resp = requests.post(
                        f"{BASE_URL}/selected_docs",
                        json={"documents": list(st.session_state['selected_docs'])}
                    )
                    if resp.status_code == 200:
                        st.success(f"Documents cached successfully.. {resp.json().get('message', '')}")
                    else:
                        st.error("Failed to cache documents")
                else:
                    st.warning("No documents selected")
