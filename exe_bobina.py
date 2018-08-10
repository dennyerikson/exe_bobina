peso_total = 4500

medidas = [357,357,264,259,163]

for medida in medidas:
    print("Medida: " + str(medida) + " Peso: " + str(medida * (peso_total/sum(medidas))) + " kg")
