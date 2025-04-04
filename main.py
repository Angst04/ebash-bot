import asyncio
# import winloop

from aiogram import Bot, Dispatcher
from aiogram.types import Message, WebAppInfo
from aiogram.filters.state import StateFilter
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

import os
from dotenv import load_dotenv

# winloop.install()
load_dotenv()

TOKEN = os.getenv('TOKEN')
ADMINS = list(map(int, os.getenv('ADMINS', '').split(','))) if os.getenv('ADMINS') else []

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(StateFilter(None), Command("admin"))
async def cmd_admin(message: Message):
   if message.from_user.id in ADMINS:
      builder = InlineKeyboardBuilder()
      builder.row(InlineKeyboardButton(text='Админ-панель', url='https://ebash-studio.vercel.app/structure'))
      await message.answer(text='Страница администратора', reply_markup=builder.as_markup())
   else:
      await message.answer(text='У вас недостаточно прав для доступа')

@dp.message(StateFilter(None), Command("start"))
async def cmd_start(message: Message):
   builder = InlineKeyboardBuilder()
   builder.row(InlineKeyboardButton(text='Начать', web_app=WebAppInfo(url='https://ebash-tma.vercel.app/')))
   # builder.row(InlineKeyboardButton(text='Начать', web_app=WebAppInfo(url='https://shy-glasses-hunt.loca.lt')))
   
   await message.answer(text='Добро пожаловать в бота-помощника канала EBASH!', reply_markup=builder.as_markup())
   
async def main():
   print('Бот запущен')
   await bot.delete_webhook(drop_pending_updates=True)
   await dp.start_polling(bot)

if __name__ == "__main__":
   asyncio.run(main())