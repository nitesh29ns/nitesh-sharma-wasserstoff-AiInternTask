import streamlit as st
import pandas as pd
import json
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

res = [{'document_name': 'd20357592', 'theme': 'Debt Recovery', 'extracted_answer': 'No specific cost breakdown for debt recovery mentioned', 'citation': 'Page 1'}, {'document_name': 'd20346323', 'theme': 'Debt Recovery', 'extracted_answer': 'No specific cost breakdown for debt recovery mentioned', 'citation': 'Page 0'}, {'document_name': 'd20360688', 'theme': 'Debt Recovery', 'extracted_answer': 'No specific cost breakdown for debt recovery mentioned', 'citation': 'Page 1'}, {'document_name': 'd20345878', 'theme': 'Debt Recovery', 'extracted_answer': "Report on pre-judgment attachment: Court enforcement officer or private bailiff issues and delivers a report on the attachment of Defendant's assets (no cost specified)", 'citation': 'Page 0'}, {'document_name': 'd20357001', 'theme': 'Debt Recovery', 'extracted_answer': 'No specific cost breakdown for debt recovery mentioned', 'citation': 'Page 1'}]



# Convert to DataFrame
#df = pd.DataFrame(output)

# Show as interactive table
#st.dataframe(df, width=1200, height=600) #use_container_width=True


import streamlit as st
import os, requests, json
import pandas as pd

    
query = st.text_input("Enter your question here:")
if st.button("Get Response"):
    output = res
    #print(type(output['content']))
    #data_list = json.loads(output['llm_output']["content"])
    #st.text_area("LLM Output", value=data_list, height=300)
    #df = pd.DataFrame(res)
    # Show as interactive table
    #st.dataframe(df, use_container_width=True) 
    synthesized_response = generate_theme_summary(output)
    st.text_area(label="synthesized_response", value=synthesized_response,height=300)