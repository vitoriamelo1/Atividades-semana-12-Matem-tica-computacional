# Função para avaliar as proposições
def avaliar_proposicoes(P, Q, M):
    # Proposição R: A festa é animada
    R = (P and Q) or (P or Q) or (not P and M)  # Avalia R com base nas condições
    return R

# Função para gerar a tabela verdade
def tabela_verdade(P, Q, M):
    print(f"{'P':<5} {'Q':<5} {'M':<5} {'R':<5}")  # Cabeçalho da tabela
    print("P: Vitoria vai à festa.")
    print("Q: Jorge vai à festa.")
    print("M: Jorge traz música.")
    print("R: A festa é animada.")
    print("-" * 30)  # Linha separadora

    # Avalia R
    R = avaliar_proposicoes(P, Q, M)
    print(f"{int(P):<5} {int(Q):<5} {int(M):<5} {int(R):<5}")  # Exibe os valores

# Função principal
def main():
    # Receber valores do usuário
    P_input = input("Vitoria vai à festa? (s/n): ").strip().lower()
    Q_input = input("Jorge vai à festa? (s/n): ").strip().lower()
    M_input = input("Jorge traz música? (s/n): ").strip().lower()

    # Converter entradas para valores booleanos
    P = P_input == 's'
    Q = Q_input == 's'
    M = M_input == 's'

    # Gerar a tabela verdade
    tabela_verdade(P, Q, M)

# Executar a função principal
if __name__ == "__main__":
    main()