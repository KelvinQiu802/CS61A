class Link:

    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    @property
    def second(self):
        return self.rest.first

    @second.setter
    def second(self, value):
        self.rest.first = value


l = Link(1, Link(2, Link(3)))
print(l.first)
print(l.rest.first)
print(l.rest.rest.first)
print(l.rest.rest.rest is Link.empty)

s = Link(0, l)
print(s.first)
print(s.second)
s.second = 10
print(s.second)
