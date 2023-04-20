from abc import abstractmethod


class Factura:
    def __init__(self, importe):
        self.importe = importe

    @abstractmethod
    def calcular_importe(self):
        pass


class FacturaResponsableIVA(Factura):
    def calcular_importe(self):
        return self.importe * 1.21


class FacturaNoInscriptoIVA(Factura):
    def calcular_importe(self):
        return self.importe


class FacturaExentoIVA(Factura):
    def calcular_importe(self):
        return self.importe * 1.0


class FacturaFactory:
    @staticmethod
    def crear_factura(importe, tipo_cliente):
        if tipo_cliente == "Responsable":
            return FacturaResponsableIVA(importe)
        elif tipo_cliente == "No Inscripto":
            return FacturaNoInscriptoIVA(importe)
        elif tipo_cliente == "Exento":
            return FacturaExentoIVA(importe)
        else:
            raise ValueError(f"Tipo de cliente no válido: {tipo_cliente}")




if __name__ == "__main__":
    # Ejemplo de uso:
    factura = FacturaFactory.crear_factura(1000, "Responsable")
    print(f"Importe de la factura con condicion responsable: ${factura.calcular_importe()}")

    factura2 = FacturaFactory.crear_factura(2000, "Exento")
    print(f"Importe de la factura con condicion Exento: ${factura2.calcular_importe()}")

    factura3 = FacturaFactory.crear_factura(500, "No Inscripto")
    print(f"Importe de la factura Exento No Inscripto: ${factura3.calcular_importe()}")


