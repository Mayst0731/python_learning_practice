def do_twice_dec(func):
    def wrapper(*args,**kwargs):
        str = 'go '
        str += func(*args, **kwargs) + ' '
        str += 'in day time and ' + func(*args, **kwargs)
        str += ' at night as well'
        return str
    return wrapper

@ do_twice_dec
def act(str):
    return str

print(act('swimming'))


