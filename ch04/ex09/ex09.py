# @title ch04-09
def get_odds(first, last, step):
    for number in range(first, last, step):
        yield number


for i, odd in enumerate(get_odds(1, 10, 2), 1):
    if i == 3:
        print(odd)

# result:
# 5
