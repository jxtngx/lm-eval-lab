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


"""collect output to a table for subjective feedback

this module ought to include a class object that calls an LM, and collects the output to a table.

that table can be displayed in a UI or shared via CSV to Google Sheets, and then be used to complete
a survey meant to capture a human's perception regarding the quality of the output.
"""
