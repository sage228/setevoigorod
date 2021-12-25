from config import bot_token
#import logging
import asyncio
from aiogram import Bot, Dispatcher, executor, types


# Инициализируем бота
loop = asyncio.get_event_loop()
bot = Bot(bot_token)
dp = Dispatcher(bot, loop=loop)

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)
    print(message.text)
    # driver = webdriver.Chrome('C:\нужное\Python\BOT 2.0\chromedriver.exe')
    # driver.get('https://sgo.rso23.ru')
    # await message.answer(driver.find_element_by_xpath(
    #     '/ html/body/div[2]/div[1]/div/div/span').text)
# запускаем лонг полинг
if __name__ == '__main__':
    from handlers import dp, send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin)
