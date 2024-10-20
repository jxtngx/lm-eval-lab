# LM Eval Lab

> [!IMPORTANT]
> this project is under active development

## The basics

LM Eval Lab is a high level project to evaluate language models (LMs) with task based approaches, as a synthesizer in RAG, in LM as a judge scenarios (as judge and judged), and collecting output for human feedback.

### Intent

Using this repo should aid in the selection of LMs based on user defined quantitative criteria and qualitative perception.

### Models

Focus will be given to open LM variants belonging to Meta, NVIDIA, and Nous Research.

> [!NOTE]
> See this Hugging Face [collection](https://huggingface.co/collections/jxtngx/slm-quants-66fd22225a60c216a7e30989) for quantized models.

> [!NOTE]
> the default model quantization in the listed HF collection is GGUF 4bit (K_M)

## Concept

LM Eval Lab's main class is `Evaluator`; which is similar to `Trainer` objects in deep learning in that these objects control other core interfaces and supporting interfaces. 

`Evaluator` will accept an iterable of evaluations to run, and those evaluations are determined by the areas mentioned in the basics section e.g.

```python
from lm_eval_lab import Evaluator, Human, Judge, Synth, Harness

human = Human(...)
judge = Judge(metrics=[...])
synth = Synth(retriever="similarity", embed_model="model", reranker="model")
harness = Harness(tasks=[...])

evaluator = Evaluator(
    evals = [
        human,  # collect output for human feedback
        judge,  # LM as a Judge
        synth,  # evaluate the LM in a RAG pipeline as the synthesizer
        harness  # run lm-eval-harness tasks
    ]
)

evaluator.run()
```

Running the evaluator will log results to the user defined directory or `lm-eval-lab/logs/evaluator`.

## Run times

The length of time it takes to run evaluations depends on several factors, including:

- the machine we own or have virtual access to
- the size of the model
- the amount of evals
- the type of evals
- the subtasks performed by the evals

In other words: if we own an M-series MacBook Pro or have access to a single NVIDIA A10G or Tesla T4, we will need to select a small language model (8B parameters or fewer) that has likely been quantized (made smaller, so to speak), and – while we can run each of (`Human`, `Judge`, `Synth`, `Harness`), we would want to limit the tasks included in `Harness` (defaults are [mmlu, hellaswag, gsm8k]) to achieve a reasonable run time.

## Compute environments

Assuming a single GPU, care ought to be taken to load the model as efficiently as possible; which likely means that evals ought to be in a queue (a simple for loop) in order to load the model one time only. Though not ideal in terms of reducing run times, iterating through the evals one at a time will help to avoid out-of-memory errors we may encounter if attempting to run evals in parallel in compute limited environments.

In a multi-GPU environment, run times could be reduced by distributing simple evals (`Human`, `Judge`) to one device, and complex evals (`Synth`, `Harness`) on the remainder of the devices. Though this requires knowledge of backend APIs that have to do with device count and device placement (including CPU offloading).

Such design decisions require selecting dependencies based on device awareness i.e. distributed evals or single device evals; and device architectures – Apple's MPS, NVIDIA's CUDA etc. 

## Notes

- The core focus of this library is generating output for evaluation. The modules in the library reflect the mentioned techniques.
- LangChain is preferred for model provider integrations
- LlamaIndex is preferred for evaluating intermediate steps in RAG pipelines
- ChromaDB is preferred for simplicity as a local vectordb
- Ragas is preferred for LM performance metrics
- LangChain will be used for LMs as a judge
- Output will be collected to a table for human feedback to mock [this survey](https://github.com/aws-samples/human-in-the-loop-llm-eval-blog). 
