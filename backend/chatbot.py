from groq import Groq
from json import load, dump
import datetime
from dotenv import dotenv_values

env_vars = dotenv_values(".env")
Username = env_vars.get("Username")
Assistantname = env_vars.get("Assistantname")
GroqAPIKey = env_vars.get("GroqAPIKey")

client = Groq(api_key='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')
messages = []

System = f"""Hello, I am {Username}, You are a very accurate and advanced AI chatbot named {Assistantname} which also has real-time up-to-date information from the internet.
*** Do not tell time until I ask, do not talk too much, just answer the question.***
*** Reply in only English, even if the question is in Hindi, reply in English.***
*** Do not provide notes in the output, just answer the question and never mention your training data. ***
"""

SystemChatbot = [{"role": "system", "content": System}]

try:
    with open(r"Data\chatLog.json", "r") as f:
        messages = load(f)
except FileNotFoundError:
    with open(r"Data\chatLog.json", "w") as f:
        dump([], f)

def RealtimeInformation():
    now = datetime.datetime.now()
    Day = now.strftime("%A")
    Date = now.strftime("%D")
    Month = now.strftime("%B")
    Year = now.strftime("%Y")
    Hour = now.strftime("%H")
    Minute = now.strftime("%M")
    Second = now.strftime("%S")
    
    data = f"Please use this as real-time information if needed,\n"
    data += f"Day: {Day}\n Date: {Date}\n Month: {Month}\n Year: {Year}\n"
    data += f"Time: {Hour}\n Hours: {Minute}\n Minutes: {Second}\n Seconds.\n"
    return data

def AnswerModifier(Answer):
    return '\n'.join([line for line in Answer.split('\n') if line.strip()])

def Chatbot(Query):
    try:
        with open(r"Data\chatLog.json", "r") as f:
            messages = load(f)

        messages.append({"role": "user", "content": Query})

        completion = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=SystemChatbot + [{"role": "system", "content": RealtimeInformation()}] + messages,
            max_tokens=1024,
            temperature=0.7,
            top_p=1,
            stream=True,
            stop=None
        )

        Answer = ""
        for chunk in completion:
            if chunk.choices[0].delta.content:
                Answer += chunk.choices[0].delta.content

        Answer = Answer.replace("</s>", "")
        messages.append({"role": "assistant", "content": Answer})

        with open(r"Data\chatLog.json", "w") as f:
            dump(messages, f, indent=4)

        return AnswerModifier(Answer)

    except Exception as e:
        print(f"Error: {e}")
        with open(r"Data\chatLog.json", "w") as f:
            dump([], f, indent=4)
        return Chatbot(Query)

if __name__ == "__main__":
    while True:
        user_input = input("Enter Your Question: ")
        print(Chatbot(user_input))
