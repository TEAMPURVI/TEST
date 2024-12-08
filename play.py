buttons = [
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="⎙", callback_data=f"add_playlist {videoid}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
      [
            InlineKeyboardButton(
                text="⪻  -10s",
                callback_data=f"ADMIN 1|{chat_id}",
            ),
            InlineKeyboardButton(
                text="↻",
                callback_data=f"ADMIN Replay|{chat_id}"
            ),  
            InlineKeyboardButton(
                text="+10s  ⪼",
                callback_data=f"ADMIN 2|{chat_id}",
            ),
        ],
         [
            InlineKeyboardButton(
                text=_["⍟ ᴀᴅᴅ ᴍᴇ ⍟"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data="close",
            )
        ],
    ]
    return buttons
