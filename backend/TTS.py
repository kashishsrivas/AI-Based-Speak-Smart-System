import pygame
import random
import os
import asyncio
import edge_tts
from dotenv import dotenv_values

# Load environment variables
env_vars = dotenv_values(".env")
AssistantVoice = env_vars.get("AssistantVoice")  # Fixed typo in variable name

async def TextToSpeechAsync(text) -> None:
    file_path = os.path.join("Data", "speech.mp3")
    if os.path.exists(file_path):
        os.remove(file_path)
    communicate = edge_tts.Communicate(text, AssistantVoice, pitch='-10Hz', rate='+1%')
    await communicate.save(file_path)

def TTS(text, func=lambda r=None: True):
    try:
        asyncio.run(TextToSpeechAsync(text))
        if not pygame.mixer.get_init():  # Check if mixer is initialized
            pygame.mixer.init()
        audio_path = os.path.join("Data", "speech.mp3")
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            if func() == False:
                break
            pygame.time.Clock().tick(10)
        return True
    except Exception as e:
        print(f"Error in TTS: {e}")
    finally:
        try:
            if pygame.mixer.get_init():  # Ensure cleanup only if initialized
                func(False)
                pygame.mixer.music.stop()
                pygame.mixer.quit()
        except Exception as e:
            print(f"Error during cleanup: {e}")

def HandleLongTextToSpeech(text, func=lambda r=None: True):
    sentences = str(text).split(".")
    responses = [
        "The rest of the result has been printed to the chat screen, kindly check it out sir.",
        "The rest of the text is now on the chat screen, sir, please check it.",
        "You can see the rest of the text on the chat screen, sir.",
        "The remaining part of the text is now on the chat screen, sir.",
        "Sir, you'll find more text on the chat screen for you to see.",
        "The rest of the answer is now on the chat screen, sir.",
        "Sir, please look at the chat screen, the rest of the answer is there.",
        "You'll find the complete answer on the chat screen, sir.",
        "The next part of the text is on the chat screen, sir.",
        "Sir, please check the chat screen for more information.",
    ]
    
    if len(sentences) > 4 and len(text) >= 250:
        short_text = ".".join(sentences[:2]) + "." + random.choice(responses)
        TTS(short_text, func)
    else:
        TTS(text, func)

if __name__ == "__main__":
    while True:
        user_query = input("Enter the Query: ")
        HandleLongTextToSpeech(user_query)
