from bot import bot, dp
from aiogram.types import Message
from config import admin_id, users


async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text='Бот запущен')

# Страница
#driver = webdriver.Chrome()
#driver.get('https://vk.com/rick.n.morty')

