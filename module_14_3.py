from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage= MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton( text = 'Расчитать')
button2 = KeyboardButton( text = 'Информация')
kb.add(button1, button2)

kb1 = InlineKeyboardMarkup()
button3 = InlineKeyboardButton(text='Product1', callback_data='product_buying')
button4 = InlineKeyboardButton(text='Product2', callback_data='product_buying')
button5 = InlineKeyboardButton(text='Product3', callback_data='product_buying')
button6 = InlineKeyboardButton(text='Product4', callback_data='product_buying')
kb1.add(button3, button4, button5, button6)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()



@dp.message_handler(commands= ['start'])
async def start(message):
    await message.answer('Привет! Выберите опцию', reply_markup=kb)

@dp.message_handler(text='Купить')
async def get_buying_list(message: types.Message):
    for i in range(1, 5):
        product_name = f'Название: Product{i}'
        description = f'Описание: описание {i}'
        price = f'Цена: {i * 100}'
        if i == 1:
            await message.answer_photo(
                photo="https://daily-motor.ru/wp-content/uploads/2022/04/9cef02fc84b44b545de632dda897d7d4-flying-car-weird-cars.jpg")
        if i == 2:
            await message.answer_photo(
                photo="https://cdn.forbes.ru/files/c/1082x727/photo_galleries/mercedes-benz_g_63_amg_w_463_3._facelift_-_frontansicht_7._august_2012_stuttgart.jpg__1582289638__61631.webp")
        if i == 3:
            await message.answer_photo(
                photo="https://masterpiecer-images.s3.yandex.net/3dcff7597d2311eebb2eb646b2a0ffc1:upscaled")
        if i == 4:
            await message.answer_photo(
                photo="https://habrastorage.org/getpro/habr/upload_files/741/73b/ac4/74173bac4ae562f46fd359b5ac2d2c43.jpg")
        await message.answer(f'{product_name} | {description} | {price}')

    await message.answer('Выберите продукт для покупки:', reply_markup=kb1)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)