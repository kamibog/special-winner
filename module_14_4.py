from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from crud_functions import initiate_db, get_all_products

api = "7822886140:AAE8ywqcQOXunJRMZTNTDxbZ3UwzN-pUC9M"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
buy = KeyboardButton(text='Купить')
kb.add(button)
kb.add(button2)
kb.add(buy)

kb_inline = InlineKeyboardMarkup()
button3 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button4 = InlineKeyboardButton(text='Формулы расчета', callback_data='formulas')
kb_inline.add(button3)
kb_inline.add(button4)

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=kb)

@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer("Выберите опцию", reply_markup=kb_inline)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer("10 х вес(кг) + 6.25 х рост(см)-5 х возвраст(г) +5")
    await call.answer()

@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer("Введите свой возраст: ")
    await UserState.age.set()
    await call.answer()

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост: ")
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес: ")
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)

    data = await state.get_data()
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])

    bmr = 10 * weight + 6.25 * growth - 5 * age + 5

    await message.answer(f"Ваша норма калорий: {bmr} ккал в день.")
    await state.finish()

@dp.message_handler(text='Купить')
async def get_buying_list(message: types.Message):
    products = get_all_products()
    product_list = ""
    for idx, (title, description, price) in enumerate(products, start=1):
        product_list += f"Название: {title} | Описание: {description} | Цена: {price}\n"
        await bot.send_photo(message.chat.id, photo=open(f'P{idx}.png', 'rb'))

    await message.answer(product_list)
    await message.answer("Выберите продукт для покупки:", reply_markup=kb_inline)

if __name__ == "__main__":
    initiate_db()
    executor.start_polling(dp, skip_updates=True)
