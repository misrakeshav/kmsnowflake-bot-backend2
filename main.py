from fastapi import FastAPI
from pydantic import BaseModel
from services.snowflake import user_exists_partial
from services.llm import ask_llm

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str

@app.post("/ask")
async def handle_question(request: QuestionRequest):
    question = request.question

    # If user is asking whether a user exists
    if "does the user" in question.lower() and "exist" in question.lower():
        username = extract_username(question)
        if username:
            print(f"Checking for users like '{username}'...")
            matches = user_exists_partial(username)
            if matches:
                return {
                    "answer": f"✅ Found matching user(s) in Snowflake: {', '.join(matches)}"
                }
            else:
                return {
                    "answer": f"❌ No users found in Snowflake matching '{username}'"
                }
        else:
            return {"answer": "I couldn't extract the username from your question."}

    # Fallback: send question to LLM
    answer = ask_llm(question)
    return {"answer": answer}

def extract_username(question: str):
    """
    Naively extract the username that follows the word 'user'.
    """
    words = question.strip().split()
    for i, word in enumerate(words):
        if word.lower() == "user" and i + 1 < len(words):
            return words[i + 1].strip("?.'\"")
    return None
