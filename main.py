import asyncio
from crypto_bot import bot_init

if __name__ == "__main__":
    bot, dp = bot_init.start_crypto_bot()
    from crypto_bot.bot_view import CryptoBot
    cp = CryptoBot(bot, dp)
    asyncio.run(cp.handlers())


    # client = bot_init.start_private_bot()
    pass