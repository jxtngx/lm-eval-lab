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
import typer

from lm_eval_lab.utils.config import load_config

cfg = load_config(os.path.join(os.getcwd(), ".lab-configs/lab-config.yaml"))

app = typer.Typer()


@app.callback()
def callback() -> None:
    pass


@app.command("download")
def download(
    repo_id: str = "jxtngx/Meta-Llama-3.2-1B-Instruct-Q4_K_M-GGUF",
    filename: str = "*q4_k_m.gguf",
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
