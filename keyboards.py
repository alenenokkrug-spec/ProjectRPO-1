from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎯 Цель визита", callback_data="set_info")],
        [InlineKeyboardButton(text="💪 Тренировки", callback_data="trainings")],
        [InlineKeyboardButton(text="🍎 Питание", callback_data="nutrition")],
    ])


def goals_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🏋️ Набор массы", callback_data="goal_mass")],
        [InlineKeyboardButton(text="🔥 Похудение", callback_data="goal_weight_loss")],
        [InlineKeyboardButton(text="💪 Поддержание формы", callback_data="goal_maintain")],
    ])


def gender_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💪 Тренировки для женщин", callback_data="trainings_woman")],
        [InlineKeyboardButton(text="💪 Тренировки для мужчин", callback_data="trainings_man")],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_main")],
    ])


def woman_training_keyboard() -> InlineKeyboardMarkup:
    buttons = [
        ("Разминка", "exercise_warmup"),
        ("Ноги", "exercise_legs"),
        ("Ягодицы", "exercise_glutes"),
        ("Спина", "exercise_back"),
        ("Грудь", "exercise_chest"),
        ("Руки", "exercise_arms"),
        ("Кардио", "exercise_cardio"),
        ("Кор", "exercise_core"),
        ("Пресс", "exercise_abs"),
        ("Фулл-боди", "exercise_fullbody"),
        ("Заминка", "exercise_cooldown"),
    ]
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=text, callback_data=data)] for text, data in buttons
    ] + [[InlineKeyboardButton(text="⬅️ Назад", callback_data="trainings")]])


def man_training_keyboard() -> InlineKeyboardMarkup:
    buttons = [
        ("Разминка", "exercise_warmup"),
        ("Бицепс", "exercise_biceps"),
        ("Спина", "exercise_back"),
        ("Трапеция", "exercise_trapeze"),
        ("Задняя дельта", "exercise_rear_delta"),
        ("Плечи", "exercise_shoulders"),
        ("Трицепс", "exercise_triceps"),
        ("Ноги", "exercise_legs"),
        ("Грудь", "exercise_chest"),
        ("Фулл-боди", "exercise_fullbody"),
        ("Заминка", "exercise_cooldown"),
    ]
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=text, callback_data=data)] for text, data in buttons
    ] + [[InlineKeyboardButton(text="⬅️ Назад", callback_data="trainings")]])
