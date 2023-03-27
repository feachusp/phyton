a = float(input("Entre com o tamanho do lado A do triangulo: "))
b = float(input("Entre com o tamanho do lado B do triangulo: "))
c = float(input("Entre com o tamanho do lado C do triangulo: "))

if (a > b + c) or (b > a + c) or (c > a + b):
    print("Os valores não formam um triangulo!")
elif a == b and a == c and b == c:
    print("Triangulo Equilatero!")
elif a == b or a == c or b == c:
    print("Triangulo Isosceles!")
elif a != b and a != c and b != c:
    print("Triangulo Escaleno!")