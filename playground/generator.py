def my_range(start, end):
    i = start
    while i < end:
        yield i
        i += 1


def count_down(num):
    if num >= 0:
        yield num
        yield from count_down(num - 1)


for i in my_range(0, 5):
    print(i)

print('#####################')

for i in count_down(5):
    print(i)
