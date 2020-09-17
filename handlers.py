from aiogram.types import Message
from aiogram.dispatcher.filters import CommandStart
from keyboards import transition_menu
from state import Game
from load_all import dp
from sticker_id import positive_sticker, negative_sticker
import random

number_stage = 1
admin_id = 382505606


@dp.message_handler(user_id=admin_id, commands=["stage"])
async def count_user(message: Message):
    await message.answer(f'Аня находится на {number_stage} этапе')


@dp.message_handler(CommandStart())
async def start(message: Message):
    global number_stage
    number_stage = 1
    await message.answer('Привет, Анют! Мы, твои подруги, знаем, что ты очень любишь сюрпризы, загадки и головоломки. '
                         'Поэтому мы придумали для тебя мини-квест, который тебе предстоит пройти на большом белом '
                         'лимузине! Кстати, он уже ждет тебя. Спускайся вниз!  Для того, чтобы собрать нас всех вместе,'
                         ' тебе нужно будет хорошо подумать и вспомнить самые яркие моменты жизни в городе двух N. '
                         'Чтобы узнать , в какое место тебе нужно будет ехать, ты должна разгадать загадку.')
    await message.answer('Когда будешь готова, нажми кнопку снизу', reply_markup=transition_menu)
    await Game.pre_stage1.set()


@dp.message_handler(state=Game.pre_stage1)
async def pre_stage1(message: Message):
    await message.answer('Первая загадка:\nМесто, которое подарило тебе нас')
    await Game.stage1.set()


@dp.message_handler(state=Game.stage1)
async def stage1(message: Message):
    global number_stage
    if message.text.lower() != 'школа' and message.text.lower() != 'лицей':
        await message.answer_sticker(negative_sticker.get(random.randint(0, 9)))
        await message.answer('Ответ не верен')
        await Game.stage1.set()
    else:
        number_stage += 1
        await message.answer_sticker(positive_sticker.get(2))
        await message.answer('Молодец! Отправляйся по адресу ул. красных зорь 14а, к магазину Пятерочка.\n'
                             'Нажми, когда будешь на месте.', reply_markup=transition_menu)
        await Game.pre_stage2.set()


@dp.message_handler(state=Game.pre_stage2)
async def pre_stage2(message: Message):
    await message.answer('Вторая загадка: место, где твоя попка привлекла взгляды мужчин')
    await Game.stage2.set()


@dp.message_handler(state=Game.stage2)
async def stage2(message: Message):
    global number_stage
    if message.text.lower() != "режим" and message.text.lower() != "спортклуб режим":
        await message.answer_sticker(negative_sticker.get(random.randint(0, 9)))
        await message.answer('Ответ не верен')
        await Game.stage2.set()
    else:
        number_stage += 1
        await message.answer_sticker(positive_sticker.get(3))
        await message.answer('Отлично! Адрес места назначения проспект Героев 72А, парковка у Евроспара.\n'
                             'Нажми, когда будешь на месте', reply_markup=transition_menu)
        await Game.pre_stage3.set()


@dp.message_handler(state=Game.pre_stage3)
async def pre_stage3(message: Message):
    await message.answer('Третья загадка: место нашей шальной молодости, где мы прятались в кустах и убегали от '
                         'лишних глаз')
    await Game.stage3.set()


@dp.message_handler(state=Game.stage3)
async def stage3(message: Message):
    global number_stage
    if message.text.lower() not in ['сормовский парк', 'стадион труд', 'труд']:
        await message.answer_sticker(negative_sticker.get(random.randint(0, 9)))
        await message.answer('Ответ не верен')
        await Game.stage3.set()
    else:
        number_stage += 1
        await message.answer_sticker(positive_sticker.get(4))
        await message.answer('Молодец! Отправляйся за следующей подружкой на  Бульвар Юбилейный, 30, стадион «Труд.\n'
                             'Нажми, когда будешь на месте', reply_markup=transition_menu)
        await Game.pre_stage4.set()


@dp.message_handler(state=Game.pre_stage4)
async def pre_stage4(message: Message):
    await message.answer('Четвертая загадка: Un pezzo di Italia a Nižnij Novgorod')
    await Game.stage4.set()


@dp.message_handler(state=Game.stage4)
async def stage4(message: Message):
    global number_stage
    if message.text.lower() not in ['papi', 'ресторан papi', 'кафе papi']:
        await message.answer_sticker(negative_sticker.get(random.randint(0, 9)))
        await message.answer('Ответ не верен')
        await Game.stage4.set()
    else:
        number_stage += 1
        await message.answer_sticker(positive_sticker.get(5))
        await message.answer('Perfettamente! Езжай по адресу ул. Рождественская, 37\n'
                             'Нажми, когда будешь на месте', reply_markup=transition_menu)
        await Game.pre_stage5.set()


@dp.message_handler(state=Game.pre_stage5)
async def pre_stage5(message: Message):
    await message.answer('Пятая загадка: место, которое вывело твою жизнь на новый этап.')
    await Game.stage5.set()


@dp.message_handler(state=Game.stage5)
async def stage5(message: Message):
    global number_stage
    if message.text.lower() != "пакгаузы":
        await message.answer_sticker(negative_sticker.get(random.randint(0, 9)))
        await message.answer('Ответ не верен')
        await Game.stage5.set()
    else:
        number_stage += 1
        await message.answer_sticker(positive_sticker.get(6))
        await message.answer('Поздравляем! Осталась последняя локация! Езжай на мыс Стрелка!')
