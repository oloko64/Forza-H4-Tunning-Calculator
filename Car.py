class Carro:
    def __init__(self, peso, distr_peso, rig_mola, barra_20):
        self.peso = peso
        self.distr_peso = distr_peso
        self.rig_mola = rig_mola
        self.barra_20 = barra_20

    def suspencaoFront(self):
        final = (self.peso * (self.rig_mola / 100)) * (self.distr_peso / 100)
        return round(final, 2)

    def suspencaoRear(self):
        final = (self.peso * (self.rig_mola / 100)) * ((100 - self.distr_peso) / 100)
        return round(final, 2)

    def dampingFront(self):
        final = self.barra_20 * (self.distr_peso / 100)
        return round(final, 2)

    def dampingRear(self):
        final = self.barra_20 * ((100 - self.distr_peso) / 100)
        return round(final, 2)

    def reboundFront(self):
        final = self.dampingFront() * 0.5
        return round(final, 2)

    def reboundRear(self):
        final = self.dampingRear() * 0.5
        return round(final, 2)
