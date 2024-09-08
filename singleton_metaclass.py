class Singleton_Meta(type):

    _instance = None
    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super().__call__(*args, **kwargs)
        return self._instance


class Singleton_Class(metaclass=Singleton_Meta):
    pass



if __name__ == "__main__":
    
    s1 = Singleton_Class()
    s2 = Singleton_Class()
    print(s1 is s2)
