class Pelicula:
    def __init__(self, id = 0, titulo = "", importe = 0.0, tipo = 0, pais = 0):
        self.id = id
        self.titulo = titulo
        self.importe = importe
        self.tipo = tipo
        self.pais = pais
    def __str__(self):
        p = "{:<30}".format("Codigo identificador: " + str(self.id))
        p += "{:<30}".format("Titulo: " + str(self.titulo))
        p += "{:<40}".format("Importe invertido: " + str(self.importe))
        p += "{:<30}".format("Tipo: " + str(self.tipo))
        p += "{:<30}".format("Pais de origen: " + str(self.pais))
        return p
