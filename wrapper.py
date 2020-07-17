from datetime import datetime

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            str = "it's date time"
            str += func()
        else:
            str = "don't make noise"
        return str
    
    return wrapper


@not_during_the_night
def activity():
    str = ' ,go biking'
    return str


print(activity())


