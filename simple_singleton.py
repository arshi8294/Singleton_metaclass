class Singleton:
    
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance
    

if __name__ == '__main__':
    
    s1 = Singleton()
    s2 = Singleton()
    print(s1 is s2)