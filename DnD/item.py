class Item:
    def __init__(self, name, weight, value):
        self._name = name
        self._weight = weight
        self._value = value

    def __str__(self):
        return self._name

    def get_weight(self):
        return self._weight

    def get_value(self):
        return self._value

    def get_attr(self):
        return (self._weight, self._value)
