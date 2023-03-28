import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Me dê 3 ideias de aplicativos que eu posso criar com as api´s da openai"}])
print(completion.choices[0].message.content)