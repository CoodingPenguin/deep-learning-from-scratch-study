class Man:
    def __init__(self, name):
        self.name = name
        print("초기화되었습니다!")

    def hello(self):
        print("Hello, I'm " + self.name + "!")

    def goodbye(self):
        print("Goodbye, I'm " + self.name + "!")

man = Man("주형")
man.hello()
man.goodbye()