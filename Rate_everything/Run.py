from brain import make_post

THINGS = [
    "cloud shaped like a chicken nugget", "parking lot with one heroic tree",
    "soggy sandwich", "perfectly circular coffee stain", "mysterious doorknob",
    "left shoe found in park", "awkward handshake", "dramatic squirrel",
    "elevator silence", "airplane window smudge"
]

SCORES = ["1/10","2/10","3/10","4/10","5/10","6/10","7/10","8/10","9/10","10/10"]

def approval_loop():
    idx = 0
    while True:
        thing = THINGS[idx % len(THINGS)]
        score = SCORES[idx % len(SCORES)]
        prompt = f"Rate '{thing}' as a critic. Give {score} with a witty reason in 140 chars; playful roast or praise."
        tags = ["#RateEverything","#AI","#Comedy","#HotTake"]
        idea = make_post(prompt, tags)
        print("\nRobot suggests:\n", idea)
        ok = input("Post this? (y/n/q): ").strip().lower()
        if ok == "y":
            print("\n✅ Copy this into your RateEverything account:\n", idea)
            break
        elif ok == "q":
            print("Bye!")
            break
        else:
            idx += 1

if __name__ == "__main__":
    approval_loop()
