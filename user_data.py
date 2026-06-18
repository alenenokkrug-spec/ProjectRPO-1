from dataclasses import dataclass

@dataclass
class UserProfile:
    name: str
    age: int
    weight: float
    goal: str

# Простое хранение в памяти. Для учебного проекта этого достаточно.
# После перезапуска бота данные очистятся.
users: dict[int, UserProfile] = {}


def calculate_sets(age: int, weight: float) -> str:
    """Подбор количества подходов по возрасту и весу."""
    if age < 14:
        return "2 подхода. Нагрузка лёгкая, без перегруза и без тяжёлых весов."
    if age < 18:
        if weight < 50:
            return "2–3 подхода. Лучше начинать спокойно и следить за техникой."
        return "3 подхода. Средняя нагрузка, без упражнений до отказа."
    if age <= 45:
        if weight < 55:
            return "3 подхода. Нагрузка умеренная, можно постепенно увеличивать сложность."
        if weight <= 85:
            return "3–4 подхода. Стандартная нагрузка для большинства упражнений."
        return "3 подхода. Лучше делать чуть меньше подходов, но аккуратно и без рывков."
    if age <= 60:
        return "2–3 подхода. Нагрузка умеренная, отдых между подходами лучше увеличить."
    return "2 подхода. Нагрузка лёгкая, главное — безопасность и плавная техника."


def get_user_sets(user_id: int) -> str:
    profile = users.get(user_id)
    if profile is None:
        return "3 подхода. Это базовый вариант, потому что данные о возрасте и весе ещё не указаны."
    return calculate_sets(profile.age, profile.weight)