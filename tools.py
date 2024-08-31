import streamlit as st
import requests
from bs4 import BeautifulSoup
from openai import OpenAI

client = OpenAI()


def scrape_text_from_html(url):
    # Fetch the content from the URL
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract text from the HTML
    text = soup.get_text(separator=' ', strip=True)

    return text


def summarize_text_with_openai(text, max_tokens=1000):
    # Use the OpenAI API to generate a summary of the text
    response = client.chat.completions.create(model="gpt-4o",
                                              messages=[{"role": "system",
                                                         "content": "Additional Context: You are a journalist tasked with writing summaries for news articles to be featured in a weekly newsletter."
                                                                    "Instructions: Provide a concise summary of the following news article, focusing on the main points and key takeaways. "
                                                                    "Use clear and concise language suitable for a general audience and maintain a neutral and objective tone."
                                                                    "Constraints: "
                                                                    "- Keep the summary within 100-150 words"
                                                                    "Output Format:"
                                                                    "    Main"
                                                                    "    Topic: [Brief introduction capturing the main topic of the article] "
                                                                    "    Key Points: "
                                                                    "- [Key point 1]"
                                                                    "    - [Key point 2]"
                                                                    "    - [Key point 3]"
                                                                    "    Significance: [Sentence highlighting the article's significance or impact]"},
                                                        {"role": "user", "content": "Article: ```"+text+"```"}],
                                              )
    summary = response.choices[0].message.content
    return summary