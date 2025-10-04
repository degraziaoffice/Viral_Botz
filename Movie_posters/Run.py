from brain import make_post

PROMPTS = [
    ("Write a funny 140 character plot for Titanic using reviews; door too small; add playful sarcasm.",
     ["#Movies","#AI","#Poster","#Titanic"]),
    ("Write a funny 140 character plot for Inception using reviews; dreams within dreams; confused but impressed.",
     ["#Movies","#AI","#Poster","#Inception"]),
    ("Write a funny 140 character plot for Interstellar using reviews; space dad; love vs physics.",
     ["#Movies","#AI","#Poster","#Interstellar"]),
    ("Write a funny 140 character plot for The Godfather using reviews; family business; oranges.",
     ["#Movies","#AI","#Poster","#TheGodfather"]),
    ("Write a funny 140 character plot for Mean Girls using reviews; burn book drama; fetch failed.",
     ["#Movies","#AI","#Poster","#MeanGirls"]),
]

def approval_loop():
    idx = 0
    while True:
        prompt, tags = PROMPTS[idx % len(PROMPTS)]
        idea = make_post(prompt, tags)
        print("\nRobot suggests:\n", idea)
        ok = input("Post this? (y = yes, n = try again, q = quit): ").strip().lower()
        if ok == "y":
            print("\n✅ Copy this into your Movie account:\n", idea)
            break
        elif ok == "q":
            print("Bye!")
            break
        else:
            idx += 1

if __name__ == "__main__":
    approval_loop()
