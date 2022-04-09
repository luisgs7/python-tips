# pylint: disable-all

from collections import namedtuple

def minha_lista():

    MyList = namedtuple("Compra", "frutas local supermercados extras")

    return MyList(
        frutas=["maçã", "uva", "abacate"],
        local="avenida colinas",
        supermercados=2,
        extras={"doces": "chocolates", "sucos": "laranja"}
    )

lista = minha_lista()

#lista.frutas = ["laranja"]

print(lista)