import os
import requests
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL_NAME = "llama3-70b-8192"

SYSTEM_PROMPT = """
You are a strict JSON generator that converts natural language into a Pinecone-compatible filter query.
You should only calculate the dates like last year, last month etc based on the current date.
Use only this schema:
- author: string
- tags: { "$in": [list of strings] }
- published_date: { "$gte": "YYYY-MM-DD", "$lt": "YYYY-MM-DD" }
- OR use published_year and published_month as:
  "published_year": { "$eq": YEAR },
  "published_month": { "$eq": MONTH }

RULES:
1. Use "tags": { "$in": [...] } always, never just a list.
2. If the query includes vague time periods like "last year", convert to published_date with $gte and $lt in ISO date format.
  eg :- "last year" = $gte: "YYYY-MM-DD", $lt: "YYYY-MM-DD"
3. If the query includes a specific year/month (e.g. January 2022), use:
   "published_year": { "$eq": 2022 }, "published_month": { "$eq": 1 }
4. Always return strict JSON.
5. Never include explanation or natural language.
6. Always calculate dates like "last year", "last month", "last week", etc., using the current date as the reference point.
"""



def build_pinecone_query(user_query: str):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_query}
        ],
        "temperature": 0.2
    }

    try:
        res = requests.post(GROQ_URL, json=payload, headers=headers)
        res.raise_for_status()
        content = res.json()["choices"][0]["message"]["content"]
        result = eval(content)  # safer alternative: json.loads() if formatting is reliable

        print(result)
        return {"status": "success", "query": result}
    except Exception as e:
        return {"status": "error", "message": str(e), "raw_output": res.text}
