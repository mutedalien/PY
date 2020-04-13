def hello_max():
    print('Hello', 'Max')
hello_max()

def hello(who):
    print('Hello', who)
hello('Leo')
hello('Kate')

def greeting(who, say):
    print(say, who)
greeting('Leo', 'Hi')
greeting('Max', 'Hello')

def greeting(say, *args): # * Дает возможность указывать множество параметров для args
    print(say, args)
greeting('Hello', 'Leo')
greeting('Hello', 'Leo', 'Max', 'Kate')

def get_person(**kwargs):
    for k, v in kwargs.items():
        print(k, v)
get_person(name='Leo', age=20, has_car=True)