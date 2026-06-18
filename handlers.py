from aiogram import Router, F, types
from keyboards import main_keyboard, gender_keyboard, woman_training_keyboard, man_training_keyboard

main_router = Router()


@main_router.message(F.text == "/start")
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я бот для тренировок. С чего начнём?", reply_markup=main_keyboard())


@main_router.message(F.text == "/help")
async def cmd_help(message: types.Message):
    await message.answer("Я помогу выбрать тренировку и рассчитать количество подходов по возрасту и весу.")


@main_router.callback_query(F.data == "back_main")
async def back_main(callback: types.CallbackQuery):
    await callback.message.edit_text("Главное меню:", reply_markup=main_keyboard())
    await callback.answer()


@main_router.callback_query(F.data == "trainings")
async def trainings(callback: types.CallbackQuery):
    await callback.message.edit_text("Выберите раздел тренировок:", reply_markup=gender_keyboard())
    await callback.answer()


@main_router.callback_query(F.data == "trainings_woman")
async def trainings_woman(callback: types.CallbackQuery):
    await callback.message.edit_text("Тренировки для женщин:", reply_markup=woman_training_keyboard())
    await callback.answer()


@main_router.callback_query(F.data == "trainings_man")
async def trainings_man(callback: types.CallbackQuery):
    await callback.message.edit_text("Тренировки для мужчин:", reply_markup=man_training_keyboard())
    await callback.answer()


@main_router.callback_query(F.data == "nutrition")
async def nutrition(callback: types.CallbackQuery):
    await callback.message.answer(
        "🍎 Базово: пейте воду, не пропускайте нормальную еду и подбирайте питание под цель. "
    )
    await callback.answer()
