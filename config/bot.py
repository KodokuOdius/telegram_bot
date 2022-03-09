from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from . import settings

_bot = Bot(
    token=settings.token,
    parse_mode=types.ParseMode.HTML
)

_storage = MemoryStorage()


DP = Dispatcher(
    bot=_bot, 
    storage=_storage
)


