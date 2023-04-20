class Hamburguesa:
    def __init__(self):
        self.tipo = ""
        self.tamanio = ""
        self.salsa = ""
        self.entrega = ""

    def set_tipo(self, tipo):
        self.tipo = tipo

    def set_tamanio(self, tamanio):
        self.tamanio = tamanio

    def set_salsa(self, salsa):
        self.salsa = salsa

    def set_entrega(self, entrega):
        self.entrega = entrega

    def __str__(self):
        return f"Hamburguesa {self.tipo} {self.tamanio} con salsa {self.salsa}. Entrega: {self.entrega}."


class HamburguesaBuilder:
    def __init__(self):
        self.hamburguesa = Hamburguesa()

    def set_tipo(self, tipo):
        self.hamburguesa.set_tipo(tipo)
        return self

    def set_tamanio(self, tamanio):
        self.hamburguesa.set_tamanio(tamanio)
        return self

    def set_salsa(self, salsa):
        self.hamburguesa.set_salsa(salsa)
        return self

    def set_entrega(self, entrega):
        self.hamburguesa.set_entrega(entrega)
        return self

    def build(self):
        return self.hamburguesa




if __name__ == "__main__":
    builder = HamburguesaBuilder()
    builder.set_entrega('delivery').set_salsa('mayones').set_tamanio('XL').set_tipo('comun')
    print(builder.build())

