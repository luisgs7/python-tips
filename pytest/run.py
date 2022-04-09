from src.calculadora import Calculadora
from src.operations.add import AddOpetarion
from src.operations.sub import SubOperation

calc = Calculadora(AddOpetarion(), SubOperation())

op1 = calc.add(2, 5, True)
op2 = calc.sub(5, 3, True)

print(op1)
print(op2)