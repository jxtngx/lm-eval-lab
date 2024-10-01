# SLM Eval Lab

A high level library to evaluate small language models (SLMs) with task based approaches, retrieval techniques, LMs as a judge, and human feedback.

This library aids in the selection of SLMs based on user defined criteria and perception.

## To do

- [ ] consolidate setup.py and setup.cfg to pyproject.toml
- [ ] choose lm-eval tasks
- [ ] determine models (likely Nemotron distilled, Minitron, Phi 3 mini, Llama 3.1 and 3.2)
- [ ] locate persona dataset (e.g. [argilla/FinePersonas-v0.1](https://huggingface.co/datasets/argilla/FinePersonas-v0.1)) and determine suitability
- [ ] check installation and usage in Colab
- [ ] check clone and usage in GPU enabled instance
- [ ] craft prompts for LM as a judge
- [ ] find an up-to-date python util to collect nvidia-smi metrics
- [ ] read these [eval details and techniques](https://huggingface.co/datasets/meta-llama/Llama-3.2-3B-Instruct-evals) by Meta
- [ ] read and watch [this resource](https://docs.smith.langchain.com/concepts/evaluation#llm-as-judge) by LangChain on LMs as a judge

## Notes

- The core focus of this library is generating output for evaluation. The modules in the library reflect the mentioned techniques.
- LangChain is preferred for model provider integrations
- LlamaIndex is preferred for evaluating intermediate steps in RAG pipelines
- ChromaDB is preferred as a basic vectordb
- Ragas is preferred for LM performance metrics
- Either DeepEval or LangChain will be used for LMs as a judge