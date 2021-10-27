class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color): 
        if (color == self.color):
            pass
        else:
            if (color == 'rojo' or color == 'verde' or color == 'amarillo' or color == 'negro' or color == 'blanco'):
                self.color = color 
            else:
                pass    

class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):   
        for i in self.asientos:
            if (i is None):
                pass
            else:
                self.cantidadCreados+=1

        return self.cantidadCreados

    def verificarIntegridad(self):
        cIguales = 0
        cTotales= 0
        if (self.registro != self.motor.registro):
            print("Las piezas no son originales")
        else:
            for i in self.asientos:
                if (i is None):
                    pass
                else:
                    cTotales+=1
                    if (self.registro == i.registro):
                        cIguales+=1
                    else:
                        pass                  
            if(cIguales==cTotales):
                print("Auto original")
            else:
                print("Las piezas no son originales") 
        


class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, nregistro):
        self.registro = nregistro

    def asignarTipo(self, nmotor):
        if (nmotor == 'electrico' or nmotor == 'gasolina'):
            self.tipo = nmotor
        else:
            pass         
