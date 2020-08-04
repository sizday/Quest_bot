from aiogram.dispatcher.filters.state import StatesGroup, State


class Game(StatesGroup):
    transition = State()
    stage1 = State()
    stage2 = State()
    stage3 = State()
    stage4 = State()
    stage5 = State()
    end = State()
