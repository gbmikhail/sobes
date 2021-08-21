# 3. Усовершенствовать родительский класс таким образом, чтобы получить доступ к защищенным переменным.
# Результат выполнения заданий 1 и 2 должен быть идентичным.


class ItemDiscount:
    def __init__(self, name, price):
        self._name = name
        self._price = price


class ItemDiscountReport(ItemDiscount):
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def get_parent_data(self):
        print(self._name, self._price)


child = ItemDiscountReport('sale', 10)
print(child.get_parent_data())
