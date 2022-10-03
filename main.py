def maximizar_troca_de_figurinhas(figurinhas_x, figurinhas_y):
  
    controle = 0
    quantidade = 0

    if len(figurinhas_x) < len(figurinhas_y):  
        for x in range(len(figurinhas_x)):
            for y in range(len(figurinhas_y)):
                if figurinhas_x[x] == figurinhas_y[y]:
                    controle += 1
        quantidade = len(figurinhas_x) - controle


    elif len(figurinhas_y) < len(figurinhas_x):
        for x in range(len(figurinhas_y)):
            for y in range(len(figurinhas_x)):
                if figurinhas_y[x] == figurinhas_x[y]:
                    controle += 1
        quantidade = len(figurinhas_y) - controle

                                                              
    else:
        for x in range(len(figurinhas_x)):
            for y in range(len(figurinhas_y)):
                if figurinhas_x[x] == figurinhas_y[y]:
                    controle += 1
        quantidade = len(figurinhas_x) - controle

    return quantidade