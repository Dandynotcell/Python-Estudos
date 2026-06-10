def calcular_imc(peso, altura):
    if altura <= 0:
        raise valueError("A altura precisa ser maior que zero")
    
    imc = peso / (altura ** 2)
    return imc
def classificar_imc(imc):
    if imc <18.5:
        return "abaixo do peso"
    elif imc <25:
        return "peso normal" 
    elif imc < 30:
        return "sobre peso"
    else:       return "obesidade"