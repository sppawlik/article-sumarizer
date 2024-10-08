import requests
from bs4 import BeautifulSoup
from openai import OpenAI

client = OpenAI()


# Set your OpenAI API key here
# Replace with your OpenAI API key


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


def main():
    url = "https://news.mit.edu/2024/ai-assistant-monitors-teamwork-promote-effective-collaboration-0819"  # Replace with the target URL

    # Step 1: Scrape the text from the HTML page
    scraped_text = scrape_text_from_html(url)

    print("Scraped Text:")
    print(scraped_text)
    print("\n---\n")

    # Step 2: Summarize the scraped text using OpenAI
    summary = summarize_text_with_openai(scraped_text)

    print("Summary:")
    print(summary)


if __name__ == "__main__":
    main()
