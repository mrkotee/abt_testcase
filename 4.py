import sys
import json


def count_questions(data: dict):
    # вывести количество вопросов (questions)
    q_len = 0
    for round in data['game']['rounds']:
        q_len += len(round['questions'])

    print(q_len)
    return q_len


def print_right_answers(data: dict):
    # вывести все правильные ответы (correct_answer)
    correct_answers = []
    for round in data['game']['rounds']:
        for question in round['questions']:
            if question['type'] == "text":
                correct_answers.append(question['correct_answer'])
            elif question['type'] == "select":
                ans_id = question['correct_answer']
                correct_answers.append(question['answers'][ans_id])
            elif question['type'] == "multiselect":
                for ans_id in question['correct_answer']:
                    correct_answers.append(question['answers'][ans_id])

    print(correct_answers)
    return correct_answers


def print_max_answer_time(data: dict):
    # вывести максимальное время ответа (time_to_answer)
    def check_max_time(time_to_answer):
        nonlocal max_time
        if time_to_answer > max_time:
            max_time = time_to_answer

    max_time = 0
    for round in data['game']['rounds']:
        if round['type'] == "blitz":
            check_max_time(round['settings']['time_to_answer'])
        else:
            for question in round['questions']:
                check_max_time(question['time_to_answer'])

    print(max_time)
    return max_time


def main(filename):
    with open(filename) as f:
        data = json.load(f)  # загрузить данные из test.json файла
    count_questions(data)
    print_right_answers(data)
    print_max_answer_time(data)


if __name__ == '__main__':
    # передать имя файла из аргументов командной строки
    if len(sys.argv) < 2:
        print("Передайте аргументом имя файла")
        sys.exit()
    filename = sys.argv[1]
    main(filename)
