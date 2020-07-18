# Telegram draft listener
Telegram allows users to use cloud drafts that can contain up to about 16000 characters which can be used for sending data to the server from telegram app. The ordinary message sending process can cause problems like losing spaces and line breaks or wrong messages order.

This code uses [pyrogram](https://github.com/pyrogram/pyrogram) and [telegraph](https://github.com/python273/telegraph) libraries for creating the telegraph page with correct line breaks and paragraphs from the draft.
