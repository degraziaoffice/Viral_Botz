from brain import make_post

ANGLES = [
    "celebrity privacy vs oversharing",
    "brand eco claims vs plastic packaging",
    "politician unity talk vs partisan tweets",
    "influencer hustle vs nap posts",
    "tech minimalist ads vs feature overload",
    "diet culture vs dessert reels"
]

def approval_loop():
    idx = 0
    while True:
        angle = ANGLES[idx % len(ANGLES)]
        prompt = f"Make a funny 140 char post about hypocrisy: {angle}. Keep it light satire; no names; witty contrast."
        tags = ["#Satire","#Irony","#AI"]
        idea = make_post(prompt, tags)
        print("\nRobot suggests:\n", idea)
        ok = input("Post this? (y/n/q): ").strip().lower()
        if ok == "y":
            print("\n✅ Copy this into your HypocrisyWatch account:\n", idea)
            break
        elif ok == "q":
            print("Bye!")
            break
        else:
            idx += 1

if __name__ == "__main__":
    approval_loop()
