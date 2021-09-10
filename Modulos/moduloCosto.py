class edificio:
  vpe=5000000
  def __init__(self, naltura, npisos = 5):
    self.pisos = npisos 
    self.altura = naltura
  def costos(self):
    costo=self.pisos*self.altura*self.vpe 
    return costo


class edificiogen(edificio):
  vpe = 5000000


version=2

def getVersion():
  return "Vewrsion: " + str(version)

class edificiopis(edificio):
  def __init__(self, naltura, npisc, npisos = 5):
    self.pisos = npisos 
    self.altura = naltura
    self.pisc = npisc
  def costos(self):
    costo = (self.pisos*self.altura*self.vpe)+(4000000*self.pisc)
    return costo


class edificiocan(edificio):
  def __init__(self, naltura, ncanch, npisos = 5):
    self.pisos = npisos 
    self.altura = naltura
    self.canch = ncanch
  def costos(self):
    costo = (self.pisos*self.altura*self.vpe)+(10000000*self.canch)
    return costo
