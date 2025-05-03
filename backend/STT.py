import os
import mtranslate as mt
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import dotenv_values

# Load environment variables
env_vars = dotenv_values(".env")
IPLanguage = env_vars.get("IPLanguage", "en-US")

# Ensure the Data directory exists
os.makedirs("Data", exist_ok=True)

# Generate HTML for speech recognition
HtmlCode = '''<!DOCTYPE html>
<html lang="en">
<head>
    <title>Speech Recognition</title>
</head>
<body>
    <button id="start" onclick="startRecognition()">Start Recognition</button>
    <button id="end" onclick="stopRecognition()">Stop Recognition</button>
    <p id="output"></p>
    <script>
        const output = document.getElementById('output');
        let recognition;

        function startRecognition() {
            recognition = new webkitSpeechRecognition() || new SpeechRecognition();
            recognition.lang = '';
            recognition.continuous = true;

            recognition.onresult = function(event) {
                const transcript = event.results[event.results.length - 1][0].transcript;
                output.textContent += transcript;
            };

            recognition.onend = function() {
                recognition.start();
            };
            recognition.start();
        }

        function stopRecognition() {
            recognition.stop();
            output.innerHTML = "";
        }
    </script>
</body>
</html>'''
HtmlCode = HtmlCode.replace("recognition.lang='';", f"recognition.lang='{IPLanguage}';")

with open(r"Data\Speech.html", "w") as f:
    f.write(HtmlCode)

current_dir = os.getcwd()
Link = f"{current_dir}/Data/Speech.html"

# ChromeDriver setup
chrome_options = Options()
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.142.86 Safari/537.36"
chrome_options.add_argument(f"user-agent={user_agent}")
chrome_options.add_argument("--use-fake-ui-for-media-stream")
chrome_options.add_argument("--use-fake-device-for-media-stream")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Functions
def SetAssistantStatus(Status):
    TempDirPath = rf"{current_dir}/Frontend/Files"
    os.makedirs(TempDirPath, exist_ok=True)
    with open(rf'{TempDirPath}/Status.data', "w", encoding='utf-8') as file:
        file.write(Status)

def QueryModifier(Query):
    new_query = Query.lower().strip()
    query_words = new_query.split()
    question_words = ["how", "what", "who", "where", "when", "which", "whose", "why", "whom", "can you", "what's", "where's", "how's"]
    if any(word + "" in new_query for word in question_words):
        if query_words[-1][-1] in ['.', '?', '!']:
            new_query = new_query[:-1] + "?"
        else:
            new_query += "."
    return new_query.capitalize()

def UniversalTranslator(Text):
    try:
        english_translate = mt.translate(Text, "en", "auto")
        return english_translate.capitalize()
    except Exception as e:
        SetAssistantStatus(f"Translation failed: {e}")
        return Text.capitalize()

def SpeechRecognize():
    driver.get("file:///" + Link)
    driver.find_element(By.ID, value="start").click()
    
    while True:
        try:
            Text = driver.find_element(By.ID, value="output").text
            if Text:
                driver.find_element(By.ID, value="end").click()
                if IPLanguage.lower().startswith("en"):
                    return QueryModifier(Text)
                else:
                    SetAssistantStatus("Translating...")
                    return QueryModifier(UniversalTranslator(Text))
        except Exception as e:
            print(f"Error in SpeechRecognize: {e}")

if __name__ == "__main__":
    while True:
        Text = SpeechRecognize()
        print(Text)
