import streamlit as st
import os, requests
import pandas as pd
from collections import defaultdict

def generate_theme_summary(data):
    theme_groups = defaultdict(list)

    # Group by theme
    for item in data:
        theme_groups[item['theme']].append(item)

    summary_lines = []
    for i, (theme, entries) in enumerate(theme_groups.items(), 1):
        doc_ids = ", ".join(item['document_name'] for item in entries)
        line = f"Theme {i} – {theme}:\nDocuments ({doc_ids}) highlight:"
        for item in entries:
            line += f"\n- {item['extracted_answer']} (Citation: {item['citation']})"
        summary_lines.append(line)

    return "\n\n".join(summary_lines)

def llm_response(BASE_URL:str):
    
    query = st.text_input("Enter your question here:")
    if st.button("Get Response"):
        if not query:
            st.warning("Please enter a question")
        else:
            resp = requests.post(f"{BASE_URL}/response", json={"query": query})
            if resp.status_code == 200:
                output = resp.json().get("llm_output")

                # Handle llm time out because the use of free tier.
                if isinstance(output, str):
                    st.text_area(label="LLM Output (Error or Message)", value=output, height=300)

                # If the output is a list
                elif isinstance(output, list) and all(isinstance(item, dict) for item in output):
                    df = pd.DataFrame(output)
                    st.dataframe(df, use_container_width=True)

                    synthesized_response = generate_theme_summary(output)
                    st.text_area(label="Synthesized Response", value=synthesized_response, height=300)

                else:
                    st.warning("Unexpected format in LLM output.")
                    st.write(output)

            else:
                st.error("Error getting response")
