# Python Basics

## Printing something to the conse
```
print "Hello World"
```

## Variables
`foo = 1`

### Numbers
```
foo = 1                     # int
bar = 1.2                   # float
```

### String
```
foo = 'my foo'
print foo[1:]               # y foo
print foo * 2               # my foomy foo
foo = foo + ' hehe'         # my foo hehe

bar = '%s is my name and I am %d years old' % ('Bar', 21)
bar = '{name} is my name and I am {age} years old'.format(name='Bar', age=21)
```

## Conditions
```
a = 1
if a == 1:
    pass
elif a == 2:
    pass
else:
    pass
```
False Values: None, False, 0, empty sequence (e.g. '', [], ()), {} 

## Functions
```
def foo(bar, foobar=True, *args, **kwargs):
    # starting from the 3rd non keyword arguments will go to args
    # keyword arguments other than bar and foobar will got to kwargs
    return 1
```

## Data Structures

### list
```
my_list = []
my_list.append(1)               # [1]
my_list.append(True)            # [1, True]
len(my_list)                    # 2
last_item = my_list.pop()       # [1]
my_list = my_list + [2, 3, 4]   # [1, 2, 3, 4]
my_list[:2]                     # [1, 2]

```

### tuple
```
a = (1, 2)
print a[0]                      # 1
print a[1]                      # 2
```
Tuples are immutable

### Dictionaries
```
a = {'foo': 1}
a['foo']                        # 1
a.get('foo')                    # 1
a['bar'] = 2
del a['foo']
a.update({'my_foo': 'bar'})     # {'bar': 2, 'my_foo': 'bar'}
```


## loops
```
foo = [1, 2, 3]
for num in foo:
    print num

bar = {'sample': 1, 'another_sample': 2}
for key in bar:
    print bar[key]
```


## Class
```
class FooBar(object):
    
    def foo(self):
        print 'foo'

    def bar(self, num):
        print 'bar {}'.format(num)


my_foo_bar = FooBar()
my_foo_bar.foo()
my_foo_bar.bar(num=2)


class FooBarChild(FooBar):
    
    def __init__(self, age):
        print 'This is the constructor'
        self.age = age

    def get_age(self):
        return self.age


my_foo_bar_child = FooBarChild(age=10)
print my_foo_bar_child.get_age()                # 10
```

[library](https://docs.python.org/2.7/library/index.html)