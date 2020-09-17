from aiogram.dispatcher.filters.state import StatesGroup, State


class Game(StatesGroup):
    pre_stage1 = State()
    stage1 = State()
    pre_stage2 = State()
    stage2 = State()
    pre_stage3 = State()
    stage3 = State()
    pre_stage4 = State()
    stage4 = State()
    pre_stage5 = State()
    stage5 = State()

