from aiogram.types import Message
from aiogram.dispatcher.filters import CommandStart
from keyboards import transition_menu
from state import Game
from load_all import dp

number_stage = 1
# admin_id = 382505606
admin_id = 428388372


@dp.message_handler(user_id=admin_id, commands=["stage"])
async def count_user(message: Message):
    await message.answer(f'Аня находится на {number_stage} этапе')


@dp.message_handler(state=Game.transition)
async def transition(message: Message):
    global number_stage
    await message.answer('Поздравляю. Нажми, когда будешь готова', reply_markup=transition_menu)
    if number_stage == 2:
        await Game.pre_stage2.set()
    elif number_stage == 3:
        await Game.pre_stage3.set()
    elif number_stage == 4:
        await Game.pre_stage4.set()
    elif number_stage == 5:
        await Game.pre_stage5.set()
    elif number_stage == 6:
        await Game.pre_stage6.set()
    elif number_stage == 7:
        await Game.pre_stage7.set()


@dp.message_handler(CommandStart())
async def start(message: Message):
    await message.answer('Привет, это квест! *** текст будет потом ***.\nПравила просты: приходит загадка, '
                         'в ответ нужно написать место, которое она описывает.')
    await message.answer('Когда будешь готова, нажми кнопку снизу', reply_markup=transition_menu)
    await Game.pre_stage1.set()


@dp.message_handler(state=Game.pre_stage1)
async def pre_stage1(message: Message):
    await message.answer('Первая загадка:\nМесто, которое подарило тебе нас')
    await Game.stage1.set()


@dp.message_handler(state=Game.stage1)
async def stage1(message: Message):
    global number_stage
    if message.text.lower() != 'школа':
        await message.answer('Ответ не верен')
        await Game.stage1.set()
    else:
        number_stage += 1
        await Game.transition.set()


@dp.message_handler(state=Game.pre_stage2)
async def pre_stage2(message: Message):
    await message.answer('Место нашей шальной молодости, где мы прятались в кустах и убегали от лишних глаз')
    await Game.stage2.set()


@dp.message_handler(state=Game.stage2)
async def stage2(message: Message):
    global number_stage
    if message.text.lower() != "мост у труда":
        await message.answer('Ответ не верен')
        await Game.stage2.set()
    else:
        number_stage += 1
        await Game.transition.set()


@dp.message_handler(state=Game.pre_stage3)
async def pre_stage3(message: Message):
    await message.answer('Место, в котором люди влюбляются в наш город двух N')
    await Game.stage3.set()


@dp.message_handler(state=Game.stage3)
async def stage3(message: Message):
    global number_stage
    if message.text.lower() != "памятник Чкалову":
        await message.answer('Ответ не верен')
        await Game.stage3.set()
    else:
        number_stage += 1
        await Game.transition.set()


@dp.message_handler(state=Game.pre_stage4)
async def pre_stage4(message: Message):
    await message.answer('Un pezzo di Italia a Nižnij Novgorod')
    await Game.stage4.set()


@dp.message_handler(state=Game.stage4)
async def stage4(message: Message):
    global number_stage
    if message.text.lower() != "папи":
        await message.answer('Ответ не верен')
        await Game.stage4.set()
    else:
        number_stage += 1
        await Game.transition.set()


@dp.message_handler(state=Game.pre_stage5)
async def pre_stage5(message: Message):
    await message.answer('Место, где твоя попка привлекала взгляды мужчин')
    await Game.stage5.set()


@dp.message_handler(state=Game.stage5)
async def stage5(message: Message):
    global number_stage
    if message.text.lower() != "режим":
        await message.answer('Ответ не верен')
        await Game.stage5.set()
    else:
        number_stage += 1
        await Game.transition.set()


@dp.message_handler(state=Game.pre_stage6)
async def pre_stage6(message: Message):
    await message.answer('Место, которое вывело твою жизнь на новый этап')
    await Game.stage6.set()


@dp.message_handler(state=Game.stage6)
async def stage6(message: Message):
    global number_stage
    if message.text.lower() != "пакгаузы":
        await message.answer('Ответ не верен')
        await Game.stage6.set()
    else:
        number_stage += 1
        await Game.transition.set()


@dp.message_handler(state=Game.pre_stage7)
async def pre_stage7(message: Message):
    await message.answer('Финальная точка, где тебя ждет сюрприз. Завяжи глаза 👀')
    await Game.stage7.set()


@dp.message_handler(state=Game.stage7)
async def stage7(message: Message):
    global number_stage
    if message.text.lower() != "кафе опера":
        await message.answer('Ответ не верен')
        await Game.stage7.set()
    else:
        await Game.end.set()
