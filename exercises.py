from pathlib import Path
from aiogram import Router, F, types
from aiogram.types import FSInputFile
from user_data import get_user_sets

exercise_router = Router()
GIF_DIR = Path(__file__).parent / "gifs"

EXERCISES = {
    "exercise_warmup": {
        "title": "Разминка",
        "text": "Суставная разминка, лёгкие наклоны, круговые движения руками и ногами. Цель — подготовить тело к нагрузке.",
        "gif": "warmup.gif",
    },
    "exercise_legs": {
        "title": "Ноги",
        "text": "Приседания, выпады, подъёмы на носки. Следи, чтобы колени не заваливались внутрь.",
        "gif": "legs.gif",
    },
    "exercise_glutes": {
        "title": "Ягодицы",
        "text": "Ягодичный мостик, отведения ноги назад, выпады. Движение делай плавно, без рывков.",
        "gif": "glutes.gif",
    },
    "exercise_back": {
        "title": "Спина",
        "text": "Тяга, гиперэкстензия, упражнения на осанку. Спина ровная, шея без напряжения.",
        "gif": "back.gif",
    },
    "exercise_chest": {
        "title": "Грудь",
        "text": "Отжимания или жим. Главное — контролировать движение и не проваливаться в плечах.",
        "gif": "chest.gif",
    },
    "exercise_arms": {
        "title": "Руки",
        "text": "Сгибания и разгибания рук, лёгкие упражнения на бицепс и трицепс.",
        "gif": "arms.gif",
    },
    "exercise_cardio": {
        "title": "Кардио",
        "text": "Быстрая ходьба, лёгкий бег, прыжки или велотренажёр. Темп должен быть комфортным.",
        "gif": "cardio.gif",
    },
    "exercise_core": {
        "title": "Кор",
        "text": "Планка, dead bug, боковая планка. Корпус держи ровно, поясницу не прогибай.",
        "gif": "core.gif",
    },
    "exercise_abs": {
        "title": "Пресс",
        "text": "Скручивания, подъём ног, планка. Не тяни шею руками, работай мышцами живота.",
        "gif": "abs.gif",
    },
    "exercise_fullbody": {
        "title": "Фулл-боди",
        "text": "Комплекс на всё тело: приседания, отжимания, тяга, пресс и лёгкое кардио.",
        "gif": "fullbody.gif",
    },
    "exercise_cooldown": {
        "title": "Заминка",
        "text": "Лёгкая растяжка и восстановление дыхания после тренировки.",
        "gif": "cooldown.gif",
    },
    "exercise_biceps": {
        "title": "Бицепс",
        "text": "Сгибания рук с гантелями или резинкой. Локти держи ближе к корпусу.",
        "gif": "biceps.gif",
    },
    "exercise_trapeze": {
        "title": "Трапеция",
        "text": "Шраги и упражнения на верх спины. Не зажимай шею слишком сильно.",
        "gif": "trapeze.gif",
    },
    "exercise_rear_delta": {
        "title": "Задняя дельта",
        "text": "Разведения рук в наклоне. Движение небольшое, но контролируемое.",
        "gif": "rear_delta.gif",
    },
    "exercise_shoulders": {
        "title": "Плечи",
        "text": "Жим вверх и разведения рук. Не бери слишком большой вес, плечи любят аккуратность.",
        "gif": "shoulders.gif",
    },
    "exercise_triceps": {
        "title": "Трицепс",
        "text": "Разгибания рук, обратные отжимания. Локти не разводи слишком широко.",
        "gif": "triceps.gif",
    },
}


@exercise_router.callback_query(F.data.startswith("exercise_"))
async def show_exercise(callback: types.CallbackQuery):
    exercise = EXERCISES.get(callback.data)
    if exercise is None:
        await callback.answer("Упражнение не найдено")
        return

    sets = get_user_sets(callback.from_user.id)
    text = (
        f"🏋️ {exercise['title']}\n\n"
        f"{exercise['text']}\n\n"
        f"Количество подходов: {sets}"
    )

    gif_path = GIF_DIR / exercise["gif"]
    if gif_path.exists():
        await callback.message.answer_animation(animation=FSInputFile(gif_path), caption=text)
    else:
        await callback.message.answer(text + f"\n\nГифка пока не добавлена: gifs/{exercise['gif']}")

    await callback.answer()
