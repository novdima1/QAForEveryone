class Color:
    def __init__(self):
        # object attributes
        self.name = 'Default Color'
        self.lg = self.Lightgreen()

    def show(self):
        print("Name:", self.name)

    class Lightgreen:
        def __init__(self):
            self.name = 'Light Green'
            self.code = '024avc'

        def display(self):
            print("Name1:", self.name)
            print("Code1:", self.code)


class Canvas(Color):
    pass

canvas = Canvas()
canvas.lg.display()

# Change 1
# Change 2
# Change 3.1

