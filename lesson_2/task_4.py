# 4. Реализовать возможность переустановки значения цены товара.
# Необходимо, чтобы и родительский, и дочерний классы получили новое значение цены.
# Следует проверить это, вызвав соответствующий метод родительского класса и функцию дочернего (функция,
# отвечающая за отображение информации о товаре в одной строке).


class ItemDiscount:
    def __init__(self, name, price):
        self._name = name
        self._price = price


class ItemDiscountReport(ItemDiscount):
    def __init__(self, name, price):
        super().__init__(name, price)

    def set_price(self, price):
        self._price = price

    def get_parent_data(self):
        print(self._name, self._price)


child = ItemDiscountReport('sale', 10)
child.set_price(30)
print(child.get_parent_data())
