# MIT License
#
# Copyright (c) 2018 Furoin <https://github.com/furoin>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from pyrogram import Client, Filters

eval_running_text = "**Eval Code:**\n```{code}```\n**Running...**"
eval_success_text = "**Eval Code:**\n```{code}```\n**Success**"
eval_error_text = "**Eval Code:**\n```{code}```\n**Error:**\n```{error}```"
eval_result_text = "**Eval Code:**\n```{code}```\n**Result:**\n```{result}```"


@Client.on_message(Filters.command("eval", prefix="!"))
def evalcode(client, message):
    code = " ".join(message.command[1:])
    if code:
        m = client.send_message(message.chat.id, eval_running_text.replace('{code}', code), parse_mode="MARKDOWN")
        try:
            result = eval(code)

        except Exception as e:
            client.edit_message_text(message.chat.id, m.message_id,
                                     eval_error_text.replace('{code}', code).replace('{error}', str(e)),
                                     parse_mode="MARKDOWN")
        else:
            if result:
                client.edit_message_text(message.chat.id, m.message_id,
                                         eval_result_text.replace('{code}', code).replace('{result}', str(result)),
                                         parse_mode="MARKDOWN")

            else:
                client.edit_message_text(message.chat.id, m.message_id,
                                         eval_success_text.replace('{code}', code),
                                         parse_mode="MARKDOWN")
