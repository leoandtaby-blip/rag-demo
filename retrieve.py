import os


def load_documents(folder="."):
    documents = {}
    for filename in os.listdir(folder):
        if filename.endswith(".txt"):
            path = os.path.join(folder, filename)
            with open(path, "r", encoding="utf-8") as f:
                documents[filename] = f.read()
    return documents


def get_words(text):
    return {word.strip(".,?!") for word in text.lower().split()}


def find_best_match(question, documents):
    question_words = get_words(question)
    best_name = None
    best_score = 0
    for name, text in documents.items():
        score = len(question_words & get_words(text))
        if score > best_score:
            best_score = score
            best_name = name
    return best_name

if __name__ == "__main__":
    docs = load_documents()
    question = "How much does express delivery cost?"
    match = find_best_match(question, docs)
    print("Question:", question)
    print("Best matching file:", match)
