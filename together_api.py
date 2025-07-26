import together

def ask_together_ai(system_context, prompt):
    together.api_key = "b1456006455f15d69893fbfd43aa9fd5b88f65a9bbbe4239a0539baba3c631ab"  # Make sure you load this securely from a file in production

    response = together.Complete.create(
        prompt=f"{system_context}\nUser: {prompt}\nAI:",
        model="mistralai/Mixtral-8x7B-Instruct-v0.1",
        max_tokens=300,
        temperature=0.7,
        stop=["User:", "AI:"]
    )

    return response['choices'][0]['text'].strip()
