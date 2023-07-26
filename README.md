# Dami's Visual Assistant

Dami's Visual Assistant is a Python-based intelligent assistant that accepts voice input, converts it to text, sends the text to OpenAI's GPT-3 API for processing, and then converts the AI response back to voice output.
This Python script demonstrates how to use SpeechRecognition for Speech-to-Text and the OpenAI GPT-3 API for Text-to-Speech. It enables you to convert spoken input from your microphone into text using the SpeechRecognition library and then generates a response using the OpenAI GPT-3 API, converting the text response back to speech using gTTS (Google Text-to-Speech).

## Getting Started

### Prerequisites

To run the assistant, you need to have the following installed:

- Python 3.x
- OpenAI Python library (`openai`)
- SpeechRecognition library (`speech_recognition`)
- gTTS (Google Text-to-Speech) library (`gtts`)
- PyAudio library (`pyaudio`)
- `config.py` file containing your OpenAI API key

You can install the required Python libraries using the following command:

```bash
pip install openai speechrecognition gtts pyaudio
```

### Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/your_username/your_repository.git
cd your_repository
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv myenv
source myenv/bin/activate  # On Windows, use: myenv\Scripts\activate
```

3. Install the required Python libraries:

```bash
pip install -r requirements.txt
```

4. Create a file named `config.py` in the same directory as the `assistant.py` file, and paste your OpenAI API key in it:

```python
# config.py
OPEN_API_KEY = "your_openai_api_key_here"
```
Obtain an OpenAI API key:
   - Sign up for an OpenAI account and obtain your API key from https://beta.openai.com/signup/
   - Save the API key in a file named `config.py` in the same directory as the Python script (`assistant.py`) with the following content:
     ```python
     OPEN_API_KEY = "YOUR_OPENAI_API_KEY"

### Usage

1. Run the assistant by executing the following command:

```bash
python assistant.py
```

2. The assistant will start listening for your voice input. Simply speak your question or message.

3. After processing the speech-to-text conversion, the assistant will send the text to the OpenAI GPT-3 API for generating the response.

4. The generated AI response will be converted to voice output and played back to you.

5. The assistant will continue to listen for new input until you say "stop" or "exit," at which point it will terminate.

### Troubleshooting

- If you encounter any issues related to microphone access, make sure your microphone is working correctly and accessible by other applications.

- If you face any errors during speech recognition, check your internet connection and try again.

- If you have trouble with the OpenAI GPT-3 API, verify that your API key is correctly pasted in the `config.py` file.

**Important Note:**
- The OpenAI API key must be kept secure and not shared publicly.
- The GPT-3 API usage may have limitations depending on your account type and usage policies. Be mindful of your usage to avoid exceeding any limitations.

### License

This project is licensed under the MIT License. Feel free to use and modify it according to your needs.

### Acknowledgments

- This project uses OpenAI's GPT-3 API, which is powered by OpenAI.
- Special thanks to the creators of the `speech_recognition`, `gtts`, and `pyaudio` libraries for enabling speech recognition and text-to-speech functionality.



# Using Dami's Visual Assistant as an Executable (EXE)

Dami's Visual Assistant can also be packaged as an executable (EXE) file, allowing you to use the assistant without needing to install Python or any dependencies. This guide will walk you through the steps to create and use the EXE file on Windows.

## Prerequisites

Before proceeding, ensure you have the following:

1. **Python**: If you don't have Python installed, you can download the latest version from the official website: https://www.python.org/downloads/

2. **Git**: If you want to clone the project from GitHub, make sure you have Git installed: https://git-scm.com/downloads

3. **OpenAI API Key**: You'll need an API key from OpenAI to use their GPT-3 API. Get your key from the OpenAI website.

## Installation

1. Clone the GitHub repository (optional):

```bash
git clone https://github.com/your_username/your_repository.git
cd your_repository
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv myenv
source myenv/bin/activate  # On Windows, use: myenv\Scripts\activate
```

3. Install the required Python libraries:

```bash
pip install openai speechrecognition gtts pyaudio
```

4. Create a file named `config.py` in the same directory as the `assistant.py` file, and paste your OpenAI API key in it:

```python
# config.py
OPEN_API_KEY = "your_openai_api_key_here"
```

## Usage

1. Once you have set up the project and installed the dependencies, you can generate the EXE file.

2. Run the following command to generate the EXE file using PyInstaller:

```bash
pyinstaller --onefile assistant.py
```

3. After running the command, you'll find a new `dist` folder in the project directory. Inside the `dist` folder, there will be an executable file named `assistant.exe`.

4. Double-click on `assistant.exe` to launch Dami's Visual Assistant.

## Using the EXE

1. When you run `assistant.exe`, the assistant will start listening for your voice input. Simply speak your question or message.

2. After processing the speech-to-text conversion, the assistant will send the text to the OpenAI GPT-3 API for generating the response.

3. The generated AI response will be converted to voice output and played back to you.

4. The assistant will continue to listen for new input until you say "stop" or "exit," at which point it will terminate.

## Troubleshooting

- If you encounter any issues related to microphone access, make sure your microphone is working correctly and accessible by other applications.

- If you face any errors during speech recognition, check your internet connection and try again.

- If you have trouble with the OpenAI GPT-3 API, verify that your API key is correctly pasted in the `config.py` file.

## Customization and Further Development

This project is fully customizable, and you can extend it to suit your specific needs. Feel free to modify the assistant's behavior, add new features, or integrate it with other services.

## License

This project is licensed under the MIT License. Feel free to use and modify it according to your needs.

## Acknowledgments

- This project uses OpenAI's GPT-3 API, which is powered by OpenAI.
- Special thanks to the creators of the `speech_recognition`, `gtts`, and `pyaudio` libraries for enabling speech recognition and text-to-speech functionality.

Please note that creating an EXE file may vary based on your operating system and development environment. Additionally, always exercise caution while using EXE files from unknown sources, and ensure you download and run them from trusted sources.

If you have any questions or need further assistance, feel free to reach out!
