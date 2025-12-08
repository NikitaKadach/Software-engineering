import xml.etree.ElementTree as ET
def load_users():
    tree = ET.parse('users.xml')
    root = tree.getroot()

    users_list = []

    for person in root.findall('user'):
        user_info = {
            'id': int(person.find('user_id').text),
            'name': person.find('name').text,
            'age': int(person.find('age').text),
            'weight': int(person.find('weight').text),
            'level': person.find('fitness_level').text,
            'workouts': []
        }
        users_list.append(user_info)

    return users_list


def load_workouts():
    tree = ET.parse('workouts.xml')
    root = tree.getroot()

    workouts_list = []

    for training in root.findall('workout'):
        workout_info = {
            'id': int(training.find('workout_id').text),
            'user_id': int(training.find('user_id').text),
            'date': training.find('date').text,
            'type': training.find('type').text,
            'duration': int(training.find('duration').text),
            'distance': float(training.find('distance').text),
            'calories': int(training.find('calories').text),
            'heart_rate': int(training.find('avg_heart_rate').text),
            'intensity': training.find('intensity').text
        }
        workouts_list.append(workout_info)

    return workouts_list


def show_stats(users, workouts):
    total_trainings = len(workouts)
    total_people = len(users)

    all_calories = 0
    for w in workouts:
        all_calories += w['calories']

    all_time_minutes = 0
    for w in workouts:
        all_time_minutes += w['duration']
    all_time_hours = all_time_minutes / 60

    all_distance = 0
    for w in workouts:
        all_distance += w['distance']

    print("Общая статистикаа")
    print("========================")
    print(f"Всего тренировок: {total_trainings}")
    print(f"Всего пользователей: {total_people}")
    print(f"Сожжено калорий: {all_calories}")
    print(f"Общее время: {all_time_hours:.1f} часов")
    print(f"Пройдено дистанции: {all_distance:.1f} км")
    print()

def find_top_users(users, workouts):
    for user in users:
        user_trainings = []
        for w in workouts:
            if w['user_id'] == user['id']:
                user_trainings.append(w)

        user['workouts'] = user_trainings
        user['total_trainings'] = len(user_trainings)

        user_calories = 0
        for w in user_trainings:
            user_calories += w['calories']
        user['total_calories'] = user_calories

        user_time = 0
        for w in user_trainings:
            user_time += w['duration']
        user['total_time'] = user_time / 60

    sorted_users = sorted(users, key=lambda x: x['total_trainings'], reverse=True)

    print("Топ активных пользователей")
    for i in range(3):
        person = sorted_users[i]
        print(f"{i + 1}. {person['name']} ({person['level']}):")
        print(f"Тренировок: {person['total_trainings']}")
        print(f"Калорий: {person['total_calories']}")
        print(f"Время: {person['total_time']:.1f} часов")
        print()


def show_training_types(workouts):
    types_count = {}
    types_duration = {}
    types_calories = {}

    for w in workouts:
        t_type = w['type']

        if t_type in types_count:
            types_count[t_type] += 1
        else:
            types_count[t_type] = 1

        if t_type in types_duration:
            types_duration[t_type] += w['duration']
        else:
            types_duration[t_type] = w['duration']

        if t_type in types_calories:
            types_calories[t_type] += w['calories']
        else:
            types_calories[t_type] = w['calories']

    total = len(workouts)

    print("Статистика по типам тренировок:")

    type_order = ['бег', 'силовая тренировка', 'велосипед', 'плавание', 'ходьба']

    for t_type in type_order:
        if t_type in types_count:
            count = types_count[t_type]
            percent = (count / total) * 100

            avg_time = types_duration[t_type] / count
            avg_cal = types_calories[t_type] / count

            print(f"{t_type.capitalize()}: {count} тренировок ({percent:.1f}%)")
            print(f"Средняя длительность: {avg_time:.0f} мин")
            print(f"Средние калории: {avg_cal:.0f} ккал")
    print()


def find_user_info(users, workouts, name):
    found_user = None
    for user in users:
        if user['name'].lower() == name.lower():
            found_user = user
            break

    user_workouts = []
    for w in workouts:
        if w['user_id'] == found_user['id']:
            user_workouts.append(w)

    trainings_count = len(user_workouts)

    total_cal = 0
    total_time = 0
    total_dist = 0

    fav_type = {}

    for w in user_workouts:
        total_cal += w['calories']
        total_time += w['duration']
        total_dist += w['distance']

        t_type = w['type']
        if t_type in fav_type:
            fav_type[t_type] += 1
        else:
            fav_type[t_type] = 1

    favorite = max(fav_type, key=fav_type.get)

    avg_cal_per_training = total_cal / trainings_count
    total_time_hours = total_time / 60

    print(f"Анализ пользователя: {found_user['name']}")
    print("================================================")
    print(f"Возраст: {found_user['age']} лет, Вес: {found_user['weight']} кг")
    print(f"Уровень: {found_user['level']}")
    print(f"Тренировок: {trainings_count}")
    print(f"Сожжено калорий: {total_cal}")
    print(f"Общее время: {total_time_hours:.1f} часов")
    print(f"Пройдено дистанции: {total_dist:.1f} км")
    print(f"Средние калории за тренировку: {avg_cal_per_training:.0f}")
    print(f"Любимый тип тренировки: {favorite}")
    print()


def main():
    all_users = load_users()
    all_workouts = load_workouts()

    show_stats(all_users, all_workouts)

    find_top_users(all_users, all_workouts)
    show_training_types(all_workouts)

    find_user_info(all_users, all_workouts, "Борис")


if __name__ == "__main__":
    main()