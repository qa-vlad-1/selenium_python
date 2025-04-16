
class parent:
    def __init__(self):
        print("This is Parent")


class child(parent):
    def __init__(self):
        super().__init__()
        print("This is Child")


cc = child()
print(cc)








