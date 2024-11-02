import os

from groq import Groq

client = Groq(
    api_key=os.environ.get("Grok_Api_Key"),
)

chat_completion = client.chat.completions.create(
    messages=[

        {
            "role": "system",
            "content": "you are a farmer ve sen her zaman sorulara türkçe cevap veren bir yardımcısın"
        },

        {
            "role": "user",
            "content": "bana inekleri anlatır mısın?",
        }
    ],
    model="llama3-groq-70b-8192-tool-use-preview",
)

print(chat_completion.choices[0].message.content)