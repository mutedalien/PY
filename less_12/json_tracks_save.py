# модуль json
import json

favorite_tracks = [
    {'name': 'Вечная любовь', 'artist': 'Агата Кристи'},
    {'name': 'Angel', 'artist': 'Massive Attack'},
    {'name': 'Jumping', 'artist': 'Bob Marley'}
]
with open('tracks.json', 'w', encoding='utf-8') as f:
    json.dump(favorite_tracks, f)
print('Выполнено')