def formatTime(seconds):
    try:
        if (seconds > 0):
            hour = 0
            minute = 0
            second = seconds

            if seconds >= 60:
                minute = int(second / 60)
                second = second % 60

            if minute >= 60:
                hour = int(minute / 60)
                minute = minute % 60

            hour = format60(hour)
            minute = format60(minute)
            second = format60(second)
            return "{}:{}:{}".format(hour, minute, second)
        else:
            return "Invalid Time"
    except:
        return "Invalid Time"


def format60(time):
    if time > 10:
        return f'{time}'
    else:
        return f'0{time}'


print(formatTime('hehe'))
