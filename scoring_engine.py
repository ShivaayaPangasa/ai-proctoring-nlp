def calculate_preparedness_score(
    perplexity,
    vocabulary_richness,
    sentence_consistency,
    repetition_score,
    formality_score
):

    score = 0

    # ==========================
    # PERPLEXITY
    # ==========================

    if perplexity < 30:
        score += 30

    elif perplexity < 60:
        score += 20

    else:
        score += 10

    # ==========================
    # VOCABULARY RICHNESS
    # ==========================

    score += vocabulary_richness * 20

    # ==========================
    # SENTENCE CONSISTENCY
    # ==========================

    if sentence_consistency < 2:
        score += 15

    elif sentence_consistency < 5:
        score += 10

    else:
        score += 5

    # ==========================
    # REPETITION
    # ==========================

    score += repetition_score * 20

    # ==========================
    # FORMALITY
    # ==========================

    score += formality_score * 15

    # ==========================
    # LIMIT SCORE
    # ==========================

    score = min(score, 100)

    # ==========================
    # RESPONSE LABEL
    # ==========================

    if score < 35:

        label = "Natural Response"

    elif score < 65:

        label = "Prepared Response"

    else:

        label = "Highly Structured Response"

    # ==========================
    # OBSERVED TRAITS
    # ==========================

    traits = []

    if vocabulary_richness > 0.80:
        traits.append("Rich Vocabulary")

    if sentence_consistency < 2:
        traits.append("Low Sentence Variation")

    if repetition_score > 0.20:
        traits.append("Repetitive Language")

    if formality_score > 0.10:
        traits.append("Formal Language")

    if perplexity < 40:
        traits.append("Highly Predictable Text")

    # ==========================
    # CONFIDENCE
    # ==========================

    confidence = min(
        abs(score - 50) * 2,
        100
    )

    # ==========================
    # RETURN
    # ==========================

    return {

        "preparedness_score": round(
            score,
            2
        ),

        "response_type": label,

        "confidence": round(
            confidence,
            2
        ),

        "observed_traits": traits
    }