from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import load_prompt

#Config DotEnv
load_dotenv()
#Set page Title and layout
st.set_page_config(page_title="Book_Summarizer", page_icon="📚")
#Initialise the Model
model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

#App UI
st.header("Book Summarizer Tool")
# Description
st.write('''
📚 Book Summarizer - Your AI-Powered Reading Assistant! 🚀

✨ Instantly get a concise summary of any book you want!\n
📝 Just enter:\n
✅ Book Name
⚡ Summary Type (Easy, Medium, Detailed)
📏 Size Preference

Sit back and let AI do the reading for you! 📖💡
''')
col1, col2, col3 = st.columns([2, 1, 1])
with col1:
    Book_Name = st.text_input("Enter Book Name")
    
with col2:
    Style_Input = st.selectbox("Style", ["Easy", "Medium", "Book Language"], key="Style_Input")
    
with col3:
    Length_Input = st.selectbox("Length", ["Small", "Small-medium", "Medium", "large"], key="Length_Input")
    

#Prompt Template
template = load_prompt('Template.json')
# Fill the Placeholders
if st.button("Summarise"):
    chain = template | model
    result = chain.invoke({
    'Book_Name':Book_Name,
    "Style_Input":Style_Input,
    "Length_Input":Length_Input
     })
    st.write(result.content)