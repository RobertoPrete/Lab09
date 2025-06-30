from dataclasses import dataclass

from model.airport import Airport


@dataclass
class Rotta:
    a1: Airport
    a2: Airport
    distanza_totale: float
    numero_voli: int

    def __post_init__(self):
        self.avgDistance = float(self.distanza_totale / self.numero_voli)

    @property
    def a1(self):
        return self._a1

    @a1.setter
    def a1(self, value):
        self._a1 = value

    @property
    def a2(self):
        return self._a2

    @a2.setter
    def a2(self, value):
        self._a2 = value

    @property
    def totDistance(self):
        return self._distanza_totale

    @totDistance.setter
    def totDistance(self, value):
        self._distanza_totale = value

    @property
    def nVoli(self):
        return self._numero_voli

    @nVoli.setter
    def nVoli(self, value):
        self._numero_voli = value

    @property
    def avgDistance(self):
        return self._avgDistance

    @avgDistance.setter
    def avgDistance(self, value):
        self._avgDistance = value

