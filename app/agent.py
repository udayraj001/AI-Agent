from transformers import pipeline

# Initialize NLP pipelines
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

def ask_ai(question, context=""):
    """Use the QA pipeline for answering specific questions."""
    if context:
        result = qa_pipeline(question=question, context=context)
        return result['answer']
    return "I need more context to answer this question."
