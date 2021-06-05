import circuit as c

g1 = c.AndGate("G1")
g2 = c.AndGate("G2")
g3 = c.OrGate("G3")
g4 = c.NotGate("G4")
c1 = c.Connector(g1, g3)
c2 = c.Connector(g2, g3)
c3 = c.Connector(g3, g4)
print(g4.getOutput())
