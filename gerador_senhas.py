import random
import string

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

if __name__ == "__main__":
    senha = gerar_senha(8)
    print("Senha gerada:", gerar_senha(8))

    if len(senha) >= 8:
        print("Senha forte, boa escolha!")
    else:
        print("Senha fraca, escolha uma senha com no mínimo 8 caracteres.")
else:
    print("Módulo de geração de senhas importado.") 
