import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from constants import system_prompt
load_dotenv()
key = os.getenv("GEMINI_API_KEY")



client = genai.Client(
        api_key=key,
    )



def customer_support (data,history):
        print(history,data)
        user_input = data
        if user_input == "exit":
            print("Hitesh Dada: Asha krta hu ki humari sewa apko achi lagi!")
        history.append(types.Content(role="user",parts=[types.Part.from_text(text=user_input)]))
        model = "gemini-2.0-flash"
        generate_content_config = types.GenerateContentConfig(
            response_mime_type="text/plain",
            system_instruction=[
                types.Part.from_text(text=system_prompt),
            ],
        )

        response = client.models.generate_content(
            model=model,
            contents=history,
            config=generate_content_config,)
        
        history.append(types.Content(role="model", parts=[types.Part.from_text(text=response.text)]))
        print(f"Hitesh Dada: {response.text}")
        return response.text

