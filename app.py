import streamlit as st 
st.set_page_config(Layout="wide")
st.title("Semantic Search and Summarization Application")
uploaded_pdf=st.file_uploader("Upload your PDF",type=['pdf'])
if uploaded_pdf is not None:
    col1,col2,col3 = st.colums([2,1,1])

    with col1:
        pass
