
import openai as OpenAI

# with the following code in client.py:

client = OpenAI(api_key="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")

completion = client.chat.completions.create(
model="gpt-3.5-turbo",
    temperature=0.7,
    max_tokens=100,
    n=1,
    messages=[
        {
            "role": "user",
            "content": "What is the history behind the development of the internet and its impact on society?"
        }
    ]
)

print(completion.choices[0].message.content)


