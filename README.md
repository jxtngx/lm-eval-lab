# SLM Eval Lab

A high level project to evaluate small language models (SLMs) with task based approaches, retrieval techniques, LMs as a judge, and human feedback. Using this repo should aid in the selection of SLMs based on user defined quantitative criteria and qualitative perception.

Focus will be given to LM variants belonging to the Llama, Minitron, and Nemotron (distillations) model families. See this Hugging Face [collection](https://huggingface.co/collections/jxtngx/slm-quants-66fd22225a60c216a7e30989) for quantized models. 

> [!NOTE]
> small language models are models with 8B parameters or fewer

## To do

- [ ] consolidate setup.py and setup.cfg to pyproject.toml
- [ ] choose lm-eval tasks
- [ ] locate persona dataset (e.g. [argilla/FinePersonas-v0.1](https://huggingface.co/datasets/argilla/FinePersonas-v0.1)) and determine suitability for use
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
- ChromaDB is preferred for simplicity as a local vectordb
- Ragas is preferred for LM performance metrics
- LangChain will be used for LMs as a judge
- the default model quantization in the listed HF collection is GGUF 4KM