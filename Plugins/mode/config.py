# Telethon kütüphanesi config gereksinimleri.

from telethon import TelegramClient

# Telegram Client (Telethon)
API_ID = 28496124
API_HASH = "dcadf01f9a76befff2eccc932c6eabd1"
bot_token = "5946035154:AAHV9lOQKz4VL3iNhwp4ovsEWR9GKM6ux34"

# test projesi.. 
noadmin = "**🚫 Sen admin değilsin\n\n Yöneticilerle görüşebilirsin.**"
nomesaj = "**Etiket işlemine başlamam için bana bir metin ver**"
#

Maho = TelegramClient('Maho', API_ID, API_HASH).start(bot_token=bot_token)
