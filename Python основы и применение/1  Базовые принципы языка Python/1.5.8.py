
class MoneyBox:
    def __init__(self, capacity):
        self.coins = 0
        self.capacity = capacity

    def can_add(self, v):
        if self.coins + v <= self.capacity:
            return True
        else:
            return False

    def add(self, v):
        self.coins += v

#
# Как
# ни
# странно, можно
# обойтись
# одним
# атрибутом.
#
#
# class MoneyBox:
#     def __init__(self, capacity):
#         self.capacity = capacity
#
#     def can_add(self, v):
#         return self.capacity >= v
#
#     def add(self, v):
#         self.capacity -= v

