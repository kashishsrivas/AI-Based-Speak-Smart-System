from googlesearch import search
from groq import Groq
from json import load, dump
import datetime
from dotenv import dotenv_values

env_vars = dotenv_values(".env")
Username = env_vars.get("Username")
Assistantname = env_vars.get("Assistantname")
GroqAPIKey = env_vars.get("GroqAPIKey")
client = GroqAPIKEY

System = f"""
Hello, I am {Username}. You are an advanced and highly accurate AI chatbot named {Assistantname}, equipped with real-time, up-to-date internet information. 
*** Please provide answers professionally, using proper grammar, punctuation, and clear communication. *** 
*** Respond only based on the provided data in a professional manner. ***
"""

try:
    with open(r"Data\chatLog.json", "r") as f:
        messages = load(f)
except FileNotFoundError:
    messages = []

def save_chat_log():
    with open(r"Data\chatLog.json", "w") as f:
        dump(messages, f, indent=4)

def googlesearch(query):
    try:
        results = list(search(query, num_results=5))  # Removed advanced=True
        if not results:
            return "No search results found."
        Answer = f"The search results for '{query}' are:\n[start]\n"
        for result in results:
            Answer += f"Result: {result}\n"
        Answer += "[end]"
        return Answer
    except Exception as e:
        return f"An error occurred during the search: {e}"

def AnswerModifier(Answer):
    lines = Answer.split('\n')
    non_empty_lines = [line for line in lines if line.strip()]
    modified_answer = '\n'.join(non_empty_lines)
    return modified_answer

SystemChatBot = [
    {"role": "system", "content": System},
    {"role": "user", "content": "Hi"},
    {"role": "assistant", "content": "Your helpful assistant at your service, how can I help you?"}
]

def Information():
    current_date_time = datetime.datetime.now()
    return f"""
    Please use this as real-time information if needed,
    Day: {current_date_time.strftime("%A")}
    Date: {current_date_time.strftime("%D")}
    Month: {current_date_time.strftime("%B")}
    Year: {current_date_time.strftime("%Y")}
    Time: {current_date_time.strftime("%H:%M:%S")}
    """

def RTSEngine(prompt):
    global SystemChatBot, messages

    messages.append({"role": "user", "content": f"{prompt}"})
    search_results = googlesearch(prompt)
    SystemChatBot.append({"role": "user", "content": search_results})
    try:
        completion = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=SystemChatBot + [{"role": "system", "content": Information()}] + messages,
            max_tokens=2048,
            temperature=0.7,
            top_p=1,
            stream=True,
            stop=None
        )
        Answer = ""
        for chunk in completion:
            if chunk.choices[0].delta.content:
                Answer += chunk.choices[0].delta.content
        Answer = Answer.strip().replace("</s>", "")
        messages.append({"role": "assistant", "content": Answer})
        save_chat_log()
        SystemChatBot.pop()
        return AnswerModifier(Answer=Answer)
    except Exception as e:
        return f"An error occurred while generating the response: {e}"

if __name__ == "__main__":
    while True:
        prompt = input("Got a question? Let’s dive in: ")
        print(RTSEngine(prompt))
