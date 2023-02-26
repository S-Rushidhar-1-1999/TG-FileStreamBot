# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from pyrogram.types import Message
from pyrogram.types import ReplyKeyboardMarkup

from WebStreamer.vars import Var 
from WebStreamer.bot import StreamBot

@StreamBot.on_message(filters.command("start") & filters.private)
async def start(b, m: Message):
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == enums.ChatMemberStatus.BANNED:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="__Sorry, you are banned. Contact My Owner [ Rushidhar ](https://telegram.me/Rushidhar1999)__",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
             await StreamBot.send_photo(
                chat_id=m.chat.id,
                photo="https://te.legra.ph/file/95db9bf6f91bd96d7a9f1.jpg",
                caption="<i>🔐 Join Channel To Use Me 🔐</i>",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🔓 Join Now 🔓", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                
            )
             return
        except Exception:
            await b.send_message(
                chat_id=m.chat.id,
                text="<i>Something went wrong</i> <b> <a href='https://telegram.me/Rushidhar1999'>CLICK HERE FOR SUPPORT </a></b>",

                disable_web_page_preview=True)
            return

    await StreamBot.send_photo(
        chat_id=m.chat.id,
        photo ="https://te.legra.ph/file/95db9bf6f91bd96d7a9f1.jpg",
        caption =f'Hi {m.from_user.mention(style="md")}!,\n\nI am Telegram File to Link Generator Bot.\n\nSend me any file and get a direct download link and streamable link.!',
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("👨‍💻 Owner 👨‍💻", url="https://telegram.me/Rushidhar1999")]
            ]
        )
    )
