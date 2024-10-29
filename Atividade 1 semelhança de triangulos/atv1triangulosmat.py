def ladosProporcionais(lado1, lado2):
    # Verifica se os lados são proporcionais
    proporcao = lado1[0] / lado2[0]
    return all(round(lado1[i] / lado2[i], 5) == round(proporcao, 5) for i in range(1, len(lado1)))

def verificarLAL(lados1, angulo1, lados2, angulo2):
    # Verifica se dois lados são proporcionais e o ângulo entre eles é congruente
    if round(angulo1, 5) == round(angulo2, 5):
        return ladosProporcionais([lados1[0], lados1[1]], [lados2[0], lados2[1]])
    return False

def verificarLLL(lado1, lado2):
    # Verifica se todos os lados são proporcionais
    return ladosProporcionais(lado1, lado2)

def verificarAA(angulo1, angulo2):
    # Verifica se dois ângulos são congruentes
    return round(angulo1, 5) == round(angulo2, 5)

def verificarSemelhanca(triangulo1, triangulo2):
    resultado = ""
    verificou = False

    # Verificar LAL
    if 'lados' in triangulo1 and 'angulo' in triangulo1:
        if verificarLAL(triangulo1['lados'], triangulo1['angulo'], triangulo2['lados'], triangulo2['angulo']):
            resultado += "Triângulos são semelhantes pelo critério LAL: Dois lados proporcionais e o ângulo entre eles congruente.\n"
            verificou = True
        else:
            resultado += "Os triângulos NÃO são semelhantes pelo critério LAL.\n"

    # Verificar LLL
    if 'lados' in triangulo1 and 'lados' in triangulo2:
        if verificarLLL(triangulo1['lados'], triangulo2['lados']):
            resultado += "Triângulos são semelhantes pelo critério LLL: Todos os lados proporcionais.\n"
            verificou = True
        else:
            resultado += "Os triângulos NÃO são semelhantes pelo critério LLL: Os lados NÃO são proporcionais.\n"

    # Verificar AA (ângulo entre os dois lados)
    if 'angulo' in triangulo1 and 'angulo' in triangulo2:
        if verificarAA(triangulo1['angulo'], triangulo2['angulo']):
            resultado += "Triângulos são semelhantes pelo critério AA: Ângulos entre os lados congruentes.\n"
            verificou = True
        else:
            resultado += "Os triângulos NÃO são semelhantes pelo critério AA.\n"

    if not verificou:
        return "Os triângulos não são semelhantes por nenhum critério."
    return resultado

# Função para receber os dados de entrada do usuário
def obter_dados_triangulo(numero):
    triangulo = {}

    lados = input(f"Indique os dois lados do triângulo {numero} separados por espaço: ").split()
    triangulo['lados'] = list(map(float, lados))

    angulo = float(input(f"Indique o ângulo entre os dois lados do triângulo {numero}: "))
    triangulo['angulo'] = angulo

    return triangulo

# Executar o programa
triangulo1 = obter_dados_triangulo(1)
triangulo2 = obter_dados_triangulo(2)

resultado = verificarSemelhanca(triangulo1, triangulo2)
print(resultado)