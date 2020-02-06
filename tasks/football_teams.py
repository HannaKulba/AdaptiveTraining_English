n = int(input())
dict = {}


def update_winner(winner_team):
    if dict.__contains__(winner_team):
        results_win = dict[winner_team]
        dict[winner_team] = [results_win[0] + 1, results_win[1] + 1, results_win[2], results_win[3], results_win[4] + 3]
    else:
        dict.update({winner_team: [1, 1, 0, 0, 3]})


def update_loser(loser_team):
    if dict.__contains__(loser_team):
        results_lose = dict[loser_team]
        dict[loser_team] = [results_lose[0] + 1, results_lose[1], results_lose[2], results_lose[3] + 1, results_lose[4]]
    else:
        dict.update({loser_team: [1, 0, 0, 1, 0]})


def update_draws(draw_team):
    if dict.__contains__(draw_team):
        results_draws = dict[draw_team]
        dict[draw_team] = [results_draws[0] + 1, results_draws[1], results_draws[2] + 1, results_draws[3],
                           results_draws[4] + 1]
    else:
        dict.update({draw_team: [1, 0, 1, 0, 1]})


for i in range(n):
    arr = input().split(";")
    print(arr)
    if int(arr[1]) > int(arr[3]):
        update_winner(arr[0])
        update_loser(arr[2])
    elif int(arr[1]) < int(arr[3]):
        update_winner(arr[2])
        update_loser(arr[0])
    elif int(arr[1]) == int(arr[3]):
        update_draws(arr[0])
        update_draws(arr[2])

for team in dict.keys():
    print(team + ':', end='')
    for result in dict[team]:
        print(result, end=' ')
    print()
