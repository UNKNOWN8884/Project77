class script(object):
    START_TXT = """𝙷𝙴𝙻𝙾 {},
𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 <a href=https://t.me/{}>{}</a>, 𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂, 𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙴𝙽𝙹𝙾𝚈 😍"""
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: {}
🧑‍💻 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href=https://t.me/CRACKERON>Cʀᴀᴄᴋᴇʀ 🧑‍💻</a>
🏣 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
🗣️ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: Eɴɢʟɪsʜ
ℹ️ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: Pʀɪᴠᴀᴛᴇ
💾 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: Pʀɪᴠᴀᴛᴇ
✯ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: v68.3.1 [ 𝙱𝙴𝚃𝙰 ]"""
    SOURCE_TXT = """<b>NOTE:</b>
-    Lɪʟʟʏ ᴘʀᴏᴊᴇᴄᴛ Is ɴᴏᴛ ᴀ Oᴘᴇɴ Sᴏᴜʀᴄᴇ . Bᴇᴄᴀᴜsᴇ Cᴏᴘʏʀɪɢʜᴛ


<b>DEVS:</b>
- <a href=https://t.me/CRACKERON>Cʀᴀᴄᴋᴇʀ 🧑‍💻</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Fɪʟᴛᴇʀ Is Tʜᴇ Fᴇᴀᴛᴜʀᴇ ᴡᴇʀᴇ ᴜsᴇʀs ᴄᴀɴ sᴇᴛ Aᴜᴛᴏᴍᴀᴛᴇᴅ Rᴇᴘʟɪᴇs ғᴏʀ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴋᴇʏᴡᴏʀᴅ ᴀɴᴅ Cʀᴀᴄᴋᴇʀ ᴡɪʟʟ ʀᴇsᴘᴏɴᴅ ᴡʜᴇɴᴇᴠᴇʀ ᴀ ᴋᴇʏᴡᴏʀᴅ ɪs ғᴏᴜɴᴅ ᴛʜᴇ ᴍᴇssᴀɢᴇ


<b>NOTE:</b>
1.Cʀᴀᴄᴋᴇʀ  sʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
2. Oɴʟʏ Aᴅᴍɪɴs Cᴀɴ ᴀᴅᴅ ғɪʟᴛᴇʀs ɪɴ ᴀ ᴄʜᴀᴛ.
3. Aʟᴇʀᴛ Bᴜᴛᴛᴏɴs ʜᴀᴠᴇ ᴀ ʟɪᴍɪᴛ ᴏғ 64 ᴄʜᴀʀᴀᴄᴛᴇʀs.
  
 
<b>Commands and Usage:</b>
• /filter - <code>Aᴅᴅ Fɪʟᴛᴇʀ Iɴ Cʜᴀᴛ</code>
• /filters - <code>Lɪsᴛ Oғ Aʟʟ Fɪʟᴛᴇʀs ɪɴ Cʜᴀᴛ</code>
• /del - <code>ᴅᴇʟᴇᴛᴇ ᴀ Sᴘᴇᴄɪғɪᴄ Fɪʟᴛᴇʀ ɪɴ ᴄʜᴀᴛ</code>
• /delall - <code>Dᴇʟᴇᴛᴇ Tʜᴇ Wʜᴏʟᴇ Fɪʟᴛᴇʀ ɪɴ Cʜᴀᴛ(chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Mᴋ Sᴜᴘᴘᴏʀᴛs ʙᴏᴛʜ ᴜʀʟ ᴀɴᴅ ᴀʟᴇʀᴛ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴs.


<b>NOTE:</b>
1. Tᴇʟᴇɢʀᴀᴍ ᴡɪʟʟ ɴᴏᴛ ᴀʟʟᴏᴡs ʏᴏᴜ ᴛᴏ sᴇɴᴅ ʙᴜᴛᴛᴏɴs ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴄᴏɴᴛᴇɴᴛ, sᴏ ᴄᴏɴᴛᴇɴᴛ ɪs ᴍᴀɴᴅᴀᴛᴏʀʏ.
2. Mᴋ  sᴜᴘᴘᴏʀᴛs ʙᴜᴛᴛᴏɴs ᴡɪᴛʜ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ ᴛʏᴘᴇ.
3. Bᴜᴛᴛᴏɴs sʜᴏᴜʟᴅ ʙᴇ ᴘʀᴏᴘᴇʀʟʏ ᴘᴀʀsᴇᴅ ᴀs ᴍᴀʀᴋᴅᴏᴡɴ ғᴏʀᴍᴀᴛ.

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>
       
           IMBD_TXT = """Sᴇᴀʀᴄʜ Yᴏᴜʀ Mᴏᴠɪᴇs Iɴғᴏʀᴍᴀᴛɪᴏɴ Ex: Mᴏᴠɪᴇs Pʜᴏᴛᴏs Mᴏᴠɪᴇs Iɴғᴏʀᴍᴀᴛɪᴏɴ
- Sᴇᴀʀᴄʜ ғʟɪᴍ Dᴇᴛᴀɪʟs Wɪᴛʜᴏᴜᴛ Lᴇᴀᴠɪɴɢ Tᴇʟᴇɢʀᴀᴍ
- Sᴇᴀʀᴄʜ ᴀɴʏᴛʜɪɴɢ Wɪᴛʜᴏᴜᴛ Lᴇᴀᴠɪɴɢ Tᴇʟᴇɢʀᴀᴍ
<b>U𝗌𝖺𝗀𝖾:</b>
- /imdb - Gᴇᴛ ᴛʜᴇ Fɪʟᴇ ɪɴʀᴏᴍᴀᴛɪᴏɴ Fʀᴏᴍ Iᴍʙᴅ sᴏᴜʀᴄᴇ
- /search - Gᴇᴛ ᴛʜᴇ Fɪʟᴍ Iɴғᴏʀᴍᴀᴛɪᴏɴ ғᴏʀᴍ Vᴀʀɪᴏᴜs Sᴏᴜʀᴄᴇ
     
     Bʏ A : @CRACKERON 🧑‍💻"""
    FUN_TXT = """ҒႮΝ ᎷϴᎠᎬ
ᏔᎬᏞᏟϴᎷᎬ Ͳϴ ҒႮΝ ᎷϴᎠᎬ Ꭰϴ ͲᎻᎬ ҒϴᏞᏞϴᏔᏆΝᏀ 💥
1. /dice- Ͳϴ ᎡϴᏞᏞ ͲᎻᎬ ᎠᏆᏟᎬ
2./throw - Ͳϴ ᎷᎪᏦᎬ ᎠᎡᎪͲ
3./goal - Ͳϴ ᎷᎪᏦᎬ Ꭺ ᏀϴᎪᏞ
4./vthrow- Ͳϴ ᏢᏞᎪᎽ Ꭺ ᏙϴᏞᏞᎽ ᏴᎪᏞᏞ
5./sthrow- Ͳϴ ͲᎻᎡϴᏔ Ꭺ ᎪΝϴͲᎻᎬᎡ ͲᎪᎡᏀᎬͲ
6./luck- Ͳϴ ͲᎡᎽ ᎽϴႮᎡ ᏞႮᏟᏦ

ᴍᴀᴅᴇ ʙʏ: @CRACKERON 🧑‍💻
"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Mᴀᴋᴇ ᴍᴇ ᴛʜᴇ ᴀᴅᴍɪɴ ᴏғ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ɪғ ɪᴛ's ᴘʀɪᴠᴀᴛᴇ.
2. ᴍᴀᴋᴇ sᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴅᴏᴇs ɴᴏᴛ ᴄᴏɴᴛᴀɪɴs ᴄᴀᴍʀɪᴘs, ᴘᴏʀɴ ᴀɴᴅ ғᴀᴋᴇ ғɪʟᴇs.
3. Fᴏʀᴡᴀʀᴅ ᴛʜᴇ ʟᴀsᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴇ ᴡɪᴛʜ ϙᴜᴏᴛᴇs.
 I'ʟʟ ᴀᴅᴅ ᴀʟʟ ᴛʜᴇ ғɪʟᴇs ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴍʏ ᴅʙ."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Oɴʟʏ Aᴅᴍɪɴs ᴄᴀɴ ᴀᴅᴅ ᴀ ᴄᴏɴɴᴇᴄᴛɪᴏɴ.
2. Sᴇɴᴅ <ᴄᴏᴅᴇ>/ᴄᴏɴɴᴇᴄᴛ</ᴄᴏᴅᴇ> ғᴏʀ ᴄᴏɴɴᴇᴄᴛɪɴɢ ᴍᴇ ᴛᴏ ᴜʀ PM


<b>Cᴏᴍᴍᴀɴᴅ Aɴᴅ Usᴀɢᴇ:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>Nᴏᴛᴇ:</b>
Tʜɪs Mᴏᴅᴜʟᴇ Oɴʟʏ Wᴏʀᴋ Fᴏʀ ᴍʏ Aᴅᴍɪɴs

<b>Commands and Usage:</b>
• /logs - <code>Tᴏ Gᴇᴛ Tʜᴇ Rᴇsᴄᴇɴᴛ Eʀʀᴏʀs</code>
• /stats - <code>Tᴏ Gᴇᴛ Sᴛᴀᴛᴜs Oғ Fɪʟᴇs Iɴ *****</code>
• /delete - <code>Tᴏ Dᴇʟᴇᴛᴇ A Sᴘᴇᴄɪғɪᴄ Fɪʟᴇ Fʀᴏᴍ *****</code>
• /users - <code>Tᴏ Gᴇᴛ Lɪsᴛ Oғ Mʏ Usᴇʀs Aɴᴅ Iᴅs</code>
• /chats - <code>Tᴏ Gᴇᴛ Lɪsᴛ Oғ Tʜᴇ Mʏ Cʜᴀᴛs Aɴᴅ Iᴅs</code>
• /leave  - <code>Tᴏ Lᴇᴀᴠᴇ Fʀᴏᴍ Cʜᴀᴛ</code>
• /disable  -  <code>Dᴏ Dɪsᴀʙʟᴇ A Cʜᴀᴛ</code>
• /ban  - <code>Tᴏ Bᴀɴ A Usᴇʀ</code>
• /unban  - <code>Tᴏ UɴBᴀɴ A Usᴇʀ</code>
• /channel - <code>Gᴇᴛ Lɪsᴛ Oғ Tᴏᴛᴀʟ Cᴏɴɴᴇᴄᴛᴇᴅ Cʜᴀɴɴᴇʟs</code>
• /broadcast - <code>Tᴏ Bʀᴏᴀᴅᴄᴀsᴛ ᴀ Mᴇssᴀɢᴇ Tᴏ Aʟʟ Usᴇʀs</code>"""
    STATUS_TXT = """🗂️ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
👥 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
💌 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
⛽ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
🛢️ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup😍
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser🔥
ID - <code>{}</code>
Name - {}
"""
