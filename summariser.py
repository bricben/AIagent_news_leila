import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def summarize_and_analyze(article):
    prompt = f"""
    Summarize the following news article in one sentence and then write a short paragraph analyzing its implications using sound economic theory.

    Article:
    {article['text']}

    Return JSON:
    {{
        "summary": "...",
        "analysis": "...",
        "importance": 0-10 (based on impact on global markets)
    }}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    try:
        result = eval(response.choices[0].message["content"])  # Use literal_eval for safety in production
    except:
        result = {
            "summary": "Summary failed.",
            "analysis": "Analysis failed.",
            "importance": 1
        }

    return {
        "title": article["title"],
        "url": article["url"],
        **result
    }