# MIT License
#
# Copyright (c) 2020 BrightSide <https://github.com/bright5ide>
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

from pyrogram import Client, filters


@Client.on_message(
    filters.command("r", prefixes=("!",)) & filters.reply & ~filters.edited & filters.group
)
def r(client, message):
    if len(message.command) > 1:
        colength = len("r") + len("!")
        query = str(message.text)[colength:].lstrip()
        eventsplit = query.split("/")
        result = "**You mean:**\n{}".format(
            message.reply_to_message.text.replace(eventsplit[0], eventsplit[1])
        )
        client.edit_message_text(message.chat.id, message.message_id, result)
