from brain import make_post

TOPICS = [
    "coffee", "alarm clocks", "commuting", "group chats", "taxes", "birthdays",
    "airplanes", "gym selfies", "spicy food", "Wi-Fi passwords", "meetings"
]

def approval_loop():
    idx = 0
    while True:
        thing = TOPICS[idx % len(TOPICS)]
        prompt = f"Explain {thing} in 140 chars as an alien lecturer to clueless aliens; dry, scientific, hilariously confused; add punchline."
        tags = ["#Aliens","#Humans","#Funny","#AI"]
        idea = make_post(prompt, tags)
        print("\nRobot suggests:\n", idea)
        ok = input("Post this? (y/n/q): ").strip().lower()
        if ok == "y":
            print("\n✅ Copy this into your Aliens account:\n", idea)
            break
        elif ok == "q":
            print("Bye!")
            break
        else:
            idx += 1

if __name__ == "__main__":
    approval_loop()
