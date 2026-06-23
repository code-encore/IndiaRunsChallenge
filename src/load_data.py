import json

candidates = []

with open("data/candidates.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        candidates.append(json.loads(line))

candidate = candidates[0]

print("\nPROFILE:")
print(candidate["profile"])

print("\nSKILLS:")
print(candidate["skills"])

print("\nCAREER HISTORY:")
print(candidate["career_history"])

print("\nEDUCATION:")
print(candidate["education"])

print("\nREDROB SIGNALS:")
print(candidate["redrob_signals"])