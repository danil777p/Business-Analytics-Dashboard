def get_ai_insights(prompt):
    import ollama
    response = ollama.chat(
        model = 'phi3',
        messages=[{"role": "user", "content": prompt}]
    )
    return response['message']['content']
