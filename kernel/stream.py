class Pipe(object):
    def __init__(self, name='', value=None, writer=None, reader=None):
        if value is None:
            self.value = []
        else:
            self.value = value
        self.writer = writer
        self.reader = reader
        self.name = name
        self._line = 0
        self.closed = False

    def __nonzero__(self):
        return bool(self.reader)

    def set_reader(self, callback):
        self.reader = callback
        callback.stdin = self

    def set_writer(self, callback):
        self.writer = callback

    def write(self, value):
        if not self.closed:
            self.value.extend(value.split("\n"))

    def read(self):
        for line in self.value[self._line:]:
            yield line
            self._line += 1

    def readlines(self): 
        return self.value

    def close(self):
        self.closed = True
        self.broadcast()

    def get_value(self):
        return self.value

    def broadcast(self):
        if not (self.reader is None):
            pass#self.reader()
        else:
            print "<%s> %s" %(self.name, '\n'.join(self.value)),
