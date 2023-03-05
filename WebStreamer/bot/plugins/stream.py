# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

import logging
from pyrogram import filters, errors, Client, enums
from pyrogram.errors import FloodWait, UserNotParticipant
from WebStreamer.vars import Var
from urllib.parse import quote_plus
from WebStreamer.bot import StreamBot, logger
from WebStreamer.utils import get_hash, get_name
from pyrogram.enums.parse_mode import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@StreamBot.on_message(
    filters.private
    & (
        filters.document
        | filters.video
        | filters.audio
        | filters.animation
        | filters.voice
        | filters.video_note
        | filters.photo
        | filters.sticker
    ),
    group=4,
)
async def media_receive_handler(c: Client, m: Message):
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await c.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == enums.ChatMemberStatus.BANNED:
                await c.send_message(
                    chat_id=m.chat.id,
                    text="__Sorry, you are banned. Contact My Owner [ Rushidhar ](https://telegram.me/Rushidhar1999)__",
                    
                    disable_web_page_preview=True
                )
                return 
        except UserNotParticipant:
            await c.send_message(
                chat_id=m.chat.id,
                text="""<i>🔐 Join Channel To Use Me 🔐</i>""",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🔓 Join Now 🔓", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                
            )
            return
        except Exception as e:
            await m.reply_text(e)
            await c.send_message(
                chat_id=m.chat.id,
                text="**Something Went Wrong. Contact** [ Rushidhar ](https://telegram.me/Rushidhar1999)",
                
                disable_web_page_preview=True)
            return

    try:
        log_msg = await m.forward(chat_id=Var.BIN_CHANNEL)
        file_hash = get_hash(log_msg, Var.HASH_LENGTH)
        stream_link = f"{Var.URL}{log_msg.id}/{(get_name(m))}?hash={file_hash}"
        short_link = f"{Var.URL}{file_hash}{log_msg.id}"
        logger.info(f"Generated link: {stream_link} for {m.from_user.first_name}")

        msg_text = """<b><i>Your Link Generated !</i></b>\n\n<b>📂 File Name :</b> <i>{}</i>\n\n<b>🚸 Note : LINK WON'T EXPIRE TILL I DELETE</b>"""
        await log_msg.reply_text(text=f"**RᴇQᴜᴇꜱᴛᴇᴅ ʙʏ :** [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n**Uꜱᴇʀ ɪᴅ :** `{m.from_user.id}`\n**Stream ʟɪɴᴋ :** {stream_link}", disable_web_page_preview=True, quote=True)
        await m.reply_text(
            text=msg_text.format(quote_plus(get_name(m))),
            quote=True,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    #[InlineKeyboardButton("😎 STREAM IN PLAYERS 😎", url=f"https://anshumanpm.pythonanywhere.com/stream?url={stream_link}")],
                    [InlineKeyboardButton("📥 DOWNLOAD 📥", url=stream_link)],
                    [InlineKeyboardButton("🖥 STREAM 🖥", url=f"https://playvideos.pages.dev/?url={stream_link}")],
                    [InlineKeyboardButton("❤️ SOURCE CODE ❤️", url="https://github.com/EverythingSuckz/TG-FileStreamBot")]
                ]
            )
        )
    except errors.ButtonUrlInvalid:
        log_msg = await m.forward(chat_id=Var.BIN_CHANNEL)
        file_hash = get_hash(log_msg, Var.HASH_LENGTH)
        stream_link = f"{Var.URL}{log_msg.id}/{(get_name(m))}?hash={file_hash}"
        short_link = f"{Var.URL}{file_hash}{log_msg.id}"
        logger.info(f"Generated link: {stream_link} for {m.from_user.first_name}")

        await m.reply_text(
            text="<code>{}</code>\n\nShortened: {})".format(
                stream_link, short_link
            ),
            quote=True,
            parse_mode=ParseMode.HTML,
        )
    except FloodWait as e:
        print(f"Sleeping for {str(e.x)}s")
        await asyncio.sleep(e.x)
        await c.send_message(chat_id=Var.BIN_CHANNEL, text=f"Got Floodwait Of {str(e.x)}s from [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n\n**User Id :** `{str(m.from_user.id)}`", disable_web_page_preview=True)
