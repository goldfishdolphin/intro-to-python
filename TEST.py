num = 126


def StringChallenge(num):

    # code goes here

    hours = str(num // 60)
    minutes = num % 60
    print(str(num // 60)+':' + (str(num % 60)))
    return f'{hours}:{minutes}'


text = "Hello"

print(text.lower())

print(StringChallenge(126))
