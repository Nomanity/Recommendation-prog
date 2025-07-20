from random import choice
from Professions import Job, jobs_gen, scores_gen
import logging


logger = logging.getLogger(__name__)
logging.basicConfig(filename = 'Training_Graph.log',
                    level = logging.INFO,
                    format = '%(levelname)s - %(name)s - #%(lineno)d: %(message)s',
                    encoding = 'UTF-8')



def choose_random(iterator):
    value = choice(list(iterator))
    return value



def collect_inputs(): 
    print ('\n\nТеперь мне нужно, чтобы вы оценили себя или вашу желаемую профессию' \
        ' по 5 пунктам, которые я определил ранее, по шкале от 1 до 10.')
    inputs_list = []
    
    for attr in Job.attribute_names:
        while True:
            try:
                user_input = int(input(attr + ': '))
                if user_input not in range(11):
                    raise ValueError
                break
            except ValueError:
                print ('Некорректный ввод. Допустимы только целые числа от 1 до 10')
                logger.error('Input error. Only numbers 1 - 10 is valid')
    
        inputs_list.append(user_input) 
        
    inputs_list.insert(0, 'Ваши данные')
    print (dict([(inputs_list[0], inputs_list[1:])]), '\n\n\n')

    return tuple(inputs_list[1:])



def data_computations(generator = scores_gen):
    data = collect_inputs()
    scores = generator
    print ('{: ^50}\n'.format('↓↓↓ Результаты ↓↓↓'))

    good_choices, bad_choices = [], []
    for i in scores:
        difference_in_scores = sum(data) - sum(i[1])
        if difference_in_scores > 0:
            good_choices.append(i[0])
            
        else:
            bad_choices.append(i[0])

    print ('Вам подходит: ' + ', '.join(good_choices))
    print ('Будет тяжело: ' + ', '.join(bad_choices))
    exit_program()


def exit_program():
    input('\n\nДля выхода из программы нажмите Enter или Space')
    quit()

def start_program():
    print ('Давайте я помогу вам выбрать подходящую профессию.\n')
    start_input = input('Начнем? (введите да или нет) ').lower()

    while True:
        if start_input == 'да':
            break
        elif start_input == 'нет':
            exit_program()
        else:
            print ('Неправильный ввод. Попробуйте снова')
            logger.error('Неверный ввод в функции start_program()')
            start_input = input('Желаете продолжить? ').lower()


def show_example(iterator = jobs_gen):
    example_prof = choose_random(iterator)
    print ('\nДля каждой профессии вводятся 5 шкал:')
    for item in enumerate(Job.attribute_names, start = 1):
        print (item[0], item[1], sep = '. ')
    print ('\n\nНапример, для ' + f'\'{example_prof}\' '  + 'данные будут следующими:')
    example_prof.print_attributes()