from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum, {message.from_user.full_name}!")
@dp.message_handler(commands='behzod')
async def test(message:types.Message):
    await message.answer("Behzod buyrugini berdiz!")
@dp.message_handler(content_types='text')
async def test(message:types.Message):
    key = message.text
    import wikipedia
    wikipedia.set_lang('uz')
    result = ''
    try:
        result = wikipedia.summary(key)
    except wikipedia.exceptions.DisambiguationError:
        result = 'Bu kalit boyicha malumot kop.Iltimos batafsil kiriting'
    except wikipedia.exceptions.PageError:
        result ="Malumot topilmadi!"
    await message.answer(result)
