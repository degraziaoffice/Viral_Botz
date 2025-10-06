# Brain.py
# Purpose: Create punchy ≤140-character lines with hashtags, using upgraded prompts and safe trimming.

from typing import List

def compose(text: str, hashtags: List[str] | None = None, max_len: int = 140) -> str:
    """
    Compose a final line with hashtags, strictly ≤ max_len characters.
    This intentionally does NOT depend on heavy LLMs (works anywhere).
    """
    tags = []
    if hashtags:
        for t in hashtags:
            t = t.strip()
            if not t.startswith("#"):
                t = "#" + t
            tags.append(t.replace(" ", ""))

    tag_str = (" " + " ".join(tags)) if tags else ""
    base = text.strip()

    # Clean punctuation at ends
    if base.endswith((";", ",", ":", "—", "-")):
        base = base[:-1].strip()

    # Trim to fit
    if len(base) + len(tag_str) > max_len:
        base = base[:max_len - len(tag_str)].rstrip()

    final = (base + tag_str).strip()
    return final[:max_len]
