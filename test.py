from query import build_pinecone_query

sample_queries = [
    "Show me articles by Alice Zhang from last year about machine learning.",
    "Find posts tagged with ‘LLMs’ published in June, 2023.",
    "Anything by John Doe on vector search?",
]

for q in sample_queries:
    print(f"\nQuery: {q}")
    print(build_pinecone_query(q))
