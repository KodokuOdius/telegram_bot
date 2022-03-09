from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                           KeyboardButton, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)

from config.bot import DP
from config.database import DB


class RegUser(StatesGroup):
    name = State()



@DP.message_handler(commands=['start'])
async def acho(event: types.Message):
    NameKey = (
        ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        .add(KeyboardButton("😁 Оставить"))
    )

    result = DB.request(f"select * from tg_user where user_id = {event.from_user.id}", "result")
    if result == 0:
        await event.answer(
            "Привет, вижу ты у меня впервые, давай пройдём маленькую регестрацию и я расскажу о себе.\n" +
            "Введи свой желаемый <b><i>никнейм</i></b>, который будет использоваться боте, или нажми на кнопку, " + 
            "чтобы оставить никнейм из Telegram",
            reply_markup=NameKey
        )

        await RegUser.name.set()

    else:
        user = DB.request(f"select * from tg_user where user_id = {event.from_user.id}", "fetchall")

        await event.answer(
            f"Привет, {user['nick_name']}\n" +
            "Готов сново поиграть? нажимай на кнопку)"
        )



@DP.message_handler(state=RegUser.name)
async def test(event: types.Message, state: FSMContext):
    if event.text == "😁 Оставить":
        DB.request(f"insert into tg_user (user_id, nick_name) values ({event.from_user.id}, '{event.from_user.full_name}')")
        
        await event.answer(
            "Отлично!\n" +
            "Я тебя запомнил)\n" +
            "Если хочешь посмотреть свой профиль вот команда /profile",
            reply_markup=ReplyKeyboardRemove()
        )
        
        await state.finish()
    
    name = event.text

    if len(name) > 64:
        await event.reply(
            r"Извини {{{(>_<)}}}\n" +
            "Максимум 64 символа)"
        )
    else:
        DB.request(f"insert into tg_user (user_id, nick_name) values ({event.from_user.id}, '{name}')")
        
        await event.answer(
            "Отлично!\n" +
            "Я тебя запомнил)\n" +
            "Если хочешь посмотреть свой профиль вот команда /profile",
            reply_markup=ReplyKeyboardRemove()
        )
        
        await state.finish()
        





@DP.message_handler()
async def qwerty(event: types.Message):
    await event.reply("Пустая ловушка")










if __name__ == '__main__':
    from aiogram import executor

    from config.admin import shutdown, starting

    executor.start_polling(
        DP, 
        on_startup=starting, 
        on_shutdown=shutdown
    )
