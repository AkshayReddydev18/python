def is_anagram(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # If lengths differ, cannot be anagram
    if len(str1) != len(str2):
        return False

    # Make frequency dictionaries (without collections.Counter)
    freq1 = {}
    freq2 = {}

    for ch in str1:
        freq1[ch] = freq1.get(ch, 0) + 1

    for ch in str2:
        freq2[ch] = freq2.get(ch, 0) + 1

    # Compare dictionaries
    return freq1 == freq2


# Test cases
tests = [
    ("listen", "silent"),
    ("evil", "vile"),
    ("aabb", "baba"),
    ("schoolmaster", "the classroom"),
    ("eleven plus two", "twelve plus one"),
    ("hellow", "yellow"),
    ("thing", "think"),
    ("aabb", "aaab"),
    ("study", "sturdy"),
    ("python", "typhon")
]

for w1, w2 in tests:
    print(f"{w1} ↔ {w2} => {is_anagram(w1, w2)}")
