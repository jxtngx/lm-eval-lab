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
import signal
import threading
import uvicorn


from lm_eval_lab.core.base_evaluator import BaseEvaluator


class Evaluator(BaseEvaluator):
    """control evaluation experiments"""

    def __init__(self, evals: list, model: str, host: str = "localhost", port: int = 8000) -> None:
        super().__init__(evals, model, host=host, port=port)
        self.llama_cpp_app_pid: int | None = None

    def run(self) -> None:
        self.start_server()  # should be non-blocking
        assert self.llama_cpp_app_pid, "Server PID not set on server start"
        self.run_evals()  # blocking
        self.stop_server(self.llama_cpp_app_pid)  # should be non-blocking

    def run_evals(self) -> None: ...

    def start_server(self) -> None:
        config = uvicorn.Config(
            app=self.llama_cpp_app,
            host=self.server_settings.host,
            port=self.server_settings.port,
            ssl_keyfile=self.server_settings.ssl_keyfile,
            ssl_certfile=self.server_settings.ssl_certfile,
        )
        server = uvicorn.Server(config=config)
        # use a separte thread to avoid blocking call
        thread = threading.Thread(target=server.run)
        # set thread id so it can be killed progammatically
        self.llama_cpp_app_pid = thread.native_id

    def stop_server(self, thread_native_id: int) -> None:
        os.kill(thread_native_id, signal.SIGINT)
