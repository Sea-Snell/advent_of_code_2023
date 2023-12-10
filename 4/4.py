import re

if __name__ == "__main__":
    games = []
    with open('4.txt', 'r') as f:
        for game in f:
            game = game.strip()
            game_id = re.search(r'Game (\d+):', game).group(1)
            sets_of_cubes = game.split(':')[1].split(';')
            cubes_data = []
            for set_of_cubes in sets_of_cubes:
                curr_cubes = {'red': 0, 'green': 0, 'blue': 0}
                for cubes in set_of_cubes.split(','):
                    cubes = cubes.strip()
                    if 'red' in cubes:
                        curr_cubes['red'] += int(cubes.split(' ')[0])
                    elif 'green' in cubes:
                        curr_cubes['green'] += int(cubes.split(' ')[0])
                    elif 'blue' in cubes:
                        curr_cubes['blue'] += int(cubes.split(' ')[0])
                cubes_data.append(curr_cubes)
            games.append({
                'game_id': game_id,
                'cubes_data': cubes_data,
            })
    
    total = 0
    for game in games:
        minimum_game = {'red': float('-inf'), 'green': float('-inf'), 'blue': float('-inf')}
        for pull in game['cubes_data']:
            for k in minimum_game.keys():
                minimum_game[k] = max(minimum_game[k], pull[k])
        power = minimum_game['red'] * minimum_game['green'] * minimum_game['blue']
        total += power
    
    print(total)
