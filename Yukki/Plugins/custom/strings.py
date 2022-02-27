from config import ASSISTANT_PREFIX
from Yukki import BOT_NAME, BOT_USERNAME
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

START_TEXT = f"""
✨ **Hello MENTION !**

**You can use [{BOT_NAME}](https://t.me/{BOT_USERNAME}) to play Music or Videos in your Group Video Chat.**

💡 **Find out all the Bot's commands and how they work by clicking on the ➤ 📚 Commands button**
"""

COMMANDS_TEXT = f"""
✨ **Hello MENTION !**

**Click on the buttons below to know my commands.**
"""

START_BUTTON_GROUP = InlineKeyboardMarkup(
    [   
        [
            InlineKeyboardButton(
                text="💠 Commands and Menu", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="🔧 Settings", callback_data="settingm"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="📣 Updates Channel", url="https://t.me/TechZBots"
            ),
            InlineKeyboardButton(
                text="💬 Support Group", url="https://t.me/TechZBots_Support"
            ),                       
        ],        
    ]
)

START_BUTTON_PRIVATE = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="➕ Add me to Group ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
            ),            
        ],
        [   
            InlineKeyboardButton(
                text=💠 Commands and Menu", callback_data="command_menu"
            ),                       
        ],
        [
            InlineKeyboardButton(
                text="📣 Updates Channel", url="https://t.me/TechZBots"
            ),
            InlineKeyboardButton(
                text="💬 Support Group", url="https://t.me/TechZBots_Support"
            ),                       
        ],        
    ]
)

BASIC_TEXT = """
📍 **Basic Commands:**

>> /start - start the bot
>> /help - get help message
>> /spotify - play songs from spotify
>> /resso - play songs from resso
>> /lyrics - get lyrics of song
>> /playlist - play your playlist
>> /song - download a song as music or video
>> /settings - settings of the group
>> /theme - set theme for your group
>> /queue - get queued song
"""

BASIC_BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="↪️ Back", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="🔄 Close", callback_data="close_btn"
            ),            
        ],                        
    ]
)

OWNER_TEXT = """
📍 **This Bot Is Handled And Managed By :**

>> [Pratheek](https://t.me/Pratheek06)
"""

BASIC_BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="↪️ Back", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="🔄 Close", callback_data="close_btn"
            ),            
        ],                        
    ]
)

COMMAND_MENU_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="📖 Basic Commands", callback_data="basic_cmd"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="💬 Report Any Bugs Here", callback_data="owner_cmd"
            ),
        ],
        [
            InlineKeyboardButton(
                text="↪️ Back", callback_data="open_start_menu"
            ),
            InlineKeyboardButton(
                text="🔄 Close", callback_data="close_btn"
            ),            
        ],                        
    ]
)
