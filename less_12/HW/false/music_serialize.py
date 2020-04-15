# 1: Создать модуль music_serialize.py.
# В этом модуле определить словарь для вашей любимой музыкальной группы/
# С помощью модулей json и pickle сериализовать данный словарь в json и в байты, вывести результаты в терминал.
# Записать результаты в файлы group.json, group.pickle соответственно. В файле group.json указать кодировку utf-8.

print('Task 6.1 --> Module Serialize music')
import json
import pickle

def serialize_json(music_obj):
    mfg_str = json.dumps(music_obj)
    print('\n serialized json:')
    print(mfg_str)
    print(type(mfg_str))
    # serialaize to file
    with open('group.json', 'w', encoding='utf-8') as file:
        json.dump(music_obj, file)
    print('----->\n Export file to JSON - done')

def serialize_pickle(music_obj):
    mfg_pickle = pickle.dumps(music_obj)
    print('\n serialized bytes:')
    print(mfg_pickle)
    print(type(mfg_pickle))
    # serialaize to file
    with open('group.pickle', 'wb') as file:
        pickle.dump(music_obj, file)
    print('----->\n Export file to Pickle - done')

def serialize(music_obj):
    # using JSON
    serialize_json(music_obj)
    # using Pickle
    serialize_pickle(music_obj)