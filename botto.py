import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyromod import listen
from config import *

bot = Client('bot',api_id=API_ID,api_hash=API_HASH,bot_token=TOKEN)

homebuttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="Network", url = "t.me/Anime_HeavenD"
            ),
            InlineKeyboardButton(
                text="FAQs", callback_data="faqsinline"
            ),
        ],
    ]
)
backbutton= InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="Back", callback_data = "backbutton"
            )
        ]
    ]
) 


@bot.on_callback_query(filters.regex("faqsinline"))
async def faqs(_, query):
    texto = """Hey! Again 
I am request bot of Anime Heaven

Here are some things you have to keep in mind while request anything through me.

1. Make sure to check if the anime which you are requesting is already uploaded. 

2. If you wanna contact admins use "/message" cmd.

3. You can request by "/request" cmd. 

4.Spamming in bot will lead you to ban :) 

5. Be safe and join our discussion group @animeheavenhell
"""
    await query.message.edit(text=texto, reply_markup= backbutton)

@bot.on_callback_query(filters.regex("backbutton"))
async def back(_, query):
    text = f"<b>Hello {query.message.from_user.mention}\nI'm a Request Bot made for @Anime_HeavenD\nDo <code>/request</code> to Request something</b>"
    await query.message.edit(text = text, reply_markup=homebuttons)
    
@bot.on_message(filters.command('start'))
async def main(client, message):
    text = f"<b>Hello {message.from_user.mention}\nI'm a Request Bot made for @Anime_HeavenD\nDo <code>/request</code> to Request something</b>"
    await message.reply_text(text=text, reply_markup=homebuttons)

@bot.on_message(filters.command('message'))
async def message(client, message):
    message=await bot.ask(chat_id=message.chat.id, text="Do you have some Message for The Admins? Say It and I'll Deliver it to Them")
    if message.text=="/cancel":
        return await message.reply_text("cancel")
    message=f"<b>User: </b>{message.from_user.mention}\n<b>Message: </b>{message.text}"
    await bot.send_message(ADMIN_CHAT, message)

@bot.on_message(filters.command('reply'))
async def reply(client, message):
    text = message.text
    text2 = text.split(" ", 2)
    msg= text2[2]
    usr = text2[1]
    try:
        await bot.send_message(usr, msg)
        await message.reply_text(f"Sent message\nMessage = {msg}")
    except TelegramError as e:
        await message.reply_text(e)
        
@bot.on_message(filters.regex('start=request'))
@bot.on_message(filters.regex('/request'))
async def request(client, message):
    texto = f"<b>What do you want to Request?</b>\n<b>Options are:</b>\n<code>Anime</code>\n<code>Manga</code>\n<code>Movie</code>\n<code>Hentai</code>\n<code>Sticker</code>\n<code>Wallpaper</code>\n<code>Theme</code>\n<code>Music</code>\n<code>Novel</code>\n<code>Amv</code>"
    cat = await bot.ask(chat_id=message.chat.id, text=texto)
    cat.text=cat.text.lower()
    if cat.text=="anime":
        anm_req = await bot.ask(chat_id=message.chat.id, text="Tell the name of Anime you want to Request")
        anm_quality = await bot.ask(chat_id=message.chat.id, text="Now tell me which Quality you Prefer")
        if anm_req.text=="/cancel":
            return await message.reply_text("Cancelled")
        if anm_quality.text=="/cancel":
            return await message.reply_text("Cancelled")
        anm_req_send= f"#AnimeRequest\n<b>Anime: </b>{anm_req.text}\n<b>Quality: </b>{anm_quality.text}\n<b>User: </b>{message.from_user.mention}"
        await bot.send_message(ADMIN_CHAT, anm_req_send)
        await message.reply_text(f"Done, Sent your request for {anm_req.text} to The Admins")
    elif cat.text=="manga":
        mng_req = await bot.ask(chat_id=message.chat.id, text="Tell the name of Manga you want to Request")
        if mng_req.text=="/cancel":
            return await message.reply_text("Cancelled")
        mng_req_send= f"#MangaRequest\n<b>Manga: </b>{mng_req.text}\n<b>User: </b>{message.from_user.mention}"
        await bot.send_message(ADMIN_CHAT, mng_req_send)
        await message.reply_text(f"Done, Sent your request for {mng_req.text} to The Admins")
    elif cat.text=="hentai":
        hnt_req = await bot.ask(chat_id=message.chat.id, text="Tell the name of Hentai you want to Request")
        if hnt_req.text=="/cancel":
            return await message.reply_text("Cancelled")
        hnt_req_send= f"#HentaiRequest\n<b>Hentai: </b>{hnt_req.text}\n<b>User: </b>{message.from_user.mention}"
        await bot.send_message(ADMIN_CHAT, hnt_req_send)
        await message.reply_text(f"Done, Sent your request for {hnt_req.text} to The Admins")
    elif cat.text=="movie":
        mov_req = await bot.ask(chat_id=message.chat.id, text="Tell the name of Movie you want to Request")
        if mov_req.text=="/cancel":
            return await message.reply_text("Cancelled")
        mov_req_send= f"#MovieRequest\n<b>Movie: </b>{mov_req.text}\n<b>User: </b>{message.from_user.mention}"
        await bot.send_message(ADMIN_CHAT, mov_req_send)
        await message.reply_text(f"Done, Sent your request for {mov_req.text} to The Admins")
    elif cat.text=="sticker":
        stk_req = await bot.ask(chat_id=message.chat.id, text="Tell the name of Anime/Character whose Sticker you want")
        if stk_req.text=="/cancel":
            return await message.reply_text("Cancelled")
        stk_req_send= f"#StickerRequest\n<b>Sticker: </b>{stk_req.text}\n<b>User: </b>{message.from_user.mention}"
        await bot.send_message(ADMIN_CHAT, stk_req_send)
        await message.reply_text(f"Done, Sent your request for {stk_req.text} to The Admins")
    elif cat.text=="wallpaper":
        wal_req = await bot.ask(chat_id=message.chat.id, text="Tell the name of Anime/Character whose Wallpaper you want")
        wal_type = await bot.ask(chat_id=message.chat.id, text="What kind of Wallpaper would you Like?")
        if wal_req.text=="/cancel":
            return await message.reply_text("Cancelled")
        if wal_type.text=="/cancel":
            return await message.reply_text("Cancelled")
        wal_req_send= f"#WallpaperRequest\n<b>Wallpaper: </b>{wal_req.text}\n<b>Type: </b>{wal_type.text}\n<b>User: </b>{message.from_user.mention}"
        await bot.send_message(ADMIN_CHAT, wal_req_send)
        await message.reply_text(f"Done, Sent your request for {wal_req.text} to The Admins")
    elif cat.text=="theme":
        thm_req = await bot.ask(chat_id=message.chat.id, text="Tell the name of Anime/Character whose Theme you want")
        thm_type = await bot.ask(chat_id=message.chat.id, text="What kind of Theme would you Like?")
        if thm_req.text=="/cancel":
            return await message.reply_text("Cancelled")
        if thm_type.text=="/cancel":
            return await message.reply_text("Cancelled")
        thm_req_send= f"#ThemeRequest\n<b>Theme: </b>{thm_req.text}\n<b>Type: </b>{thm_type.text}\n<b>User: </b>{message.from_user.mention}"
        await bot.send_message(ADMIN_CHAT, thm_req_send)
        await message.reply_text(f"Done, Sent your request for {thm_req.text} to The Admins")
    elif cat.text=="music":
        msc_req = await bot.ask(chat_id=message.chat.id, text="Tell the name of Music you want")
        msc_det = await bot.ask(chat_id=message.chat.id, text="If you can, Tell me the Name of it's Artist/Anime")
        if msc_req.text=="/cancel":
            return await message.reply_text("Cancelled")
        if msc_det.text=="/cancel":
            return await message.reply_text("Cancelled")
        msc_req_send= f"#MusicRequest\n<b>Music: </b>{msc_req.text}\n<b>Artist: </b>{msc_det.text}\n<b>User: </b>{message.from_user.mention}"
        await bot.send_message(ADMIN_CHAT, msc_req_send)
        await message.reply_text(f"Done, Sent your request for {msc_req.text} to The Admins")
    elif cat.text=="novel":
        nvl_req = await bot.ask(chat_id=message.chat.id, text="Tell the name of Novel you want to Request")
        if nvl_req.text=="/cancel":
            return await message.reply_text("Cancelled")
        nvl_req_send= f"#NovelRequest\n<b>Novel: </b>{nvl_req.text}\n<b>User: </b>{message.from_user.mention}"
        await bot.send_message(ADMIN_CHAT, nvl_req_send)
        await message.reply_text(f"Done, Sent your request for {nvl_req.text} to The Admins")
    elif cat.text=="amv":
        amv_req = await bot.ask(chat_id=message.chat.id, text="Send the Link of Amv You want to be Posted on Channel")
        if amv_req.text=="/cancel":
            return await message.reply_text("Cancelled")
        amv_req_send= f"#AmvRequest\n<b>Amv: </b>{amv_req.text}\n<b>User: </b>{message.from_user.mention}"
        await bot.send_message(ADMIN_CHAT, amv_req_send)
        await message.reply_text(f"Done, Sent your request for {amv_req.text} to The Admins")
    elif cat.text=="/cancel":
        await message.reply_text("Cancelled")
        return
    else:
        await message.reply_text("Error. You probably Sent the Spelling Wrong")


bot.run()
