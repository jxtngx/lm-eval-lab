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

import tomllib
from pathlib import Path
from typing import Union


def load_system_prompt(prompt_path: Union[str, Path]) -> str:
    with open(prompt_path, "rb") as f:
        system_prompt = tomllib.load(f)
    return system_prompt["system"]["prompt"]
