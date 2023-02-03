import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class script(object):
    START_TXT = """<i><b>🎃 Helo {}, I'm <a href=https://telegram.me/{}>{}</a></i></b> \n\n<i><b>🎗I Can Provide You Any Movies, Web-Series, Anime, K-Dramas, Animation, etc.,</i></b>"""
    HELP_TXT = """<b>🥁 </b><b><u>How To Download Any Movie, Series, Anime etc., For Free???</u></b> \n\n<b>🎗Group [01]: </b><b>https://t.me/+WzsvFY3qXa9kZGVl</b> \n\n<b>🎗Group</b> <b>[02]: </b><b>https://t.me/+EdJU1Hqk1N80ZWQ1</b> \n\n<b>🔆</b> <b>Join Any Of The Above Groups</b>👆"""
    ABOUT_TXT = """<i><u>🧶 </u></i><i><u><b>Follow These Steps To Connect Me To Your Group</b>👇</u>

1. Click on This [</i><a href="http://telegram.me/heroriderbot?startgroup=true"><i>Blue Text</i></a><i>]
2. Select Your Group
3. Make Me Admin in Your Group</i>"""    
    SOURCE_TXT = """<i><b><u>AutoFilter + UrlShortner Bot</u></b>

🔅 Want An </i><i><b>'AutoFilter + UrlShortner Bot'</b> Like Me For Your Group &amp; Earn Money Using It?

📲 </i><i><b>Contact »</b> </i><i>@DR_STARNGE</i>"""    
    MANUELFILTER_TXT = """Help: <b>FILTERS »</b>

» <b>Filter is A Feature Where Users can Set Automated Reply to a Specific Word</b>

<b>Important Notes:</b>
1.<i> I Have To Be Admin </i>
2.<i> Only admins can add Filters in Chat</i>
3.<i> Buttons have a limit of 64 Characters</i>

<b>Commands and Usage:</b>
• <i> /filter - Add a Filter</i>
• <i> /filters - List of All Filters</i>
• <i> /del - Delete a Filter</i>
• <i> /delall - Delete All Filters</i> """
    BUTTON_TXT = """Help: <b>BUTTONS »</b>

» Supports both url and alert inline buttons.

<b>NOTE:</b>
1. <i>Telegram will not allows you to send buttons without any content, so content is mandatory.</i>
2. <i>Supports buttons with any telegram media type</i>
3. <i>Buttons should be properly parsed as markdown format</i>

<b>URL Buttons:</b>
<code>[Button Text](buttonurl:https://t.me/HeroRiderbot)</code>

<b>Alert Buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>AUTO FILTER »</b>

Add Me In Your Group as Admin & I Will Provide Any Movie, Series, Animation etc.,"""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. <i>Only Admins Can Add Connection</i>
2. <i>Send <code>/connect</code> To Connect Me to Your PM</i>

<b>Commands and Usage:</b>
•<i> /connect  - Connect a Chat to your PM</i>
•<i> /disconnect  - Disconnect from a Chat</i>
•<i> /connections - List Of All Connections</i>"""
    EXTRAMOD_TXT = """Help: <b>Extra Features of Me »</b>

<b>Commands and Usage:</b>
•<i> /id - Get ID Of A User</i>
•<i> /imdb  - Get Movie/Series Info from IMDb</i>"""
    ADMIN_TXT = """Help: <b>ADMIN MODS »</b>

<b>NOTE:</b>
This Works Only For Admins!

<b>Commands and Usage:</b>
•<i> /stats - Get Status of DataBase</i>
•<i> /delete - Delete A File</i>
•<i> /users - List of My Users </i>
•<i> /chats - Get List Of My Chats </i>
•<i> /leave  - Leave from a chat</i>
•<i> /disable  - Disable a Chat</i>
•<i> /ban  - Ban a User</i>
•<i> /unban  - Unban a User</i>
•<i> /channel - List of All Connected Channels</i>
•<i> /broadcast - Broadcast a Message to All Users</i>"""
    STATUS_TXT = """<b>🎗️ My Statistics 📲</b>

◉ <b>Total Files :</b> {}
◉ <b>Total Users :</b> {}
◉ <b>Total Chats :</b> {}
◉ <b>Used Storage :</b> {} 
◉ <b>Free Storage :</b> {}"""

    LOG_TEXT_G = """<b>#NewGroup</b>
<b>Group »</b> {} (<code>{}</code>)
<b>Total Members »</b> <code>{}</code>
<b>Added By »</b> {}
"""
    LOG_TEXT_P = """<b>#NewUser</b>
◉ ID - <code>{}</code>
◉ Name - {}
"""
