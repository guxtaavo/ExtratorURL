import re

class ExtratorURL():
    def __init__(self, url, nome_parametro):
        self.url = self.santiza_url(url)
        self.valida_url()
        self.get_valor_parametro(nome_parametro)

    def santiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if self.url == "":
            raise ValueError('A URL está vazia.')

        padrao_url = re.compile('(http(s)?://)?(www.)?[a-z]{1,20}.com(.br)?/[a-z]{1,20}')
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError("A URL não é válida.")
    
    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametro = self.url[indice_interrogacao+1:]
        return url_parametro

    def get_valor_parametro(self, nome_parametro):
        indice_parametro = self.get_url_parametros().find(nome_parametro)
        indice_valor = indice_parametro + len(nome_parametro) + 1
        indice_e_comercial = self.get_url_parametros().find("&", indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + "\n" + "Parâmetros: " + self.get_url_parametros() + "\n" + "URL base: " + self.get_url_base()

    def __eq__(self, other):
        return self.url == other.url
        # Utilizado para comparar dois objetos