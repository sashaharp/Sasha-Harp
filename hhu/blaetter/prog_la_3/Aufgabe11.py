#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Element(object):
    
    def __init__(self, name, symbol, ordNum, schmelzP, siedeP, Temp = 20.):
        self.Name = name
        self.Symbol = symbol
        self.Ordnungszahl = ordNum
        self.Schmelzpunkt = schmelzP
        self.Siedepunkt = siedeP
        self.Temperatur = Temp

    @property
    def Aggregatzustand(self):
        if self.Temperatur < self.Schmelzpunkt:
            return "fest" 
        elif self.Temperatur < self.Siedepunkt:
            return "flüssig"
        else:
            return "gasförmig"

    def aendereTemperatur(self, temp):
        self.Temperatur = temp
        if temp<-273.15:
            self.Temperatur = -273.15

    def eigenschaften(self):
        print("Name: {0} ({1})\nTemperatur: {2}°C ({3})".format(self.Name, self.Symbol, self.Temperatur, self.Aggregatzustand))

Stickstoff = Element("Stickstoff", "N", 7, -210., -195.795, 25)
Erbium = Element("Erbium", "Er", 68, 1529., 2868., -5.3)
Dysprosium = Element("Dysprosium", "Dy", 66, 1407., 2562.)

Stickstoff.eigenschaften()
Erbium.eigenschaften()
Dysprosium.eigenschaften()

Stickstoff.aendereTemperatur(-200.02)
Erbium.aendereTemperatur(-314.)
Dysprosium.aendereTemperatur(3456.7)

Stickstoff.eigenschaften()
Erbium.eigenschaften()
Dysprosium.eigenschaften()