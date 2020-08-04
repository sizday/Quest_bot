from aiogram.types import Message
from aiogram.dispatcher.filters import Command, Text, CommandStart
from keyboards import transition_menu
from state import Game
from load_all import bot, dp

number_stage = 1


@dp.message_handler(state=Game.transition)
async def transition(message: Message):
    global number_stage
    await message.answer('Нажми, когда будешь готова', reply_markup=transition_menu)
    if number_stage == 2:
        await message.answer('Место нашей шальной молодости, где мы прятались в кустах и убегали от лишних глаз')
        await Game.stage2
    """
    elif number_stage == 3:
        await message.answer('Нажми, когда будешь готова')
        await Game.stage3
    elif number_stage == 4:
        await message.answer('Нажми, когда будешь готова')
        await Game.stage4
    elif number_stage == 5:
        await message.answer('Нажми, когда будешь готова')
        await Game.stage5
    """


@dp.message_handler(CommandStart())
async def start(message: Message):
    await message.answer('Привет, это квест! *** текст будет потом ***. Правила просты: приходит загадка, '
                         'в ответ нужно написать место, которое она описывает.')
    await message.answer('\bПервая загадка\b\nМесто, которое подарило тебе нас')
    await Game.stage1.set()


@dp.message_handler(state=Game.stage1)
async def stage1(message: Message):
    global number_stage
    while True:
        if message.text.lower() == 'школа':
            await message.answer('Поздравляю')
            number_stage += 1
            break
        else:
            await message.answer('Ответ не верен')
    await Game.transition.set()


@dp.message_handler(state=Game.stage2)
async def stage2(message: Message):
    global number_stage
    while True:
        if message.text.lower() == 'школа':
            await message.answer('Поздравляю')
            number_stage += 1
            break
        else:
            await message.answer('Ответ не верен')
    await Game.transition.set()

