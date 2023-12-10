import re

if __name__ == "__main__":
    games = []
    with open('3.txt', 'r') as f:
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
        plausible = True
        for pull in game['cubes_data']:
            if pull['red'] > 12:
                plausible = False
                break
            if pull['green'] > 13:
                plausible = False
                break
            if pull['blue'] > 14:
                plausible = False
                break
        if plausible:
            total += int(game['game_id'])
    
    print(total)
