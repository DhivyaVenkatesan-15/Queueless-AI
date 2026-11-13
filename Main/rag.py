
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


KNOWLEDGE_BASE = [
    "During peak hours, administrators should open additional service counters to reduce waiting time.",
    "Queue management systems should serve customers in first come first served order.",
    "Customer waiting time can be reduced by improving staff allocation and service efficiency.",
    "Administrators should monitor the number of waiting customers and active counters.",
    "Customers should receive a unique token number for organized queue management.",
    "Estimated waiting time depends on customers ahead, average service duration and available counters.",
    "Digital queue systems reduce physical crowding and improve customer experience.",
    "Service performance should be monitored using average waiting time and completed customer count.",
    "When a queue becomes crowded, staff should prioritize efficient service without skipping queue order.",
    "Historical service records can help predict future service duration and peak-hour demand."
]


vectorizer = TfidfVectorizer(
    stop_words="english",
    ngram_range=(1, 2)
)

knowledge_vectors = vectorizer.fit_transform(KNOWLEDGE_BASE)


def retrieve_information(query, top_k=3):

    query_vector = vectorizer.transform([query])

    similarities = cosine_similarity(
        query_vector,
        knowledge_vectors
    )[0]

    ranked_indices = similarities.argsort()[::-1][:top_k]

    results = []

    for index in ranked_indices:
        if similarities[index] > 0:
            results.append(
                KNOWLEDGE_BASE[index]
            )

    if not results:
        return "No directly matching knowledge was found. Use standard queue management practices."

    return "\n".join(results)
