# Copyright Justin R. Goheen.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from typing import Optional

import typer

from lm_eval_lab.utils.load_files import load_config

# configs
lab_cfg = load_config(os.path.join(os.getcwd(), ".lab-configs/lab-config.yaml"))
eval_cfg = load_config(os.path.join(os.getcwd(), ".lab-configs/eval-config.yaml"))

# typer app
app = typer.Typer()
evaluator_app = typer.Typer()
app.add_typer(evaluator_app, name="evaluator")


@app.callback()
def callback() -> None:
    pass


@app.command("download")
def download(
    repo_id: str = f"{lab_cfg.model.owner}/{lab_cfg.model.name}",
    filename: str = lab_cfg.model.filename,
    verbose: bool = False,
    models_dir: str = ".models",
) -> None:
    from llama_cpp import Llama

    Llama.from_pretrained(
        repo_id=repo_id,
        filename=filename,
        verbose=verbose,
        local_dir=models_dir,
        cache_dir=models_dir,
    )


@evaluator_app.command("run")
def run_evaluator(
    model: str = eval_cfg.model,
    n_gpu_layers: int = -1,
    chat_format: Optional[str] = None,
    host: str = "localhost",
    port: int = 8000,
) -> None:
    from lm_eval_lab import Evaluator

    evaluator = Evaluator(
        evals=[k for k in eval_cfg.evaluations if eval_cfg.evaluations[k]],
        model=model,
        n_gpu_layers=n_gpu_layers,
        chat_format=chat_format,
        host=host,
        port=port,
    )

    evaluator.run()
