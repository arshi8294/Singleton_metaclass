class Singleton:

    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, value):
        self.value = value


if __name__ == '__main__':

    s1 = Singleton(1)
    s2 = Singleton(1111)
    
    print(s1.value, s2.value)
    print(s1 is s2)
