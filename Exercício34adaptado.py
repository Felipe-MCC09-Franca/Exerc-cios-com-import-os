import os

# Declaração de variáveis
valor: int = 0
dir: str = ""
arq: str = ""
arquivo: str = ""
dir = "/tmp/exercicios/"
arq = "ex34.txt"

# Inicio

def grava(c, rslt):
    global dir
    global arq
    global arquivo
    tipo: str = ""
    enc: str = ""
    linha: str = ""

    linha = str(c) + " " + str(rslt) + "\n"
    arquivo = dir + arq

    if(os.path.exists(dir) and os.path.isdir(dir)):
        tipo = "w"
        enc = "utf-8"
        if(os.path.exists(arquivo) and c > 0):
            tipo = "a"
        with open(arquivo, tipo, encoding = enc) as file:
            file.write(linha)

def mult(vlr, tab):
    res: int = 0

    res = vlr * tab
    return res


def main():
    global valor
    contador: int = 1
    result: int = 0

    if not os.path.exists(dir):
        os.makedirs(dir, exist_ok = True)
    os.chmod(dir, 0o744)

    valor = int(input("Digite um valor de 1 a 10: "))
    for i in range(1, 11, 1):
        result = mult(valor, contador)
        grava(contador, result)
        print(f"{valor} * {contador} = {result}")
        contador += 1


if __name__ == '__main__':
    main()

# Fim