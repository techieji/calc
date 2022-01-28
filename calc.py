from collections import deque

class info_iter:
    def __init__(self, s, lk=1):
        self.s = s
        self.v = ''
        self.i = iter(s)
        self.char = 0
        self.charcount = 0
        self.lineno = 1
        self.next = deque(maxlen=lk)

    def __iter__(self):
        return self

    def __next__(self):
        self.v = next(self.i)
        self.update()
        return self.v

    def update(self):
        if self.v == '\n':
            self.lineno += 1
            self.char = -1
        self.char += 1
        self.charcount += 1

def lex(s):
    i = iter(s)
    for x in i:
        if x in ' \t\n':
            continue
        elif x.isnumeric():
            num = ''
            while x.isnumeric():
                num += x
                x = next(i)
            yield 'NUM', num
        elif x in '+-/*;()':
            yield 'SYM', x

def lexed_formatted(s):
    i = info_iter(s)
    for t, v in lex(i):
        print(f'#{i.lineno}:{i.char}', t, '\t', v)

lexed_formatted('''1 + 2;
2 * 3;
10 / (2 + 1);
''')
