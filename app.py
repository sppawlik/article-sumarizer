import streamlit as st
from openai import OpenAI

from tools import scrape_text_from_html, summarize_text_with_openai

client = OpenAI()
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(temperature=0, model="gpt-4o")

st.write("## Article Summarizer")
url = st.text_input("Enter url")

if st.button("Summarize"):
    scraped_text = scrape_text_from_html(url)
    summary = summarize_text_with_openai(scraped_text)
    st.write(f"Summary: {summary}")


