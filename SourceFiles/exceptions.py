# Filename: : exceptions.py
# Description: Модуль состоящий из обьектов, что являются кастомными Exception-ами.


class CommandNotFoundException:
    def __init__(self, error: str = 'Command to found exception!') -> object:
        self.error = error
        super().__init__(self.error)

class CantCalculate(Exception):
    def __init__(self, obj: object, error: str = 'Cant calculate value') -> object:
        self.error = error
        self.obj = obj
        super.__init__(self.error)