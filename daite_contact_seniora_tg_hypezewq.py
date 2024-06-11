# %

team1_num = 5
print("В команде Мастера кода %s участников!" % (team1_num))

team2_num = 6
print("Итого сегодня в командах %s и %d участников!" % (team1_num, team2_num))

#format

score_2 = 42
print("Команда Волшебники данных решила задач: {s}!".format(s=score_2))

team1_time = 18015.2
print("Волшебники данных решили задачи за {s} с !".format(s=team1_time))

#f-string

score_1 = 40
challenge_result = "победа команды Мастера кода"
tasks_total = 82
time_avg = 350.4
print(f"Команды решили {score_1} и {score_2} задачи.")
print(f"Результат битвы: {challenge_result}!")
print(f"Сегодня было решено {tasks_total} задачи, в среднем по {time_avg} секунды на каждую!")


