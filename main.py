
# Angel Higueros
# 20460
# Laboratorio 2

from redbayes_higueros import Nodo, RedBayesiana
def main():

    cloudy = Nodo("Cloudy", [], {(True,): 0.5, (False,): 0.5})
    sprinkler = Nodo("Sprinkler", [cloudy], {(True, True): 0.1, (True, False): 0.5, (False, True): 0.9, (False, False): 0.5})
    rain = Nodo("Rain", [cloudy], {(True, True): 0.8, (True, False): 0.2, (False, True): 0.2, (False, False): 0.8})
    wet = Nodo("Wet grass", [rain, sprinkler], {
        (True, True, True): 0.99, (True, True, False): 0.9, (True, False, True): 0.9, (True, False, False): 0, 
        (False, True, True): 0.01, (False, True, False): 0.1, (False, False, True): 0.01, (False, False, False): 1})

   
    red = RedBayesiana([cloudy, sprinkler, rain, wet])
    evidencias = {"Sprinkler": True, "Cloudy": False, "Rain": True, "Wet grass": True}

    p_sintomas = red.calcular_probabilidad(evidencias)
    print("Probabilidad conjunta: ", p_sintomas)

    p_marginal = red.obtener_probabilidad_marginal(sprinkler, evidencias)
    print("Probabilidad marginal de sprinkler: ", p_marginal)

    p_condicional = red.obtener_probabilidad_condicional(wet, evidencias)
    print("Probabilidad condicional de Wet Grass dado Sprinkler: ", p_condicional) 



if __name__ == '__main__':
    main()



