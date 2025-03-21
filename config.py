from dotenv import load_dotenv
import os 



MODEL = "gpt-4o-mini"

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

if not OPENAI_API_KEY:
    print("No API Key was foound")
elif not OPENAI_API_KEY.startswith('sk-proj-'):
    print("API Key has been found but it is not Correct")
else:
    print('API Key looks good')
