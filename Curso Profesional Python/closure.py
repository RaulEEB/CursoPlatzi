def run(text: str):
    assert type(text) == str, "Solo puedes utilizar cadenas."
    def saludo(number: int):
        return text * number
    return saludo

def make_division_by(number1):
    assert type(number1) == int, "Dede de ser un número"
    assert number1 > 0, "Dede de ser mayor a cero."
    def division_by(number2):
        assert type(number2) == int, "Dede de ser un número."
        assert number2 > 0, "Dede de ser mayor a cero."
        return round(number2 / number1)
    return division_by

if __name__ == "__main__":
    text = run("Hola Vilma, ")
    print(text(3))
    
    division_by_3 = make_division_by(3)
    print(division_by_3(18))

    division_by_5 = make_division_by(5)
    print(division_by_5(100))

    division_by_18 = make_division_by(18)
    print(division_by_18(54))