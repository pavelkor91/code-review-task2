from abc import ABC, abstractmethod

class Figure(ABC):

    def __init__(self, x: int, y: int, color: bool) -> None:
        self.is_white = color
        self.position_x = x
        self.position_y = y
        self.is_alive = True

    @abstractmethod
    def _validate_move(self, new_x: int, new_y: int) -> bool:
        """своя реализация проверки корректности хода у каждой фигуры"""
        pass

    def kill_figure(self) -> None:
        self.is_alive = False

    def move(self, new_x: int, new_y: int) -> bool:
        if self._validate_move(self,new_x,new_y):
            """Если ход валидный перезаписываем координаты фигуры """
            """Проверка занятости клетки и атака происходит на уровне класса игры"""
            pass

class Pawn(Figure):
    def _validate_move(self, new_x: int, new_y: int) -> bool:
        """"Реализация проверки валидности хода"""
        pass

    def transform_to_queen():
        """Убиваем эту пешку и создаем на ее месте королеву"""
        pass

class Knight(Figure):
    def _validate_move(self, new_x: int, new_y: int) -> bool:
        """"Реализация проверки валидности хода"""
        pass

class King(Figure):
    def _validate_move(self, new_x: int, new_y: int) -> bool:
        """"Реализация проверки валидности хода"""
        pass

class Rook(Figure):
    def _validate_move(self, new_x: int, new_y: int) -> bool:
        """"Реализация проверки валидности хода"""
        pass

class Queen(Figure):
    def _validate_move(self, new_x: int, new_y: int) -> bool:
        """"Реализация проверки валидности хода"""
        pass

class Bishop(Figure):
    def _validate_move(self, new_x: int, new_y: int) -> bool:
        """"Реализация проверки валидности хода"""
        pass


