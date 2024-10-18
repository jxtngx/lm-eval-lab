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
import threading
from typing import Optional

import typer

from lm_eval_lab.utils.load_files import load_config

cfg = load_config(os.path.join(os.getcwd(), ".lab-configs/lab-config.yaml"))
app = typer.Typer()


@app.callback()
def callback() -> None:
    pass


@app.command("download")
def download(
    repo_id: str = f"{cfg.model.owner}/{cfg.model.name}",
    filename: str = cfg.model.filename,
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


@app.command("serve")
def serve(
    model: str = ".models/llama-3.2-1b-instruct-q4_k_m.gguf",
    chat_format: Optional[str] = None,
    host: str = "localhost",
    port: int = 8000,
) -> None:
    from time import sleep
    import uvicorn
    from llama_cpp.server.app import create_app
    from llama_cpp.server.settings import ModelSettings, ServerSettings

    model_settings = ModelSettings(
        model=model,
        chat_format=chat_format,
        use_mlock=False,  # avoids `warning: failed to munlock buffer: Cannot allocate memory`
    )
    server_settings = ServerSettings(
        host=host,
        port=port,
        ssl_keyfile=None,
        ssl_certfile=None,
    )

    app = create_app(model_settings=[model_settings], server_settings=server_settings)

    config = uvicorn.Config(
        app=app,
        host=server_settings.host,
        port=server_settings.port,
        ssl_keyfile=server_settings.ssl_keyfile,
        ssl_certfile=server_settings.ssl_certfile,
    )
    server = uvicorn.Server(config=config)
    # use a separte thread to avoid blocking call
    # see https://github.com/encode/uvicorn/discussions/1103#discussioncomment-6187606
    print("STARTING SERVER")
    thread = threading.Thread(daemon=True, target=server.run)
    thread.start()
    print("WAITING")
    sleep(15)
    assert isinstance(thread.native_id, int), f"PID is {thread.native_id}"
    print("SLEEPING")
    sleep(15)
    print("SHUTTING DOWN SERVER")
    server.should_exit = True
    while thread.is_alive():
        continue
    print("SERVER STOPPED")
