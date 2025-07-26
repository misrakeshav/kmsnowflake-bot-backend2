from openai import OpenAI

client = OpenAI(
  api_key="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"
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
