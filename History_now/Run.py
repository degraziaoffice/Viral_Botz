from brain import make_post

EVENTS = [
    "signing of the Declaration of Independence",
    "moon landing",
    "first Olympic Games",
    "printing press debut",
    "Great Pyramid construction",
    "Renaissance art workshop",
    "Magna Carta signing",
    "Apollo 13 crisis",
    "Berlin Wall fall",
    "first telephone call"
]

MODERN = [
    "Zoom call with lag", "group chat drama", "influencer collab",
    "two-factor auth fail", "food delivery delay", "ride-share surge pricing",
    "autocorrect panic", "unboxing video", "crypto airdrop", "terms & conditions pop-up"
]

def approval_loop():
    idx = 0
    while True:
        event = EVENTS[idx % len(EVENTS)]
        twist = MODERN[idx % len(MODERN)]
        prompt = f"Describe {event} as if it happened today with {twist}. 140 chars; sharp satire; modern lingo."
        tags = ["#History","#Satire","#AI","#WhatIf","#ModernDay"]
        idea = make_post(prompt, tags)
        print("\nRobot suggests:\n", idea)
        ok = input("Post this? (y/n/q): ").strip().lower()
        if ok == "y":
            print("\n✅ Copy this into your HistoryNow account:\n", idea)
            break
        elif ok == "q":
            print("Bye!")
            break
        else:
            idx += 1

if __name__ == "__main__":
    approval_loop()
