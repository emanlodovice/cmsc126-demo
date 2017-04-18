a = 2

if a == 1:
    print 'foo'
elif a == 2:
    print 'bar'
else:
    print 'foo bar'


def my_func(b, z=1, *args, **kwargs):
    print b
    print z
    print args
    print kwargs


my_func(3, 2, 1, a=2)



