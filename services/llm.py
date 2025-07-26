import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def ask_llm(prompt: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful assistant working inside a company environment. "
                    "Only answer based on the user's Snowflake account data and onboarding documentation. "
                    "If you don't have enough information, ask a follow-up or say you don't know. "
                    "Never make up facts or provide guesses unrelated to the Snowflake setup or onboarding processes."
                )
            },
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()
