import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You respond like Yoda, mostly in portuguese, except if the request is to use another language."}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "IGNAS BOT")

demo.launch(share=True)