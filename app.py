import streamlit as st
from openai import OpenAI

from tools import scrape_text_from_html, summarize_text_with_openai

client = OpenAI()
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(temperature=0, model="gpt-4o")

st.write("## Article Summarizer")

if 'urls' not in st.session_state:
    st.session_state['urls'] = []

new_item = st.text_input("Enter url")

# Button to add the new item to the list
if st.button("Add article to summarize"):
    if new_item:
        st.session_state['urls'].append(new_item)
        st.success(f"Added: {new_item}")
        print(st.session_state['urls'])
    else:
        st.error("Please enter an item")


# Display the list of items
st.write("## Articles to Summarize")

if st.button("Summarize"):
    st.write("Summarizing articles...")
    print(st.session_state['urls'])
    for i, item in enumerate(st.session_state['urls']):
        st.write(f"{i + 1}. {item}")
        scraped_text = scrape_text_from_html(item)
        summary = summarize_text_with_openai(scraped_text)
        st.write(f"Summary: {summary}")

