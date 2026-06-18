from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards import goals_keyboard, main_keyboard
from user_data import UserProfile, users, calculate_sets

info_router = Router()

GOAL_NAMES = {
    "goal_mass": "Набор массы",
    "goal_weight_loss": "Похудение",
    "goal_maintain": "Поддержание формы",
}


class VisitInfo(StatesGroup):
    waiting_for_goal = State()
    waiting_for_name = State()
    waiting_for_age = State()
    waiting_for_weight = State()


@info_router.callback_query(F.data == "set_info")
async def set_info_start(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(VisitInfo.waiting_for_goal)
    await callback.message.edit_text("Выберите цель визита:", reply_markup=goals_keyboard())
    await callback.answer()


@info_router.callback_query(VisitInfo.waiting_for_goal, F.data.in_(GOAL_NAMES.keys()))
async def process_goal(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(goal=GOAL_NAMES[callback.data])
    await state.set_state(VisitInfo.waiting_for_name)
    await callback.message.answer("Введите имя:")
    await callback.answer()


@info_router.message(VisitInfo.waiting_for_name)
async def process_name(message: types.Message, state: FSMContext):
    name = message.text.strip()
    if len(name) < 2:
        await message.answer("Имя слишком короткое. Введите имя ещё раз:")
        return
    await state.update_data(name=name)
    await state.set_state(VisitInfo.waiting_for_age)
    await message.answer("Введите возраст числом:")


@info_router.message(VisitInfo.waiting_for_age)
async def process_age(message: types.Message, state: FSMContext):
    try:
        age = int(message.text.strip())
    except ValueError:
        await message.answer("Возраст нужно ввести числом. Например: 18")
        return

    if age < 7 or age > 100:
        await message.answer("Введите реальный возраст от 7 до 100:")
        return

    await state.update_data(age=age)
    await state.set_state(VisitInfo.waiting_for_weight)
    await message.answer("Введите вес в кг. Например: 55 или 55.5")


@info_router.message(VisitInfo.waiting_for_weight)
async def process_weight(message: types.Message, state: FSMContext):
    raw_weight = message.text.strip().replace(",", ".")
    try:
        weight = float(raw_weight)
    except ValueError:
        await message.answer("Вес нужно ввести числом. Например: 55")
        return

    if weight < 20 or weight > 250:
        await message.answer("Введите реальный вес от 20 до 250 кг:")
        return

    data = await state.get_data()
    profile = UserProfile(
        name=data["name"],
        age=data["age"],
        weight=weight,
        goal=data["goal"],
    )
    users[message.from_user.id] = profile
    await state.clear()

    sets = calculate_sets(profile.age, profile.weight)
    await message.answer(
        f"Готово ✅\n\n"
        f"Имя: {profile.name}\n"
        f"Возраст: {profile.age}\n"
        f"Вес: {profile.weight:g} кг\n"
        f"Цель: {profile.goal}\n\n"
        f"Теперь в упражнениях будет показываться подходящее количество подходов: {sets}",
        reply_markup=main_keyboard(),
    )