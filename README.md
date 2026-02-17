**🎙️ Whisper-GPT Voice Assistant**
An intelligent, voice-controlled personal assistant that uses OpenAI's GPT-3.5 for logic, OpenAI's Whisper for high-accuracy speech-to-text, and Pyttsx3 for offline text-to-speech.

**✨ Features**
Accurate STT: Uses local Whisper models for superior transcription compared to standard Google Speech APIs.
AI Brain: Powered by GPT-3.5-Turbo to answer complex questions and define words.
System Control: Open popular websites (YouTube, Google, etc.) via voice.
Real-time Weather: Fetches live weather data using the OpenWeatherMap API.
Utility Tools: Tells the current date and time.
Multi-threaded: Opens browser windows in the background to prevent the assistant from freezing.

**🛠️ Prerequisites**
Before running the assistant, ensure you have the following installed:
Python 3.8+
FFmpeg: Required by Whisper for audio processing.
Windows: choco install ffmpeg
Mac: brew install ffmpeg
Linux: sudo apt install ffmpeg
PortAudio: Required for the PyAudio library
Windows: Included with pip wheels.
Mac: brew install portaudio

🚀 Installation
1)Clone the repository:git clone https://github.com/yourusername/whisper-gpt-assistant.git
cd whisper-gpt-assistant
2)Install Python dependencies:pip install openai whisper pyttsx3 requests speechrecognition pyaudio

**Set up API Keys:**
Open the Python file and replace the placeholders with your actual keys:

OPENAI_API_KEY: Get it from OpenAI Dashboard.
OPENWEATHER_API_KEY: Get it from OpenWeatherMap.

**🖥️ Usage**
Simply run the script:
python assistant.py

Voice Commands to Try:
Category,What to say
Knowledge,"""What is the capital of France?"""
Weather,"""What is the weather?"" (Assistant will ask for the city)"
Web,"""Open YouTube"" or ""Open Google"""
Definitions,"""Define the word Photosynthesis"""
Time/Date,"""What is the time?"" or ""What is the date today?"""
Exit,"""Stop"", ""Exit"", or ""Thank you"""

**⚙️ Configuration**

You can modify the following parameters in the script to suit your hardware:
Whisper Model: Changed whisper.load_model("base") to "tiny" if you have an older CPU, or "medium"/"large" if you have a powerful GPU.
Speech Rate: Adjust engine.setProperty('rate', 180) to make the assistant talk faster or slower.
Energy Threshold: Adjust r.energy_threshold if the assistant is too sensitive (or not sensitive enough) to background noise.

**🤝 Contributing**
Feel free to fork this project, open issues, or submit pull requests. Future goals include adding a "Wake Word" (e.g., "Hey Jarvis") and local LLM support.

**📄 License**
This project is licensed under the MIT License.
