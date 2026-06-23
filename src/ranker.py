import json
from scoring import calculate_score

candidates = []

with open("data/candidates.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        candidates.append(json.loads(line))

for candidate in candidates:
    candidate["score"] = calculate_score(candidate)

candidates.sort(
    key=lambda x: x["score"],
    reverse=True
)
top100 = candidates[:100]

top_candidate = candidates[0]

print("Top 10 Candidates")

for c in candidates[:10]:
    print(
        c["candidate_id"],
        c["profile"]["current_title"],
        c["score"]
    )

    import pandas as pd

rows = []

for rank, candidate in enumerate(top100, start=1):

    rows.append({
        "candidate_id": candidate["candidate_id"],
        "rank": rank,
        "score": candidate["score"],
        "reasoning": f"Ranked based on experience, AI skills, career history, and recruiter signals."
    })

df = pd.DataFrame(rows)

df.to_csv(
    "output/submission.csv",
    index=False
)

top_candidate = candidates[0]

print("\nPROFILE:")
print(top_candidate["profile"])

print("\nCAREER HISTORY:")
print(top_candidate["career_history"])

print("\nSKILLS:")
print(top_candidate["skills"])

print("\nREDROB SIGNALS:")
print(top_candidate["redrob_signals"])

print("Submission file created!")