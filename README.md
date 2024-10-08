# Eval Lab

> [!IMPORTANT]
> this project is under active development

## The basics

Eval Lab is a high level project to evaluate language models (LMs) with task based approaches, retrieval techniques, LMs as a judge, and human feedback. Using this repo should aid in the selection of LMs based on user defined quantitative criteria and qualitative perception.

Focus will be given to LM variants belonging to the Llama, Minitron, and Nemotron model families. See this Hugging Face [collection](https://huggingface.co/collections/jxtngx/slm-quants-66fd22225a60c216a7e30989) for quantized models.

> [!NOTE]
> the default model quantization in the listed HF collection is GGUF 4bit (K_M)

## Concept

Eval Lab should have a main class `Evaluator`; which is similar to `Trainer` objects in deep learning. `Evaluator` will accept a packet of evaluations to run, and those evaluations include the library interfaces e.g.

```python
from eval_lab import Evaluator, Human, Judge, Synth, Harness

human = Human(arg1, arg2, ...)
judge = Judge(metrics=[...])
synth = Synth(retriever="similarity", embed_model="model", reranker="model")
harness = Harness(tasks=[...])

evaluator = Evaluator(
    tasks = [
        human,  #  collect output for human feedback
        judge,  # LM as a Judge
        synth,  # evaluate the LM in a RAG pipeline as the synthesizer
        harness  # run lm-eval-harness tasks
    ]
)

evaluator.run()
```

Running the evaluator will log results to the user defined log dir or `eval-lab/logs/evaluator`.

## Notes

- The core focus of this library is generating output for evaluation. The modules in the library reflect the mentioned techniques.
- LangChain is preferred for model provider integrations
- LlamaIndex is preferred for evaluating intermediate steps in RAG pipelines
- ChromaDB is preferred for simplicity as a local vectordb
- Ragas is preferred for LM performance metrics
- LangChain will be used for LMs as a judge
- Output will be collected to a table for human feedback to mock [this survey](https://github.com/aws-samples/human-in-the-loop-llm-eval-blog). 