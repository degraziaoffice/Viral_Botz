from brain import make_post

CONCEPTS = [
    "solar-powered nightlight", "umbrella with holes", "Bluetooth candle",
    "left-handed spoon", "self-heating ice cream", "transparent toaster wallet",
    "reusable band-aids", "microwave oven mitts", "folding pizza straw", "Wi-Fi paperclip"
]

def approval_loop():
    idx = 0
    while True:
        idea = CONCEPTS[idx % len(CONCEPTS)]
        prompt = f"Pitch a worst invention: {idea}. 140 chars, punchline included; absurdly confident, infomercial tone."
        tags = ["#Inventions","#Comedy","#AI","#BadIdeas","#Meme"]
        text = make_post(prompt, tags)
        print("\nRobot suggests:\n", text)
        ok = input("Post this? (y/n/q): ").strip().lower()
        if ok == "y":
            print("\n✅ Copy this into your WorstInventions account:\n", text)
            break
        elif ok == "q":
            print("Bye!")
            break
        else:
            idx += 1

if __name__ == "__main__":
    approval_loop()
