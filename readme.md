# Natural Language to Pinecone Filter Query Converter

This project converts natural language queries into structured, schema-conforming Pinecone-compatible metadata filter queries using LLMs from [GROQ](https://groq.com/). It's ideal for search systems that require precise vector filtering based on author, tags, or published date.

## 🚀 Features

- 🔁 Converts free-form user queries into strict JSON filter objects
- 🔎 Supports date interpretation (e.g., "last year", "June 2023")
- 🧩 Schema-controlled filters

## 🛠️ Technologies

- 🧠 LLMs via [GROQ API](https://groq.com/)
- 📡 HTTP requests using `requests`
- 📅 Dynamic date calculations based on current date
- 🔐 Environment configuration via `python-dotenv`

## 📁 Project Structure
├── query.py # Core logic to interact with GROQ LLM and parse filter queries
├── test.py # Test file with sample natural language inputs
├── .env # Environment variables (GROQ API key, etc.)
├── task.ipynb # Indexing the dataset_


## 🔧 Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/nsatya02/AI-Task.git
   cd AI-Task
   ```
2. **Create a virtual environment and activate**
  ```bash
  python -m venv venv
  source venv/bin/activate  # or venv\Scripts\activate on Windows
  ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up your .env file**
   ```bash
   GROQ_API_KEY=your_groq_api_key_here
   ```
5.**Usage**
Run the test script with sample queries:
```bash
python test.py
```
**Sample Output :**
```kotlin
Query: Show me articles by Alice Zhang from last year about machine learning.
{
  "status": "success",
  "query": {
    "author": "Alice Zhang",
    "tags": { "$in": ["machine learning"] },
    "published_date": {
      "$gte": "2024-01-01",
      "$lt": "2025-01-01"
    }
  }
}
```




