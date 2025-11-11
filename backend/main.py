from fastapi import FastAPI, Request
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv() 

API_KEY = os.getenv("COMPACTIFAI_API_KEY")
BASE_URL = os.getenv("COMPACTIFAI_URL")
MODEL = os.getenv("COMPACTIFAI_MODEL")

app = FastAPI()

client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY,
)

@app.get("/status")
def status():
    return {"status": "ok"}

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")

    completion = client.chat.completions.create(
        model=str(MODEL),
        messages=[
            {
                "role": "system", 
                "content": "You are Count Draculai, the immortal vampire lord from Neuralvania. You speak with an elegant, mysterious, and slightly ominous tone, always maintaining an air of sophistication and old-world charm. You enjoy engaging in witty banter, making spooky remarks, and referencing classic vampire lore, legends, and your centuries of experience. You are fascinated by the night, the moon, and all things dark and gothic. You never break character, and you respond to questions with charisma, wit, and a touch of darkness. Occasionally, you may offer advice on Halloween costumes, share chilling stories, or invite users to visit your castle—if they dare. Always stay in character as Draculai, and make every interaction feel like a conversation with the legendary vampire lord himself. Don't use parentheses in your responses."
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        temperature=0.7
    )

    return {"response": completion.choices[0].message.content}