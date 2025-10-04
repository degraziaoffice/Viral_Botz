from brain import make_post

PROMPTS = [
    "Write a funny 140 character question humans still can't answer; curious and playful.",
    "Write a 140 char mystery humans still wonder; keep it witty and universal.",
    "Write a 140 char question about reality that stays unsolved; add gentle humor."
]

def approval_loop():
    idx = 0
    while True:
        prompt = PROMPTS[idx % len(PROMPTS)]
        tags = ["#Mystery","#Unsolved","#AI"]
        idea = make_post(prompt, tags)
        print("\nRobot suggests:\n", idea)
        ok = input("Post this? (y/n/q): ").strip().lower()
        if ok == "y":
            print("\n✅ Copy this into your UnansweredQuestions account:\n", idea)
            break
        elif ok == "q":
            print("Bye!")
            break
        else:
            idx += 1

if __name__ == "__main__":
    approval_loop()
