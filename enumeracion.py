def enumeracion():

    vars=[]
    res = 0
    restriccion= []
    obj = []
    condicion= []

    vars = input_int("Ingresa el número de variables: ")
    res = input_int("Ingresa el número de restricciones: ")

    print('Coeficientes para la función objetivo')
    for i in np.arange(vars):
        obj.append(input_int("Coeficiente para x{} : ".format(i)))

    print("Coeficientes para restricciones (ax0+bx1+..+gxn<=c)")
    for i in np.arange(res):
        restlst= []
        restb = 0
        for j in np.arange(vars):
            restlst.append(input_int("Coeficiente de x{} para reestricción {}: ".format(j, i)))
        restb = input_int("Valor b para reestricción {}: ".format(i))

        print("\nRestricciones ingresadas: {} {} {}".format("".join([" ({})x{} +".format(val, idx) for idx, val in enumerate(restlst)])[:-1], "<=", restb))
        restriccion.append(restlst)
        condicion.append(restb)

    obj = np.array(obj)
    restriccion = np.array(restriccion)
    condicion= np.array(condicion)
    print('Maximizar Z=', obj, '\n')
    print('s.a\n')

    print(restriccion, condicion)

    valores = np.array(list(it.product([0, 1], repeat=vars)))

    z = np.array(obj * valores)

    splitarray = np.split(restriccion, res)

    rs = np.array(splitarray * valores)

    maxz = [sum(z[i]) for i in range(len(z))]
    maxz = np.array(maxz)

    lista = []
    for j in range(len(rs)):
        lista2= []
        lista.append(lista2)
        for l in range(len(rs[j])):
            sumrs = sum(rs[j][l])
            np.array(sumrs)
            soluciones = np.all(sumrs <= condicion[j])
            lista2.append(soluciones)

    lista = np.array(lista)
    lista = np.transpose(lista)

    lista3= []
    for j in lista:
        lista3.append(np.all(j == True))
    maximo = maxz[lista3].max()
    print("\nEste es el valor de Z: ", maximo)

    index_max = np.where(maxz[lista3] == maximo)[0][0]

    print("\nResultado: ")
    print((valores[lista3][index_max]))
    