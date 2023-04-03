import openai

openai.api_key = "inserir a chave entre as aspas" 

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Me dê 3 ideias de aplicativos que eu posso criar com as api´s da openai"}])
print(completion.choices[0].message.content)
