import streamlit as st
import requests
from bs4 import BeautifulSoup
from openai import OpenAI

client = OpenAI(api_key='sk-proj-5sGwuWxoZbHibNynGZ5kT3BlbkFJW8moevSr9Yaw1nl8lcA4')


def scrape_text_from_html(url):
    # Fetch the content from the URL
    response = requests.get(url)
    response.raise_for_status()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract text from the HTML
    text = soup.get_text(separator=' ', strip=True)

    return text


def summarize_text_with_openai(text, max_tokens=1000):
    # Use the OpenAI API to generate a summary of the text
    response = client.chat.completions.create(model="gpt-4o",
                                              messages=[{"role": "system", "content": "summarize the text"},
                                                        {"role": "user", "content": text}],
                                              )
    summary = response.choices[0].message.content
    return summary