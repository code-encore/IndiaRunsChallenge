import json

with open("data/candidates.jsonl","r",encoding="utf-8") as f:
    candidate = json.loads(next(f))

for job in candidate["career_history"]:
    print("\nJOB TITLE:", job["title"])
    print("DESCRIPTION:")
    print(job["description"])