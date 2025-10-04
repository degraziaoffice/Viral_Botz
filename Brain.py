from transformers import pipeline

# This loads a free, small text generator for short funny lines.
funny_bot = pipeline("text-generation", model="gpt2")

def make_post(prompt, hashtags=None):
    """
    - Takes a prompt (what you want the robot to write)
    - Adds hashtags (list of tags like ["#AI", "#Funny"])
    - Returns a final string <= 140 characters including hashtags
    """
    if hashtags is None:
        hashtags = []
    # Generate a short text
    out = funny_bot(prompt, max_length=60, do_sample=True, temperature=0.9)[0]['generated_text']
    # Make sure the total stays within 140 chars
    tag_str = (" " + " ".join(hashtags)) if hashtags else ""
    base = out.strip()
    # Trim to fit
    max_len = 140
    if len(base) + len(tag_str) > max_len:
        base = base[:max_len - len(tag_str)].rstrip()
    return (base + tag_str).strip()
