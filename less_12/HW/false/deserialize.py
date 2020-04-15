print('Task 6.1 --> Module Deserialize music')
import json
import pickle

def deserialize_json():
    with open('group.json', 'r', encoding='utf-8') as file:
        mfg_json = json.load(file)
    print('\n-----<\n Import from JSON file - done')
    print(mfg_json)
    print(type(mfg_json))

def deserialize_pickle():
    with open('group.pickle', 'rb') as file:
        mfg_pickle = pickle.load(file)
    print('\n-----<\n Import from Pickle file - done')
    print(mfg_pickle)
    print(type(mfg_pickle))

def deserialize():
    # using JSON
    deserialize_json()
    # using Pickle
    deserialize_pickle()
