import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
import requests as requests


load_dotenv()

API_TOKEN = os.getenv("TG_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



CAT: str = "ко(т|тик|шара|тище|шечка|шачий|шка)$|ки(са|суля|сонька|ра)$"
@dp.message_handler(regexp = CAT)
async def send_cat_sticker (message: types.Message):
    await message.answer("Смотри какой котик")
    await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEIsB5kRA6Is4ILqz88s3NPTeILlnUBnwAC7x8AAnEy4UhjcFdbhYZxty8E")
@dp.message_handler()
async def send_dog (message: types.Message):
    media_url = requests.get('https://random.dog/woof.json').json().get('url')
    if media_url.lower().endswith(('jpg', 'jpeg', 'png')):
        await bot.send_photo(
            chat_id=message.from_user.id,
            photo=media_url
        )
    elif media_url.lower().endswith(('mp4', 'gif')):
        await bot.send_video(
            chat_id=message.from_user.id,
            video=media_url
        )
    else:
        await message.answer(text='woofps, get try again')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
