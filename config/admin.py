from aiogram import Dispatcher, types
from .settings import admins


async def starting(dp: Dispatcher):
    for admin in admins:
        await dp.bot.send_message(
            chat_id=admin,
            text='Бот начал работу'
        )
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Начало работы')
    ])


async def shutdown(dp: Dispatcher):
    try:
        for admin in admins:
            await dp.bot.send_message(
                chat_id=admin,
                text='Бот ушёл на тех.перерыв',
            )
    except Exception:
        pass
    await dp.storage.close()
    await dp.storage.wait_closed()
