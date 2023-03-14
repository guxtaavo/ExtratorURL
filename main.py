url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"

interrogacao = url.find('?')

url_base = url[:interrogacao]
url_parametros = url[interrogacao+1:]

parametro_search = "quantidade"
indice_parametro = url_parametros.find(parametro_search)
indice_valor = indice_parametro + len(parametro_search) + 1
indice_e_comercial = url.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]

print(valor)

