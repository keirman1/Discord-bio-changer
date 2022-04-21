import requests , random, json, threading
from time import sleep


#https://discord.com/api/v9/channels/937848410713759774/messages
#https://discord.com/api/v9/channels/911323952041820204/messages?limit=50
 


messages = [
    "Hello",
    "<= Thats cool",
    "This is all rng",
    "Go to my github",
    "God I love trampolining",
    "keirman1.github.com",
    "What are these bios",
    "I have one of those things to my left",
    "Am I a virgin?",
    'If you see this dm me "Dog fucking suck"',
    "School is useless",
    "Learn coding today!",
    "Got the drip",
    "What a loser",
    "+rep Is me and can code",
    "I play csgo (isnt russain)",
    "7m people from russia play csgo",
    "I like writing these",
    'Im a "hacker"',
    "Bigrat.monster",
    "lil naan x",
    "I dislike men",
    "Why do we exist",
    "Caught in 4k UHD",
    "Its not fun rewriting these every few seconds",
    "Say hello to me once in a while",
    "Some people hate me some people love me",
    "lua? learn a real language",
    "Some people say deez I do deez",
    "Discord ToS is strange",
    "Gimme nitro"

]

emojis = [
    "🦐",
    "👀",
    "🖥️",
    "💻",
    "💽",
    "🖱️",
    "⌨️",
    "💾",
    "🦾",
    "🤔",
    "🥶",
    "😏",
    "🤓",
    "🐀",
    "🐁",
    "🦦",
    "🎮",
    "🛫",
    "⛩",
    "🏯",
    "🎸"
]



def bio(message, emoji):


    header ={
        'authorization': 'your token'
    }
    payload = {
        'custom_status': {'text': message, 'emoji_name': emoji}
    }
    r = requests.patch('https://discord.com/api/v9/users/@me/settings', headers=header, json=payload)
    print("changed bio to: " + emoji + " " + message + ", With the code:"+ str(r.status_code))


 
    


def main():
    bio(messages[random.randrange(0, len(messages))], emojis[random.randrange(0, len(emojis))])
    

    

while True:
    main()
    sleep(random.randrange(7, 20))
    