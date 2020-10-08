# MIT License
#
# Copyright (c) 2020 Dan Tès <https://github.com/delivrance>
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

import requests

from pyrogram import Client, filters

BASE = "https://hastebin.com"


@Client.on_message(filters.command("haste", prefixes=("!",)) & filters.reply)
def haste(client, message):
    reply = message.reply_to_message

    if reply.text is None:
        return

    message.delete()

    result = requests.post(
        "{}/documents".format(BASE), data=reply.text.encode("UTF-8")
    ).json()

    message.reply(
        "{}/{}.py".format(BASE, result["key"]), reply_to_message_id=reply.message_id
    )
