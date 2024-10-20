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

from abc import ABC, abstractmethod
from typing import Optional

from llama_cpp.server.app import create_app
from llama_cpp.server.settings import ModelSettings, ServerSettings


class BaseEvaluator(ABC):
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
        self.evals = evals
        self.model = model
        self.n_gpu_layers = n_gpu_layers
        self.chat_format = chat_format
        self.host = host
        self.port = port

    @abstractmethod
    def run(self) -> None:
        """run experiments"""
        ...

    @abstractmethod
    def run_evals(self) -> None:
        """run experiments"""
        ...

    @abstractmethod
    def start_server(self) -> None:
        """start the server backend"""
        ...

    @abstractmethod
    def stop_server(self) -> None:
        """stop the server backend"""
        ...

    @property
    def model_settings(self) -> ModelSettings:
        """model settings to pass to llama-cpp app"""
        return ModelSettings(
            model=self.model,
            n_gpu_layers=self.n_gpu_layers,
            chat_format=self.chat_format,
            use_mlock=False,  # avoids `warning: failed to munlock buffer: Cannot allocate memory`
        )

    @property
    def server_settings(self) -> ServerSettings:
        """server settings to pass to llama-cpp app"""
        return ServerSettings(
            host=self.host,
            port=self.port,
            ssl_keyfile=None,
            ssl_certfile=None,
        )

    @property
    def llama_cpp_app(self):
        llama_cpp_app = create_app(
            model_settings=[self.model_settings],
            server_settings=self.server_settings,
        )
        return llama_cpp_app

    def on_evaluator_start(self) -> None:
        """complete tasks before running evaluations"""
        ...

    def on_evaluator_end(self) -> None:
        """finish experiment logs and teardown"""
        ...

    def log_metric(self) -> None:
        """log a metric on task completion"""
        ...

    def log_trace(self) -> None:
        """log an agent action as a trace"""
        ...
