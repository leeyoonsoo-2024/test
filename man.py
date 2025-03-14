class man:
    def __init__(self, name):
        self.name = name
        print("Initialized!")

    def hello(self):
        print("Hello " + self.name + "!")

    def goodbye(self):
        print("Goodbye " + self.name + "!")

m = man("David")
m.hello()
m.goodbye()


202402387 컴퓨터공학부 이윤수
