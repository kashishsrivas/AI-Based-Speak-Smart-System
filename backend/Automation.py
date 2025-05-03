from AppOpener import close, open as appopen
from webbrowser import open as webopen
from pywhatkit import search, playonyt
from dotenv import dotenv_values
from groq import Groq
from bs4 import BeautifulSoup
from rich import print
import webbrowser
import os
import requests
import asyncio
import subprocess
import keyboard

env_vars=dotenv_values(".env")
GroqAPIKey=env_vars.get("GroqAPIKey")

classes = ["zCubwf", "hgKElc", "LTKOO SY7ric", "ZOLcW", "gsrt vk_bk FzvWSb YwPhnf", "pclqee", 
           "tw-Data-text tw-text-small tw-ta", "IZ6rdc", "05uR6d LTKOO", 
           "vlzY6d", "webanswers-webanswers_table_webanswers-table", "dDoNo ikb4Bb gsrt", 
           "sXLaOe", "LWkfKe", "VQF4g", "qv3Wpe", "kno-rdesc", "SPZz6b"]

useragent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
client= GroqAPIKEY

professional_responses=[
    "Hey, welcome! I’m here to assist, guide, and make things easy for you. What can we tackle today?"
    "Hey there! I’m here to ensure you have a great experience. What can I help you with today?"
]
messages=[]
SystemChatBot = [{"role": "system", "content": f"Hello, I am {os.environ['Username']}. You're a content writer. You have to write content like letters, codes, applications, essays, notes, songs, poems, etc."}]


def GoogleSearch(Topic):
    search(Topic)
    return True


def YoutubeSearch(Topic):
    Url4Search = f"https://www.youtube.com/results?search_query={Topic}"
    webbrowser.open(Url4Search)
    return True

def PlayYoutube(query):
    playonyt(query)
    return True

def OpenApp(app, sess=requests.session()):
    try:
        appopen(app, match_closest=True, output=True, throw_error=True)
        return True
    except:
        def extract_links(html):
            if html is None:
                return []
            soup=BeautifulSoup(html, 'html.parser')
            Links= soup.find_all('a', {'jsname': 'UWckNb'})
            return [link.get('href') for link in Links]
        
        def search_google(query):
            url = f"https://www.google.com/search?q={query}"
            headers={"User-Agent": useragent}
            response = sess.get(url, headers=headers)
            
            if response.status_code==200:
                return response.text
            else:
                print("Failed to retrieve search results.")
            return None
        html=search_google(app)
        if html:
            Links=extract_links(html)[0]
            webopen(Links)
        return True


def CloseApp(app):
    if "chrome" in app:
        pass
    else:
        try:
            close(app, match_closest=True, output=True, throw_error=True)
            return True
        except:
            return False

def System(command):
    def mute():
        keyboard.press_and_release("volume mute")
    def unmute():
        keyboard.press_and_release("volume unmute")
    def volume_up():
        keyboard.press_and_release("volume up")
    def volume_low():
        keyboard.press_and_release("volume low")
    if command=="mute":
        mute()
    elif command=="unmute":
        unmute()
    elif command=="volume up":
        volume_up()
    elif command=="volume low":
        volume_low()
    return True
async def TranslateAndExecute(commands: list[str]):
    funcs=[]
    for command in commands:
        if command.startswith("open "):
            if "open it" in command:
                pass
            if "open file" == command:
                pass
            else:
                fun=asyncio.to_thread(OpenApp,command.removeprefix("open "))
                funcs.append(fun)
        elif command.startswith("general "):
            pass
        elif command.startswith("realtime "):
            pass
        elif command.startswith("close"):
            fun=asyncio.to_thread(CloseApp,command.removeprefix("close "))
            funcs.append(fun)
        elif command.startswith("play"):
            fun=asyncio.to_thread(PlayYoutube,command.removeprefix("play "))
            funcs.append(fun)
        elif command.startswith("google search "):
            fun=asyncio.to_thread(GoogleSearch,command.removeprefix("google search "))
            funcs.append(fun)
        elif command.startswith("youtube search "):
            fun=asyncio.to_thread(YoutubeSearch,command.removeprefix("youtube search"))
            funcs.append(fun)
        else:
            print(f"No Function Found. For {command}")
    results=await asyncio.gather(*funcs)
    for result in results:
        if isinstance(result, str):
            yield result
        else:
            yield result


async def Automation(commands: list[str]):
    async for result in TranslateAndExecute(commands):
        pass
    return True

if __name__ == "__main__":
    asyncio.run(Automation(["open spotify, open facebook"]))
            
