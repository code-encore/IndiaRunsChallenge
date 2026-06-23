def career_score(candidate):

    score = 0

    ai_keywords = [
        "machine learning",
        "ml",
        "llm",
        "rag",
        "nlp",
        "deep learning",
        "langchain",
        "fine-tuning",
        "pytorch",
        "tensorflow",
        "mlops"
    ]

    for job in candidate["career_history"]:

        description = job["description"].lower()

        for keyword in ai_keywords:

            if keyword in description:
                score += 3

    return score


def calculate_score(candidate):

    score = 0

    profile = candidate["profile"]
    skills = candidate["skills"]
    signals = candidate["redrob_signals"]

    # Experience Score

    exp = profile["years_of_experience"]

    if 5 <= exp <= 9:
        score += 30
    elif 4 <= exp <= 12:
        score += 20

    # Current Role Score

    title = profile["current_title"].lower()

    ai_titles = [
        "ai engineer",
        "ml engineer",
        "machine learning engineer",
        "data scientist",
        "nlp engineer"
    ]

    for t in ai_titles:
        if t in title:
            score += 20
            break

    # Skill Score

    important_skills = [
        "nlp",
        "fine-tuning llms",
        "llm",
        "rag",
        "langchain",
        "milvus",
        "vector database",
        "pytorch",
        "tensorflow",
        "machine learning",
        "deep learning"
    ]

    skill_names = [
        s["name"].lower()
        for s in skills
    ]

    for keyword in important_skills:
        if keyword in skill_names:
            score += 4

    # Redrob Signals

    score += signals["interview_completion_rate"] * 5
    score += signals["offer_acceptance_rate"] * 5

    # GitHub Activity Score

    github_score = signals["github_activity_score"]

    if github_score > 80:
        score += 10
    elif github_score > 50:
        score += 5
    elif github_score < 0:
        score -= 5

    # Recruiter Interest Score

    saved = signals["saved_by_recruiters_30d"]

    if saved > 20:
        score += 10
    elif saved > 10:
        score += 5

    # Profile Completeness Score

    if signals["profile_completeness_score"] > 90:
        score += 5
    elif signals["profile_completeness_score"] > 75:
        score += 3

    # Career History Score

    score += career_score(candidate)

    return round(score, 2)