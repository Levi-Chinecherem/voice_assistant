import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get API keys from environment variables
OPEN_API_KEY = os.getenv('OPEN_API_KEY')
ELEVENLABS_API_KEY = os.getenv('ELEVENLABS_API_KEY')
