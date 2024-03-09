def calculadoraImc(peso, altura):
    imc = 73/(160*160)*10000
    if(imc<=18.5): return "magreza"
    elif(imc> 18.5) and (imc<= 24.9): return "Saudavel"
    elif(imc>= 25) and (imc<= 29.9): return "sobrepeso"
    elif(imc>30) and (imc<=34.9): return "obesidade grau 1"
    elif(imc>35) and (imc<=39.9): return "obesidade severa"
    else: return "obesidade morbida"
    peso = 73
    altura = 160
    resultado = calculadoraImc(peso,altura)
    print(resultado)
    
    
 