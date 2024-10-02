"""create a RAG pipeline and collect metrics on intermediate steps and components of the pipeline

this module ought to provide a class that interfaces with unstructured and llama-index to evaluate
a RAG pipeline; where the pipeline includes a retriever, a reranker, and the synthesizer. metrics
should calculated using ragas.
"""
