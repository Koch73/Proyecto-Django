class Socio:
    def __init__(self, numero = 0, nombre = "", plan = 0, monto = 0.0):
        self.numero = numero
        self.nombre = nombre
        self.plan = plan
        self.monto = monto

    def __str__(self):
        p =  "{:<25}".format("nro de afiliado: " + str(self.numero))
        p += "{:<25}".format("Nombre: " + str(self.nombre))
        p += "{:<25}".format("Plan: " + str(self.plan))
        p += "{:<25}".format("monto: " + str(self.monto))
        return p
