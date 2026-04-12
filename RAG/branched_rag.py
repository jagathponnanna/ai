from google import genai

client = genai.Client(api_key="")



def decompose_query(query):
    prompt = f"""
    Break this question into 3 short sub-questions.

    Return ONLY a Python list.

    Question:
    {query}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",   
        contents=prompt)
    try:
        sub_queries = eval(response.text)
    except:
        sub_queries = [query]  
    return sub_queries



def retrieve_context(query):

    return [
        f"Context related to: {query}",
        "Additional relevant info"
    ]



def answer_branch(query, contexts):
    context_text = "\n".join(contexts)

    prompt = f"""
    Answer ONLY using the context below.
    If not found, say "Not found in context".

    Context:
    {context_text}

    Question:
    {query}

    Answer:
    """
    response = client.models.generate_content(
    model="gemini-2.5-flash",   
    contents=prompt)
    return response.text



def combine_answers(main_query, branch_answers):
    combined = "\n".join([f"{q}: {a}" for q, a in branch_answers.items()])

    prompt = f"""
    Combine the following into one clear answer.

    Main Question:
    {main_query}

    Partial Answers:
    {combined}

    Final Answer:
    """
    response = client.models.generate_content(
    model="gemini-2.5-flash",   
    contents=prompt)
    return response.text



def branched_rag(query):
    sub_queries = decompose_query(query)
    branch_answers = {}

    for q in sub_queries:
        contexts = retrieve_context(q)
        answer = answer_branch(q, contexts)
        branch_answers[q] = answer

    final_answer = combine_answers(query, branch_answers)
    return final_answer


if __name__ == "__main__":
    query = "Explain blockchain with advantages and disadvantages"
    result = branched_rag(query)

    print("\nFinal Answer:\n")
    print(result)
