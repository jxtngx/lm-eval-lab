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

import logging
import threading
from time import sleep
from typing import Optional

import uvicorn
from rich.logging import RichHandler

from lm_eval_lab.core.base_evaluator import BaseEvaluator

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = RichHandler(rich_tracebacks=True)
logger.addHandler(handler)


class Evaluator(BaseEvaluator):
    """control evaluation experiments"""

    def __init__(
        self,
        evals: list,
        model: str,
        n_gpu_layers: int,
        chat_format: Optional[str] = None,
        host: str = "localhost",
        port: int = 8000,
    ) -> None:
        super().__init__(evals, model, n_gpu_layers, chat_format=chat_format, host=host, port=port)
        self.on_evaluator_start()

    def run(self) -> None:
        self.start_server()  # should be non-blocking
        self.run_evals()  # blocking
        self.stop_server()  # should be non-blocking

    def run_evals(self) -> None:
        for eval in self.evals:
            logger.info(f"RUNNING {eval}")

    def start_server(self) -> None:
        self.server_thread.start()
        # give server time to start
        logger.info("STARTING SERVER")
        sleep(30)

    def stop_server(self) -> None:
        # see https://github.com/encode/uvicorn/discussions/1103#discussioncomment-6187606
        self.server.should_exit = True
        while self.server_thread.is_alive():
            continue
        logger.info("SERVER STOPPED")

    def on_evaluator_start(self) -> None:
        self.uvicorn_config = uvicorn.Config(
            app=self.llama_cpp_app,
            host=self.server_settings.host,
            port=self.server_settings.port,
            ssl_keyfile=self.server_settings.ssl_keyfile,
            ssl_certfile=self.server_settings.ssl_certfile,
        )
        self.server = uvicorn.Server(config=self.uvicorn_config)
        # use a separte thread to avoid blocking call
        self.server_thread = threading.Thread(target=self.server.run)
