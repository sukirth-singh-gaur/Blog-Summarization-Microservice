from google import genai
import os
from dotenv import load_dotenv # type: ignore
from bs4 import BeautifulSoup # type: ignore

load_dotenv()

apiKey = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=apiKey)

def truncate_text(text: str, max_chars: int = 1000) -> str:
    return text[:max_chars]

def extract_text_from_html(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")

    # Remove code blocks & scripts explicitly
    for tag in soup(["script", "style", "pre", "code"]):
        tag.decompose()

    text = soup.get_text(separator=" ")
    return " ".join(text.split())

def generate_summary(content : str) -> str:
    clean_text = extract_text_from_html(content)
    clean_text = truncate_text(clean_text)
    if len(clean_text) < 200:
        return clean_text
    
    prompt= f"""
    Summarize this blog in 2–3 concise sentences.
    Start with "TL;DR:".
    Be neutral and informative.
    Blog : {clean_text}
    """
    response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=prompt
    )
    return response.text;

# content = """
#     Hello this is a text
#     """
#print(generate_summary(content));
