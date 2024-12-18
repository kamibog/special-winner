from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Рассчитать'),
     KeyboardButton(text='Информация'),
     KeyboardButton(text='Купить')]
],
    resize_keyboard=True)

kb_inline = InlineKeyboardMarkup()
button3 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button4 = InlineKeyboardButton(text='Формулы расчета', callback_data='formulas')
kb_inline.add(button3)
kb_inline.add(button4)

product_buttons = [
    InlineKeyboardButton(text='Product1', callback_data='product_buying'),
    InlineKeyboardButton(text='Product2', callback_data='product_buying'),
    InlineKeyboardButton(text='Product3', callback_data='product_buying'),
    InlineKeyboardButton(text='Product4', callback_data='product_buying')
]
kb_inline_products = InlineKeyboardMarkup(row_width=2).add(*product_buttons)


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=kb)


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer("Выберите опцию", reply_markup=kb_inline)


@dp.message_handler(text='Купить')
async def get_buying_list(message: types.Message):
    products = [
        (1, "Product1", "описание 1", 100, "P1.png"),
        (2, "Product2", "описание 2", 200, "P2.png"),
        (3, "Product3", "описание 3", 300, "P3.png"),
        (4, "Product4", "описание 4", 400, "P4.png"),
    ]

    for product in products:
        product_id, name, description, price, image = product
        await message.answer(f'Название: {name} | Описание: {description} | Цена: {price}')
        await bot.send_photo(message.chat.id, photo=open(image, 'rb'))

    await message.answer("Выберите продукт для покупки:", reply_markup=kb_inline_products)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


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


@dp.message_handler()
async def all_message(message):
    print("Введите команду /start, чтобы начать общение.")
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
