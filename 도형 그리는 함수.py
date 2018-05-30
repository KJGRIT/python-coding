import turtle as t

def square(length):
    for i in range(length):
        t.fd(length)
        t.lt(90)

t.up()
t.goto(-200, 0)
t.down()
square(100);

t.up()
t.goto(0, 0)
t.down()
square(100);

t.up()
t.goto(200, 0)
t.down()
square(100);

