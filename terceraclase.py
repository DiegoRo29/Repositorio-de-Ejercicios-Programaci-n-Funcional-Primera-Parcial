import utilerias as util
from ops import suma
from ops import resta
from ops import multiplicacion
from ops import division
from ops import cuadrado

# import suma as s
# import resta as r
# import multiplicacion as m
# import division as d
# import cuadrado as c

if __name__ == "__main__":
    util.mensaje("Mensaje dentro de main.py")
    print("La suma es:", suma(4,5))
    print("La resta es:", resta(4,5))
    print("La multiplicacion es:", multiplicacion(4,5))
    print("La division es:", division(4,5))
    # print("suma:", s.suma(4,5))
    # print("Resta:", r.resta(4,5))
    # print("multiplicacion:", m.multiplicacion(4,5))
    # print("division:", d.division(4,5))
    # print("cuadrado:", c.cuadrado(4))