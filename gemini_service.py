import os
from dotenv import load_dotenv
from google import genai

from prompts import SYSTEM_PROMPT
from logger import logger

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def get_response(chat_history):

    try:

        conversation = SYSTEM_PROMPT + "\n\n"

        for message in chat_history:

            role = message["role"]
            content = message["content"]

            conversation += f"{role}: {content}\n"

        logger.info("Sending request to Gemini")

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=conversation
        )

        logger.info("Response received successfully")

        return response.text

    except Exception as e:

        logger.error(f"Gemini Error: {e}")

        return f"Error: {e}"