def ler_float(mensagem: str) -> float:
    """Lê um número float do usuário com validação."""
    while True:
        texto = input(mensagem).strip().replace(",", ".")
        try:
            return float(texto)
        except ValueError:
            print("Entrada inválida. Digite um número (ex: 10 ou 10.5).")


def escolher_opcao() -> str:
    """Mostra o menu e retorna uma opção válida."""
    opcoes_validas = {"1", "2", "3", "4", "0"}

    while True:
        print("\n=== CALCULADORA ===")
        print("1 - Somar")
        print("2 - Subtrair")
        print("3 - Multiplicar")
        print("4 - Dividir")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao in opcoes_validas:
            return opcao

        print("Opção inválida. Tente novamente.")


def calcular(opcao: str, a: float, b: float) -> float:
    """Executa a operação escolhida."""
    if opcao == "1":
        return a + b
    if opcao == "2":
        return a - b
    if opcao == "3":
        return a * b
    if opcao == "4":
        if b == 0:
            raise ZeroDivisionError("Divisão por zero não é permitida.")
        return a / b

    # Segurança: se chegar aqui, é erro de lógica no programa
    raise ValueError("Opção de cálculo inválida.")


def main():
    while True:
        opcao = escolher_opcao()

        if opcao == "0":
            print("Saindo da calculadora...")
            break

        a = ler_float("Digite o primeiro número: ")
        b = ler_float("Digite o segundo número: ")

        try:
            resultado = calcular(opcao, a, b)
            print(f"Resultado: {resultado}")
        except ZeroDivisionError as e:
            print(f"Erro: {e}")


if __name__ == "__main__":
    main()