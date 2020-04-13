import asyncio
from aiogram import Bot, Dispatcher, types, executor
from config import BOT_TOKEN, ADMIN_ID

# Запускаю поток, бота и диспатчер
loop = asyncio.get_event_loop()
bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, loop=loop)


# функция отправки сообщения админу о запуске бота
async def send_message_to_admin(dp):
    await bot.send_message(chat_id=ADMIN_ID, text='Бот запущен!')


# декоратор срабатывает по команде /start
@dp.message_handler(commands='start')
async def start_cmd_handler(message: types.Message):
    # Делаем клавиатуру из двух кнопок
    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)
    buttons = (
        (types.InlineKeyboardButton('Подробнее о проекте', callback_data='about')),
        (types.InlineKeyboardButton('Подписаться', callback_data='subscribe')),
    )
    keyboard_markup.row(*buttons)
    await bot.send_message(message.from_user.id,
                           text="Привет! \nТы на странице тестового бота! Подпишись или узнай больше",
                           reply_markup=keyboard_markup)


# декоратор срабатывает по callback_data = 'about'
@dp.callback_query_handler(text='about')
async def about_project(query: types.CallbackQuery):
    # выводим пользователю в строке состояния его выбор. Было бы логичнее выводить не callback_data, а текст
    await query.answer(f'Ты выбрал {query.data!r}')
    text = 'Отлично, сейчас я расскажу тебе, какой это замечательный тестовый бот! ' \
           'В нём ты можешь нажимать кнопки и переходить в разные меню. ' \
           'А в клавиатуру встроена кнопка \"На главную\"'
    await bot.send_message(query.from_user.id, text)  # Как добавить кнопку На главную ?


@dp.callback_query_handler(text='subscribe')
async def choose_subscribe(query: types.CallbackQuery):
    await query.answer(f'Ты выбрал {query.data!r}')
    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)
    buttons = (
        (types.InlineKeyboardButton('Тарифный план А', callback_data='subscribe_type1')),
        (types.InlineKeyboardButton('тарифный план Б', callback_data='subscribe_type2'))
    )
    keyboard_markup.row(*buttons)
    text = 'Ты решил подписаться. Отлично, выбери тарифный план и оформи подписку!'
    await bot.send_message(query.from_user.id, text=text, reply_markup=keyboard_markup)


# Два декоратора, срабатывают при любом из двух значений
@dp.callback_query_handler(text='subscribe_type1')
@dp.callback_query_handler(text='subscribe_type2')
async def pay_subscribe(query: types.CallbackQuery):
    await query.answer(f'Ты выбрал {query.data!r}')
    # кнопка оплаты, где в урл подставляется выбранный тип подписки
    keyboard_markup = types.InlineKeyboardMarkup(row_width=1)
    buttons = (
        (types.InlineKeyboardButton('Оплатить', callback_data='subscribe_pay',
                                    url=f'https://example.com?subscribe_type={query.data}')),
    )
    keyboard_markup.row(*buttons)
    text = f'Супер! Ты выбрал {query.data}, нажми на кнопку оплатить и получи доступ!'
    # как вывести не query.data, а текст предыдущей кнопки?
    await bot.send_message(query.from_user.id, text=text, reply_markup=keyboard_markup)


# Собственно вопросы:
# 1. Как во все меню добавить клавиатурную кнопку На главную?
# 2. Как редактировать кол-во кнопок в строке?
# 3. Можно ли как то реализовать универсальную кнопку назад в которой будет подставлятьс переменная из предыдущего меню?
# 4. Откуда в моём боте три клавиатурные кнопки: Button1, Botton2, Button3 !?

executor.start_polling(dp, on_startup=send_message_to_admin)