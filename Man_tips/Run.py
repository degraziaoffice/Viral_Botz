from brain import make_post

TOPICS = [
    "fix anything", "build a fire", "grill etiquette", "tool organization",
    "car troubleshooting", "apology strategy", "laundry sorting", "budgeting basics",
    "first apartment setup", "meeting nerves"
]

def approval_loop():
    idx = 0
    while True:
        topic = TOPICS[idx % len(TOPICS)]
        prompt = f"Write a funny 140 char 'man tip' about {topic}; exaggerated, helpful-ish; light-hearted."
        tags = ["#ManTips","#AI","#Humor"]
        idea = make_post(prompt, tags)
        print("\nRobot suggests:\n", idea)
        ok = input("Post this? (y/n/q): ").strip().lower()
        if ok == "y":
            print("\n✅ Copy this into your ManTips account:\n", idea)
            break
        elif ok == "q":
            print("Bye!")
            break
        else:
            idx += 1

if __name__ == "__main__":
    approval_loop()
