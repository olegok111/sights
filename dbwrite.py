import time


def maybe_int(s: str):
    try:
        return int(s)
    except ValueError:
        return s


def pwrite(player, points):

    with open('data/players.txt', 'r', encoding='utf8') as file:
        lines = file.readlines()
        player_data = {}
        for line in lines:
            _line = line.replace('\n', '')
            _line = list(map(maybe_int, _line.split()))
            player_data[_line[0]] = {'points': _line[1], 'lastseen': _line[2]}

    date = str(time.localtime().tm_mday) + '/' + str(time.localtime().tm_mon) + '/' + str(time.localtime().tm_year)
    if player in player_data.keys():
        player_data[player]['points'] = points
        player_data[player]['lastseen'] = date
    else:
        player_data[player] = {'points': points, 'lastseen': date}

    with open('data/players.txt', 'w', encoding='utf8') as file:
        for nickname in player_data.keys():
            print(nickname, player_data[nickname]['points'], player_data[nickname]['lastseen'], file=file)


def pget(player):

    with open('data/players.txt', 'r', encoding='utf8') as file:
        lines = file.readlines()
        for line in lines:
            _line = line.replace('\n', '')
            _line = list(map(maybe_int, _line.split()))
            if _line[0] == player:
                return {'points': _line[1], 'lastseen': _line[2]}


if __name__ == '__main__':
    print('This is the module which writes player data to the database (data/players.txt).')