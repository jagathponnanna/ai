from google import genai

client = genai.Client(api_key="ABC")

def build_rag_prompt(query, contexts, history):
    """
    Builds a grounded RAG prompt using retrieved contexts.
    
    Args:
        query (str): User question
        contexts (list[str]): Retrieved context chunks
    
    Returns:
        str: Final prompt
    """
    
    context_text = "\n".join(contexts)

    prompt = f"""
    You are a precise and reliable assistant.

    Your task is to answer the user's question ONLY using the provided context, and use your english skills to explain and elaborate it.

    CONTEXT:
    {context_text}

    HISTORY:
    {history}

    QUESTION:
    {query}

    ANSWER:
    """
    return prompt

def generate_response(q,context,history):
    prompt=build_rag_prompt(q,context,history)
    response = client.models.generate_content(
        model="gemini-2.5-flash",  
        contents=prompt,
        config={
            "temperature": 0.1,
            "max_output_tokens": 500,
        }
    )

    return response.text

