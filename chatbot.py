# ==========================================================
# chatbot.py
# AI FAQ Chatbot using TF-IDF + Cosine Similarity
# ==========================================================

import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from preprocess import preprocess


class FAQChatbot:

    def __init__(self, csv_file="data/faq.csv"):

        self.csv_file = csv_file

        # Load FAQ dataset
        print(csv_file)
        import os 
        print(os.path.exists(csv_file))
        self.data = pd.read_csv(csv_file)
        

        # Remove empty rows
        self.data.dropna(inplace=True)

        # Preprocess questions
        self.data["Processed"] = self.data["Question"].apply(preprocess)

        # Create TF-IDF Vectorizer
        self.vectorizer = TfidfVectorizer()

        # Convert questions into vectors
        self.question_vectors = self.vectorizer.fit_transform(
            self.data["Processed"]
        )

    # -------------------------------------------------------

    def get_answer(self, user_question):

        if user_question.strip() == "":
            return "Please enter a question."

        # Preprocess user question
        cleaned_question = preprocess(user_question)

        # Convert into vector
        user_vector = self.vectorizer.transform([cleaned_question])

        # Cosine Similarity
        similarity_scores = cosine_similarity(
            user_vector,
            self.question_vectors
        )

        # Highest similarity
        best_index = similarity_scores.argmax()

        best_score = similarity_scores[0][best_index]

        # Threshold
        if best_score < 0.30:
            return (
                "Sorry! I couldn't find a matching answer.\n"
                "Please try asking differently."
            )

        return self.data.iloc[best_index]["Answer"]

    # -------------------------------------------------------

    def confidence_score(self, user_question):

        cleaned_question = preprocess(user_question)

        user_vector = self.vectorizer.transform([cleaned_question])

        similarity_scores = cosine_similarity(
            user_vector,
            self.question_vectors
        )

        return round(float(similarity_scores.max()) * 100, 2)


# ==========================================================
# Testing
# ==========================================================

if __name__ == "__main__":

    bot = FAQChatbot()

    print("=" * 50)
    print("AI FAQ Chatbot")
    print("Type 'exit' to quit.")
    print("=" * 50)

    while True:

        question = input("\nYou : ")

        if question.lower() == "exit":
            break

        answer = bot.get_answer(question)

        score = bot.confidence_score(question)

        print("\nBot :", answer)
        print("Confidence :", score, "%")