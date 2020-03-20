class MyList(list):
    data = None

    def __init__(self, list_object):
        super().__init__()
        if isinstance(list_object, list):
            self.data = list_object[:]
        else:
            self.data = list_object.data[:]

    def __repr__(self):
        return str(self.data)

    def __contains__(self, item):
        return True if item in self.data else False

    def __getitem__(self, index):
        return self.data[index]

    def __add__(self, other):
        self.add(other)
        return MyList(self.data)

    def __iadd__(self, other):
        self.add(other)
        return MyList(self.data)

    def __radd__(self, other):
        self.add(other)
        return MyList(self.data)

    def add(self, alist: list):
        self.data = self.data + alist
