class DoubleCola:

    def __init__(self):
        pass

    def whoIsNext(self, names, double):
        if double <= len(names):
            return names[double-1]
        return names[(double % len(names))]
