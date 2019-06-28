##p.156 구구단

i, dan = 0, 0
guguLine = ""

for i in range(2,10):
    guguLine = guguLine + (" #   %d단   #  " %i)

print(guguLine)

for i in range(1, 10, 1):
    guguLine = ""
    for k in range(2, 10):
        guguLine = guguLine +str("%2d X %2d = %2d  " % (k, i, k*i))

    print(guguLine)


for i in range(1, 10, 1):
    guguLine = ""
    for k in range(2,10):
        guguLine = guguLine + str("%2d X %2d = %2d " % (i, k, k*i))

    print(guguLine)