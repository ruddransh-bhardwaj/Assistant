import openai
import whisper
import torch
from PIL import Image
import clip
from transformers import pipeline

# Load Whisper Model for Speech Recognition
whisper_model = whisper.load_model("base")

# Load CLIP Model for Image Understanding
device = "cuda" if torch.cuda.is_available() else "cpu"
clip_model, preprocess = clip.load("ViT-B/32", device=device)

def transcribe_audio(audio_path):
    """Transcribes speech to text using Whisper."""
    result = whisper_model.transcribe(audio_path)
    return result["text"]

def analyze_image(image_path):
    """Analyzes an image and generates a caption."""
    image = preprocess(Image.open(image_path)).unsqueeze(0).to(device)
    text_inputs = clip.tokenize(["a photo of a person", "a beautiful landscape", "a busy city street"]).to(device)
    with torch.no_grad():
        image_features = clip_model.encode_image(image)
        text_features = clip_model.encode_text(text_inputs)
        similarity = (image_features @ text_features.T).softmax(dim=-1)
    descriptions = ["Person", "Landscape", "City"]
    return descriptions[similarity.argmax()]

def ask_gpt(prompt):
    """Asks GPT-4 a question and returns a response."""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        api_key="your_openai_api_key"
    )
    return response['choices'][0]['message']['content']

def main():
    print("Welcome to the Multimodal AI Assistant!")
    while True:
        mode = input("Enter mode (text/speech/image/exit): ")
        if mode == "text":
            query = input("Ask me anything: ")
            response = ask_gpt(query)
            print("AI:", response)
        elif mode == "speech":
            audio_path = input("Enter path to audio file: ")
            text = transcribe_audio(audio_path)
            response = ask_gpt(text)
            print("AI:", response)
        elif mode == "image":
            image_path = input("Enter path to image file: ")
            description = analyze_image(image_path)
            response = ask_gpt(f"Describe {description} in detail.")
            print("AI:", response)
        elif mode == "exit":
            break
        else:
            print("Invalid mode. Try again.")

if __name__ == "__main__":
    main()
