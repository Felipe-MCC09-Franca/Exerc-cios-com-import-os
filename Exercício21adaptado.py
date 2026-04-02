import os

# Declaração de variáveis
nome: str = ''
nota1: float = 0.0
nota2: float = 0.0
nota3: float = 0.0
nota4: float = 0.0
valor_media: float = 0.0
dir: str = ''
arq: str = ''

dir = '/tmp/exercicios/'
arq = 'ex21.txt'

# Inicio

def med(n1, n2, n3, n4):
    media: float = 0.0
    media = (n1 + n2 + n3 + n4) / 4
    return media

def escreveArq(caminho, arquivo, linha_arq):
    file: str = ''
    tipo: str = ''
    enc: str = ''
    
    enc = "utf-8"
    caminho_completo = os.path.join(caminho, arquivo)

    if os.path.exists(caminho) and os.path.isdir(caminho):
        tipo = "w"
        if os.path.exists(caminho_completo):
            tipo = "a"
        
        with open(caminho_completo, tipo, encoding=enc) as f:
            f.write(linha_arq)

def cadastro(nm, nt1, nt2, nt3, nt4, vlr_med):
    global dir, arq
    linha: str = ""
    
    linha = nm + ";" + str(nt1) + ";" + str(nt2) + ";" + str(nt3) + ";" + str(nt4) + ";" + str(vlr_med) + "\n"
    
    escreveArq(dir, arq, linha)

def entrada():
    global nome, nota1, nota2, nota3, nota4, valor_media
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    nota3 = float(input("Digite a nota 3: "))
    nota4 = float(input("Digite a nota 4: "))
    
    valor_media = med(nota1, nota2, nota3, nota4)
    
    print(f"Média de {nome}: {valor_media}")
    
    cadastro(nome, nota1, nota2, nota3, nota4, valor_media)

def main():
    pasta = '/tmp/exercicios'
    if not os.path.exists(pasta):
        os.makedirs(pasta)
    os.chmod(pasta, 0o744)
    
    contador: int = 0
    for i in range(5):
        contador = i
        entrada()

if __name__ == '__main__':
    main()

# Fim