from brain import make_post

TOPICS = [
    "black holes", "quantum tunneling", "blockchain", "CRISPR",
    "antibiotic resistance", "climate feedback loops", "machine learning overfitting",
    "supply chain bullwhip", "fusion power", "inflation economics"
]

def approval_loop():
    idx = 0
    while True:
        topic = TOPICS[idx % len(TOPICS)]
        prompt = f"Explain {topic} in 140 chars like I'm 5; playful analogy; crystal clear; slightly silly; no jargon."
        tags = ["#ELI5","#Learning","#AI","#Simple"]
        idea = make_post(prompt, tags)
        print("\nRobot suggests:\n", idea)
        ok = input("Post this? (y/n/q): ").strip().lower()
        if ok == "y":
            print("\n✅ Copy this into your ELI5 account:\n", idea)
            break
        elif ok == "q":
            print("Bye!")
            break
        else:
            idx += 1

if __name__ == "__main__":
    approval_loop()
