def classificar_triangulo(a: int, b: int, c: int) -> str:
    if a <= 0 or b <= 0 or c <= 0:
        return "nao e um triangulo"

    if a + b <= c or a + c <= b or b + c <= a:
        return "nao e um triangulo"

    if a == b == c:
        return "equilatero"
    if a == b or a == c or b == c:
        return "isosceles"
    return "escaleno"
