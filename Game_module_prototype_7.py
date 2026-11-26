from random import randint
from random import choice

# Задание словаря с темами и словами для игры
age_5_7 = {"Сказки":{"клубок":"сказочный путеводитель",
"буян":"чудо-остров", "копытце":"опасная лужа", "ласточка":"знает, где зимуют принцы",
"лисичка":"горе-строитель"}, 
"Животные":{"медведь":"хозяин леса", "утконос":"есть ядовитый шип",
"бивень": "выдающийся зуб", "лама":"родня верблюда", "океан":"дом самых больших животных"},
"Жучки":{"блоха":"в Туле с ней поступили как с лошадью", "кузнечик":"совсем как человечек",
"таракан":"не боится атома", "стрекоза":"безответственная особа, которая любит петь", 
"муха":"именинница-невеста Комара"}}

#Список доступных букв
possible_letters =["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
 

# Игроки
gamer1 = ("Вася", 1231)
gamer2 = ("Маша", 1232)
gamer3 = ("Лёня", 1233)


# Выбор темы и слова
theme_index = randint(0,2)
theme= list(age_5_7.keys())[theme_index]
print(f'Тема: {theme}')

word_index = randint(0,4)
word = list(age_5_7.get(theme).keys())[word_index]
word_list = list(word)
word_desc = age_5_7[theme][word]
print (f'Подсказка: {word_desc}')

#Счетчик доступных ходов
count_of_parts = len(word_list)
print(f'Осталось открыть: {count_of_parts} букв')

#Скрываем значения букв в слове
word_to_open =[]
for char in word_list:
    char = "_"
    word_to_open.append(char)
print(word_to_open)


#Определяем очередность игроков
tern = {}
tern_number = [1, 2, 3]
gamer1_tern = choice(tern_number)
tern[gamer1_tern]=gamer1[0]
tern_number.remove(gamer1_tern)
gamer2_tern = choice(tern_number)
tern[gamer2_tern]=gamer2[0]
tern_number.remove(gamer2_tern)
gamer3_tern = tern_number[0]
tern[gamer3_tern]=gamer3[0]
print(tern)

#Игровые счета
scores ={}
scores[tern[1]]=0
scores[tern[2]]=0
scores[tern[3]]=0 
print(scores)

#Действия игроков
actions=["назвать букву", "назвать слово целиком"]

#Функция кручения барабана
def wheel_go():
    #Список возможных значений
    possible_cases=[50,100,150,200,250,300,350,'Плюс','Переход хода','Умножить на 2','Банкрот']
    case = choice(possible_cases)
    return case

#Первый игрок делает ход:
print (f'{tern[1]}, крутите барабан!')
point = wheel_go()
print(point)


#Определение наличия буквы в слове
def is_letter_in_word(letter):
    if letter in word_list:
        letters_positions =[]
        letter_counter = word_list.count(letter)
        for i in range(letter_counter):
            l_ind = word_list.index(letter)
            letters_positions.append(l_ind)
            word_list[l_ind] = '_'
            letter_counter -= 1
        for position in letters_positions:
            word_to_open[position]=letter
        return word_to_open
    return word_to_open

#Открытие буквы в варианте "Плюс"
def char_to_open_def(number):
    char_to_open = word_list[number-1]
    word_to_open[number-1] = char_to_open
    possible_letters.remove(char_to_open)
    print(word_to_open)
    return word_to_open
    
#Выбор варианта действия и Обработка ошибок ввода значения для выбора варианта действия
def try_action_choise():
    while True:
        try: 
            text = int(input('Выберите действие: назвать букву (0), назвать слово целиком (1): '))
        except ValueError:
            print('Упс, опечаточка! Попробуйте еще разок, но только 0 или 1')
            continue
        if text == 0 or text == 1:
                return text
                break


#Ограничение значений номера буквы для варианта "Плюс"
def open_a_letter_in_plus():
    #Список доступных значений
    possible_numbers=[ind+1 for ind, char in enumerate(word_to_open) if char == '_']
    while True:
        try: 
            text = int(input('Введите номер буквы, которую желаете открыть: '))
        except ValueError:
            print(f'Упс, опечаточка! Попробуйте еще разок, но только какое-нибудь число из вот этих:  {possible_numbers}')
            continue
        except IndexError:
            print(f'Упс, опечаточка! Попробуйте еще разок, но только какое-нибудь число из вот этих:  {possible_numbers}')
        if text in possible_numbers:
                return text
                break

#Ограничение значений букв для ввода игроком
def choose_the_letter():
    while True:
        try:
            text = str(input('Введите букву: ')).lower()
        except ValueError:
            print('Упс, опечаточка! Попробуйте еще разок')
            continue
        if text in possible_letters:
                return text
                break

#Игра основная функция
def result_detection(point, j):
    result=[]
    if point in (50,100,150,200,250,300,350):
    #Игрок выбирает действие
        action_choise = try_action_choise()
        if action_choise == 0:
            action = actions[action_choise]
            letter = choose_the_letter()
            possible_letters.remove(letter)
            effect = is_letter_in_word(letter)
            result.append(effect)
            count_of_parts = effect.count('_')
            result.append(count_of_parts)
            score_increase = point*effect.count(letter)
            new_score = scores[tern[j]] + score_increase
            result.append(new_score)
            if effect.count(letter) > 0:
                next_actor = j
            else:
                if j == 1 or j == 2:
                    next_actor = j+1
                else:
                    next_actor = 1
            result.append(next_actor)
        else:
            print ('Введите слово')
            user_word = str(input()).lower()
            user_word_list = list(user_word)
            if user_word_list == list(word):
                score_increase = point + 1000
                new_score = scores[tern[j]] + score_increase
                count_of_parts = 0
                result.append(count_of_parts)
                result.append(new_score)
                result.append(new_score)
                print(f'В этой игре победил {tern[j]}! Поздравляем Вас!')

            else:
                #Пока без исключения игрока,  просто обнуление счета
                print(f'Как печально... Слово-то не то... {tern[j]}, отдохните чуть-чуть...')
                score_increase = 0
                new_score = scores[tern[j]] * score_increase
                result.append(new_score)
                if j == 1 or j == 2:
                    next_actor = j+1
                else:
                    next_actor = 1 
                result.append(next_actor)
                
    elif point == 'Плюс':
        number = open_a_letter_in_plus()
        effect = char_to_open_def(number)
        result.append(effect)
        count_of_parts = effect.count('_')
        result.append(count_of_parts)
        score_increase = 0
        new_score = scores[tern[j]] + score_increase
        print(new_score)
        result.append(new_score)
        if j == 1 or j == 2:
            next_actor = j+1
        else:
            next_actor = 1 
        result.append(next_actor)
        
    elif point == 'Переход хода':
        print (f'Увы, {tern[j]}, не в этот раз')
        if j == 1 or j == 2:
            next_actor = j+1
        else:
            next_actor = 1 
        result.append(next_actor)
    
    elif point == 'Умножить на 2':
        #Игрок выбирает действие
        action_choise = try_action_choise()
        if action_choise == 0:
            action = actions[action_choise]
            letter = choose_the_letter()
            possible_letters.remove(letter)
            effect = is_letter_in_word(letter)
            result.append(effect)
            count_of_parts = effect.count('_')
            result.append(count_of_parts)
            #Выбор способа увеличения в зависимости от исходного состояния счета
            if scores[tern[j]] == 0:
                score_increase = 500
            else:
                score_increase = scores[tern[j]]
            new_score = scores[tern[j]] + score_increase
            result.append(new_score)
            if effect.count(letter) > 0:
                next_actor = j
            else:
                if j == 1 or j == 2:
                    next_actor = j+1
                else:
                    next_actor = j
            result.append(next_actor)
        else:
            print ('Введите слово')
            user_word = str(input()).lower()
            user_word_list = list(user_word)
            if user_word_list == list(word):
                if scores[tern[j]] == 0:
                    score_increase = 1500
                else:
                    score_increase = scores[tern[j]]+1000
                new_score = scores[tern[j]] + score_increase
                count_of_parts = 0
                result.append(count_of_parts)
                result.append(new_score)
                result.append(new_score)
                print(f'В этой игре победил {tern[j]}! Поздравляем Вас!')
            else:
                #Пока без исключения игрока,  просто обнуление счета
                print(f'Как печально... Слово-то не то... {tern[j]}, отдохните чуть-чуть...')
                score_increase = 0
                new_score = scores[tern[j]] * score_increase
                result.append(new_score)
                if j == 1 or j == 2:
                    next_actor = j+1
                else:
                    next_actor = 1 
                result.append(next_actor)
    elif point == 'Банкрот':
        print (f'Ой-ой, {tern[j]}, вот не повезло! Отдохните пока... и дышите глубже, кажется, вы взволнованы')
        score_increase = 0
        new_score = scores[tern[j]] * score_increase
        result.append(new_score)
        if j == 1 or j == 2:
            next_actor = j+1
        else:
            next_actor = 1 
        result.append(next_actor)
    
    return result
    

first_act = result_detection(point,  1)

if len(first_act) < 2:
    if point == 'Переход хода':
        j = first_act[0]
        print('\n'*2)
        print(word_to_open)
        print(f'Осталось открыть: {count_of_parts} букв')
        print(f'Текущий счёт: {scores}')
        print (f'{tern[j]}, крутите барабан!')
    elif point in (50,100,150,200,250,300,350):
        scores[tern[1]] = first_act[0]
        print('\n'*2)
        print(f'Текущий счёт: {scores}')
    elif point == 'Умножить на 2':
        scores[tern[1]] = first_act[0]
        print('\n'*2)
        print(f'Текущий счёт: {scores}')  
elif len(first_act) == 2:
    if point in (50,100,150,200,250,300,350):
        #Пока без удаления игрока, просто обнуление счета
        scores[tern[1]] = first_act[0]
        j = first_act[1]
        print('\n'*2)
        print(word_to_open)
        print(f'Осталось открыть: {count_of_parts} букв')
        print(f'Текущий счёт: {scores}')
        print (f'{tern[j]}, крутите барабан!')
    elif point == 'Умножить на 2':
        #Пока без удаления игрока, просто обнуление счета
        scores[tern[1]] = first_act[0]
        j = first_act[1]
        print('\n'*2)
        print(word_to_open)
        print(f'Осталось открыть: {count_of_parts} букв')
        print(f'Текущий счёт: {scores}')
        print (f'{tern[j]}, крутите барабан!')
    elif point == 'Банкрот':
        #Пока без удаления игрока, просто обнуление счета
        scores[tern[1]] = first_act[0]
        j = first_act[1]
        print('\n'*2)
        print(word_to_open)
        print(f'Осталось открыть: {count_of_parts} букв')
        print(f'Текущий счёт: {scores}')
        print (f'{tern[j]}, крутите барабан!')
elif len(first_act) == 3:
    count_of_parts = first_act[0]
else:
    word_to_open=first_act[0]
    count_of_parts = first_act[1]
    scores[tern[1]] = first_act[2]
    j = first_act[3]
    print('\n'*2)
    print(word_to_open)
    print(f'Осталось открыть: {count_of_parts} букв')
    print(f'Текущий счёт: {scores}')
    print (f'{tern[j]}, крутите барабан!')

#Рекурсия до завершения игры    
while count_of_parts != 0: 
    point = wheel_go()
    print (f'Подсказка: {word_desc}')
    print(point)
        
    next_act = result_detection(point,  j)
        

    if len(next_act) < 2:
        if point == 'Переход хода':
            j = next_act[0]
            print('\n'*2)
            print(word_to_open)
            print(f'Осталось открыть: {count_of_parts} букв')
            print(f'Текущий счёт: {scores}')
            print (f'{tern[j]}, крутите барабан!')
        elif point in (50,100,150,200,250,300,350):
            scores[tern[1]] = next_act[0]
            print('\n'*2)
            print(f'Текущий счёт: {scores}')
        elif point == 'Умножить на 2':
            scores[tern[1]] = next_act[0]
            print('\n'*2)
            print(f'Текущий счёт: {scores}')
    elif len(next_act) == 2:
        if point in (50,100,150,200,250,300,350):
            #Пока без удаления игрока, просто обнуление счета
            scores[tern[1]] = next_act[0]
            j = next_act[1]
            print('\n'*2)
            print(word_to_open)
            print(f'Осталось открыть: {count_of_parts} букв')
            print(f'Текущий счёт: {scores}')
            print (f'{tern[j]}, крутите барабан!')
        elif point == 'Умножить на 2':
            #Пока без удаления игрока, просто обнуление счета
            scores[tern[1]] = next_act[0]
            j = next_act[1]
            print('\n'*2)
            print(word_to_open)
            print(f'Осталось открыть: {count_of_parts} букв')
            print(f'Текущий счёт: {scores}')
            print (f'{tern[j]}, крутите барабан!')
        elif point == 'Банкрот':
            #Пока без удаления игрока, просто обнуление счета
            scores[tern[j]] = next_act[0]
            j = next_act[1]
            print('\n'*2)
            print(word_to_open)
            print(f'Осталось открыть: {count_of_parts} букв')
            print(f'Текущий счёт: {scores}')
            print (f'{tern[j]}, крутите барабан!')
    elif len(next_act) == 3:
        break
    else:
        word_to_open=next_act[0]
        count_of_parts = next_act[1]
        scores[tern[j]] = next_act[2]
        j = next_act[3]
        print('\n'*2)
        print(word_to_open)
        print(f'Осталось открыть: {count_of_parts} букв')
        print(f'Текущий счёт: {scores}')
        print (f'{tern[j]}, крутите барабан!')

print('Этап закончен! Молодцы!')
    