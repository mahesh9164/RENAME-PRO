from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
import humanize
from helper.database import  insert 

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client,message):
	insert(int(message.chat.id))
	await message.reply_text(text =f"""
	Hello 👋 {message.from_user.first_name }
	
**☞ I'm A Telegram File & Video Rename Bot With Permanent Thumbnail Support.**

**☞ Send Me Any Telegram File/Video!** 

**☞ Send A Photo To Save As Permanent Thumbnail!**

**☞ Select Your Desired/Required Option!** 

**☞ Then Wait Till The Process Get Completed!**

**☞ Maintained By : @MAHI_458**

**☞ Want To Buy Owr Premium Rename Bot With Custom Caption Support Contact Me On @MAHI_458**
	""",reply_to_message_id = message.message_id ,  
	reply_markup=InlineKeyboardMarkup(
	 [[ InlineKeyboardButton("✰☆✩ 🅄🄿🄳🄰🅃🄴🅂  🄲🄷🄰🄽🄽🄴🄻 ✩☆✰" ,url="https://t.me/Amazon_Prime_Video_Officiall") ]  ]))


@Client.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client,message):
       media = await client.get_messages(message.chat.id,message.message_id)
       file = media.document or media.video or media.audio 
       filename = file.file_name
       filesize = humanize.naturalsize(file.file_size)
       fileid = file.file_id
       await message.reply_text(
       f"""__𝐖𝐡𝐚𝐭 𝐒𝐡𝐚𝐥𝐥 𝐈 𝐖𝐚𝐧𝐭𝐞𝐝 𝐓𝐨 𝐃𝐨 𝐖𝐢𝐭𝐡 𝐓𝐡𝐢𝐬 𝐅𝐢𝐥𝐞 ㋛︎__\n**File Name** :- {filename}\n**File Size** :- {filesize}"""
       ,reply_to_message_id = message.message_id,
       reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("📝  Rename ",callback_data = "rename")
       ,InlineKeyboardButton("✖️  Cancel ",callback_data = "cancel")  ]]))
