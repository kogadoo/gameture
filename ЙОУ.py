import json
import csv
import random

def load_game_data():
    try:
        with open('game_data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {'users': []}


def save_game_data(data):
    with open('game_data.json', 'w') as file:
        json.dump(data, file, indent=4)


def delete(data):
    with open('game_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Age', 'Fruit', 'Reputation', 'Achievements'])
        for user in data['users']:
            writer.writerow(
                [user['name'], user['age'], user['fruit'], user['reputation'], ', '.join(user['achievements'])])

def goodlife():
    print("Ты: Не спасибо, не очень хочется во что то ввязываться", end = " ")
    input()
    print("Д: Ну ладно, мое дело предложить, твое дело отказаться, удачи братуха")
def kaiflife():
    print("Ты: Да бро, рассказывай, а то скучно капец", end = " ")
    input()
    print("Д: в общем рассказываю, есть варик банкомат взломать и бабки прикарманить, стоит в отдаленном районе, сделать это проще некуда, согласен?", end = " ")
    input()
    print("Ты: Ну не знаю...", end = " ")
    input()
    print("Д: Да не ломайся ты, все чики пуки будет, заживем наконец нормально!", end = " ")
    input()
    print("Ты: Ладно, погнали!", end = " ")
    input()
    print("Получено достижение: Дурачек")
    achievements.append("Дурачек")
    input()
    return achievements
def information():
    print(f"Ваше имя: {name}\nВаш возраст: {age}\nВаш любимый фрукт: {fruit}")
def reput(rep):
    rep = (str(rep))
    print("Репутация: " + rep)
    return rep

while True:
    achievements = []
    info = []
    game_data = load_game_data()
    rep = 0
    shara = random.randint(0, 4)
    names = ("Вололдя", "Михаил", "Григорий", "Иван")
    name = input("Представься плез: ")
    fruit = input("Любимый фрукт: ")
    age = 22
    yesornot = input("Стартуем?\n1. Да\n2. Нет\n3. Выход\n")
    if yesornot == "2":
        continue
    elif yesornot == "3":
        break
    elif yesornot == "1":
        print("Был обычный, ничем не примечательный день, впрочем как и всегда, ты размышлял о том, что тебе уже 22 года, а ты так скучно скучно живешь:(")
        print("Но тут раздался телефонный звонок. Это был твой давний друг:")
        age = 22
        choice = input("1. Да бро, рассказывай, а то скучно капец\n2. Не спасибо, не очень хочется во что-то ввязываться\n")
        if choice == "1":
            kaiflife()
            print("Через два часа вы встретились у того самого банкомата и начали взлом, но как назло мимо проезжал наряд полиции...")
            input()
            print("Получено достижение: Сел в 22 года..")
            game_data['users'].append({
                    'name': name,
                    'age': age,
                    'fruit': fruit,
                    'reputation': rep,
                    'achievements': ["Сел в 22 года.."]
                })

            input()
            print(f"Прошла неделя, тебя перевели в тюрьму. Нужно с кем-то закорешиться")
            print("1. С сокамерником Олегом\n2. С сокамерником Магой\n3. Найти типа в столовой, и закентиться с ним")
            reput(rep)
            kenty = input()


            save_game_data(game_data)

            if kenty == "1":
                print("Твой выбор пал на Олега, что ж закентиться получилось, но дядя Олежа оказался не так прост, он тот еще гей. С таким другом жизнь на зоне до добра не доведет.. В следующий раз придется выбирать кента аккуратней.\nПолучено достижение: Друг Олежа")
                achievements.append("Друг Олежа")
                rep -= 10
                reput(rep)
            elif kenty == "2":
                print("Твой выбор пал на Магу. Ты подошел к нему, кинул салам, но тот лишь презрительно посмотрел на тебя и отвернулся.\nТвои действия?\n1. Дернуть его за плечо\n2. Забить и уйти\n3. Умолять закентиться с тобой")
                maga = input()
                if (maga == "1"):
                    print("Ты дернул его за плечо, дабы тот повернулся, но Мага прописал тебе в ухо с разворота, ты отключился\nПолучено достижение: В отключке")
                    achievements.append("В отключке")
                    input()
                    print(f"Ты очнулся в медотделе, лежать тут нужно ближайшие сутки\n*А Мага харош, неплохой удар*\nПолучено достижение: Отмутозили в первый день")
                    rep -= 5
                    reput(rep)
                if (maga == "2"):
                    print("Ну что ж, необщительный мага какой-то:(")
                if (maga == "3"):
                    print("Ты начал умолять магу начать дружить с тобой. Он сжалился, но сказал, что если будешь таким нытиком, то кентом его не считай\n*Видно - Мага тип ровный, придется взять себя в руки*")
                    rep += 10
                    reput(rep)
                elif kenty == "3":
                    print("Ты пошел искать типов в столовке. Выбери с кем хочешь закентиться\n1. Большой мужик одиночка\n2. Толпа мужиков, на вид хлюпиков\n3. Компашка двух друзей")
                    stolovka = input()
                    stolovkaname = names[shara]
                    if (stolovka == "1"):
                        print(f"Несмотря на его телосложение, {stolovkaname} здесь изгой, но все его боятся, поэтому не трогают. А он неплохой друг.")
                        rep += 5
                        reput(rep)
                    if (stolovka == "2"):
                        print("Ты подлетел к этой толпе, и попытался взять инициативу разговора на себя, и показать свое превосходтсво, но хлюпики этого не оценили, и отпинали тебя толпой\n*Жизнь жестока*\nПолучено достижение: Толпою гасят даже льва")
                        achievements.append("Толпою гасят даже льва")
                        rep -= 5
                        reput(rep)
                    if (stolovka == "3"):
                        print(f"Ты подошел к этим двоим. Их зовут {stolovkaname} и {stolovkaname}. Как то забазарился с ними, вроде ровные типы, и знают здесь многих, определенно отличное знакомство\nПолучено новое достижение: Два новых кента")
                        achievements.append("Два новых кента")
                        rep += 15
                        reput(rep)
            action = input("1. Сохранить игру\n2. Загрузить игру. \n3. Удалить сохранение")
            if action == "1":
                save_game_data(game_data)
            elif action == "2":
                load_game_data()
            elif action == "3":
                delete(game_data)
                print("Сохранение удалено!")
            print("На сегодня хватит. Дальше - больше")
            break
        elif choice == "2":
            goodlife()
            break


