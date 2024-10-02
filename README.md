# SLM Eval Lab

## The basics

A high level project to evaluate small language models (SLMs) with task based approaches, retrieval techniques, LMs as a judge, and human feedback. Using this repo should aid in the selection of SLMs based on user defined quantitative criteria and qualitative perception.

Focus will be given to LM variants belonging to the Llama, Minitron, and Nemotron (distillations) model families. See this Hugging Face [collection](https://huggingface.co/collections/jxtngx/slm-quants-66fd22225a60c216a7e30989) for quantized models. 

> [!NOTE]
> small language models are models with 8B parameters or fewer

> [!NOTE]
> the default model quantization in the listed HF collection is GGUF 4bit (K_M)

## Notes

- The core focus of this library is generating output for evaluation. The modules in the library reflect the mentioned techniques.
- LangChain is preferred for model provider integrations
- LlamaIndex is preferred for evaluating intermediate steps in RAG pipelines
- ChromaDB is preferred for simplicity as a local vectordb
- Ragas is preferred for LM performance metrics
- LangChain will be used for LMs as a judge