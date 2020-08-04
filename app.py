from aiogram import executor
from load_all import bot


async def on_shutdown(dp):
    await bot.close()


if __name__ == '__main__':
    from handlers import dp

    executor.start_polling(dp, on_shutdown=on_shutdown)
