import numpy as np
import random as rd
import collections

from config import CONFIG
balotos = [
[6,12,24,25,28,15],
[6,19,23,27,35,10],
[12,17,22,36,43,11],
[1,8,9,22,34,2],
[6,7,11,27,42,15],
[1,3,21,30,39,15],
[20,21,23,32,42,14],
[4,10,15,33,37,1],
[3,9,13,21,27,7],
[1,12,18,26,39,11],
[1,21,36,41,42,16],
[5,21,24,34,43,3],
[2,24,32,38,42,10],
[19,25,32,38,41,13],
[6,29,31,36,41,6],
[2,3,10,29,43,16],
[16,33,36,39,43,6],
[6,7,18,25,41,16],
[3,11,21,22,36,11],
[14,18,26,32,42,1],
]

max_pob_cruzados = 0


def getPoblacion(numero):
  return [getIndividuo() for i in range (numero)]

def getIndividuo():
  return [rd.randint(CONFIG.RANDMIN,CONFIG.RANDMAX) for x in range(CONFIG.LENPROGENITOR)]

def LOX(child, progenitor, poblacionCruzada):
  indice = []
  for i in range(4):
    num = np.random.randint(0,5)
    while num in indice:
      num = np.random.randint(0,5)
    child[num] = progenitor[num]
    indice.append(num)
  index_map = collections.defaultdict(list) # Mapa para almacenar los indices de cada número
  # Recorrer el array y registrar los índices
  for index, num in enumerate(child):
    index_map[num].append(index)
  # Filtrar numeros que tienen más de un indice (repetidos)
  repeated_indices = {num: indices for num, indices in index_map.items() if len(indices) > 1}
  if len(repeated_indices) > 0:
    indexers = len(repeated_indices)-1
    for index in repeated_indices:
      position = len(repeated_indices[index]) - 1
      for i in progenitor:
        if i in child:
          continue
        else:
          if indexers >= 0:
            child[repeated_indices[index][position]] = i
            indexers -= 1
            position -= 1
          else:
            poblacionCruzada.append(child)
            break
  else:
    poblacionCruzada.append(child)


def AuxiliarCruce(child, parent):
  indexers = []
  for i in range(4):
    num = np.random.randint(0,5)
    while num in indexers:
      num = np.random.randint(0,5)
    child[num] = parent[num]
    indexers.append(num)
  return child

def FuncionCruce(padre, madre):
  # if len(padre[0]) != 6 or len(madre[0]) != 6:
  #  raise ValueError("Los arrays deben tener una longitud de 6 elementos.")
  poblacionCruzada = []
  for i in range(CONFIG.MAXPOBCRUZ):
    # child1 = [0,0,0,0,0,0]
    # child2 = [0,0,0,0,0,0]
    child1 = padre[0].copy()
    child2 = madre[0].copy()
    # child1 = AuxiliarCruce(child1, madre[0])
    # child2 = AuxiliarCruce(child2, padre[0])
    LOX(child1, madre[0], poblacionCruzada)
    LOX(child2, padre[0], poblacionCruzada)
  return poblacionCruzada

def FuncionMutacion(poblacionCruzada):
  temp = 0
  for i in range(len(poblacionCruzada)-1):
    if rd.random() <= CONFIG.PROBMUTACION:
     
      punto = rd.randint(0, CONFIG.LENPROGENITOR-1)
      while temp == punto:
        punto = rd.randint(0, CONFIG.LENPROGENITOR-1)
      temp = punto
      nuevo_valor = rd.randint(CONFIG.RANDMIN, CONFIG.RANDMAX)
      while nuevo_valor in poblacionCruzada[i]:
       nuevo_valor = rd.randint(CONFIG.RANDMIN, CONFIG.RANDMAX)
      poblacionCruzada[i][punto]=nuevo_valor
  return poblacionCruzada


def objective_function(input_array, new_array):
    total_difference = sum(abs(a - b) for a, b in zip(sorted(input_array), sorted(new_array)))
    return total_difference

def By_Probability(objetiveProb, poblacionAletatoria, probabilityBalotos):
  maxProb_Al_top_6_numbers = 0
  ArrayProb_Al = []
  for i in poblacionAletatoria:
      for y in i:
        if y in probabilityBalotos:
            maxProb_Al_top_6_numbers +=probabilityBalotos[y]
        #print(maxProb_Al_top_6_numbers)
      ArrayProb_Al.append(([i],maxProb_Al_top_6_numbers))
      maxProb_Al_top_6_numbers = 0
  #print(ArrayProb_Al)
  ArrayProb_Al.sort(key=lambda x: x[1], reverse=True)
  #print("**********************")
  #print(ArrayProb_Al)
  return ArrayProb_Al

def mainExce(maxPoblation,nIteraciones, maxPoblacion_Cruzados):
  max_pob_cruzados = int(maxPoblacion_Cruzados)
  totalInd = int(maxPoblation)
  #POBLACION ALEATORIA
  poblacionAletatoria = getPoblacion(totalInd)
  #print(poblacionAletatoria)
  #FIN

  #POBLACION BALOTOS
  flat_array = [num for sublist in balotos for num in sublist]
  counter = collections.Counter(flat_array)
  total_elements = len(flat_array)
  probabilityBalotos = {num: count / 43 for num, count in counter.items()}
  top_6_Balotos = sorted(probabilityBalotos, key=probabilityBalotos.get, reverse=True)[:6]
  maxProb_Bal_top_6_numbers = 0
  for i in top_6_Balotos:
      if i in probabilityBalotos:
          maxProb_Bal_top_6_numbers +=probabilityBalotos[i]
  #print(maxProb_Bal_top_6_numbers)
  #FIN

  # #POBLACION ALEATORIA
  # maxProb_Al_top_6_numbers = 0
  # ArrayProb_Al = []
  # for i in poblacionAletatoria:
  #     for y in i:
  #       if y in probabilityBalotos:
  #           maxProb_Al_top_6_numbers +=probabilityBalotos[y]
  #       #print(maxProb_Al_top_6_numbers)
  #     ArrayProb_Al.append(([i],maxProb_Al_top_6_numbers))
  #     maxProb_Al_top_6_numbers = 0
  # #print(ArrayProb_Al)
  # ArrayProb_Al.sort(key=lambda x: x[1], reverse=True)
  # #print("**********************")
  # #print(ArrayProb_Al)
  # #FIN


  # arrayObjetivo = []
  # if objetivo != None:
  #   objetivo = objetivo.split(',')
  #   for number in objetivo:
  #     try:
  #       arrayObjetivo.append(int(number))
  #     except:
  #       continue
  #   top_6_Balotos = arrayObjetivo
  ArrayProb_Al = By_Probability(maxProb_Bal_top_6_numbers, poblacionAletatoria, probabilityBalotos)
  # if objetivo != None:
  #   top_6_Balotos = objetivo
  bestSolutionByIteration = []
  for interation in range(int(nIteraciones)):
    print(interation+1)
    if len(ArrayProb_Al) > 1:
      padre = ArrayProb_Al[0]
      madre = ArrayProb_Al[1]
      ArrayProb_Al.clear()
      poblacionCruzada = FuncionCruce(padre[0], madre[0])
      # print(f"Total poblacion: {len(poblacionCruzada)}")
      # for i in poblacionCruzada:
      #   print(i)
      poblacionMutada = FuncionMutacion(poblacionCruzada)
      ArrayProb_Al = By_Probability(maxProb_Bal_top_6_numbers, poblacionMutada, probabilityBalotos)
      #SELECCION POR FUNCION OBJETIVO
      # for posibleSol in poblacionMutada:
      #   result = objective_function(top_6_Balotos, posibleSol)
      #   ArrayProb_Al.append(([posibleSol], result))
      # ArrayProb_Al.sort(key=lambda x: x[1], reverse=False)
      # try:
      if ArrayProb_Al[0][1] >= 0.283:
        print("Alguna solucion encontrada")
        bestSolutionByIteration.append(ArrayProb_Al[0])
        bestSolutionByIteration.append(ArrayProb_Al[1])
        bestSolutionByIteration.append(ArrayProb_Al[2])
      #     print(ArrayProb_Al[0])
      #     print(ArrayProb_Al[1])
      #     print(f"Total iteraciones: {interation}")
      #     break
      # except Exception as Err:
      #   return 0, Err, interation+1, top_6_Balotos
    else:
      print('************ Break by Poblation < 1 - Exception **************')
      print(f'Mejor resultado 1: {padre[0]}, probabilidad: {padre[1]}')
      print(f'Mejor resultado 2: {madre[0]}, Probabilidad: {madre[1]}')
      print(f'Objetivo: {top_6_Balotos}, Probabilidad: {maxProb_Bal_top_6_numbers}')
  print('************ Break Iteration **********')
  print(f'Mejor resultado 1: {padre[0]}, probabilidad: {padre[1]}')
  print(f'Mejor resultado 2: {madre[0]}, Probabilidad: {madre[1]}')
  print(f'Objetivo: {top_6_Balotos}, Probabilidad: {maxProb_Bal_top_6_numbers}')
  return ArrayProb_Al[0], ArrayProb_Al[1], interation+1, top_6_Balotos


mainExce(20, 10000, 32)