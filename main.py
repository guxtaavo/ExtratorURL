from extrator_url import ExtratorURL

def main():
    url = input("Digite o URL: ")
    nome_parametro = input("Digite o nome do parametro que você queira saber o valor: ")
    extrator_url = ExtratorURL(url, nome_parametro)
    print('O tamanho da url é:', len(extrator_url))

if __name__ == "__main__":
    main()


# url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
