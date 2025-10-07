
n = 2
progression = []
start = 1
while len(progression) < 100000:
    progression.append(start)
    start += n

def progression(limit=100):
    n = 2
    start = 1
    count = 1
    while count < limit:
        yield start
        start += n
        count += 1
#print(type(progression(10)))
#print(list(progression(10)))

count = 0
for number in progression(100001):
    if count == 10000:
        print(number)
        break
    count += 1

