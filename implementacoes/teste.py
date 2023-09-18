def converterBGR2CMYK(bgr):
    altura,largura,channels = bgr.shape
    bgrdash = bgr.astype(np.float64)/255.
    C = 1 - bgrdash[:,:,2]
    M = 1 - bgrdash[:,:,1]
    Y = 1 - bgrdash[:,:,0]
    CMY = np.dstack((C,M,Y))
    minValor = np.min(CMY,2)
    print(minValor[124,0])
    CMYK = np.zeros((altura,largura,4))
    for x in range(altura):
        for y in range(largura):
            if(minValor[y,x] == 1):
                CMYK[y,x] = (0,0,0,1)
            else:
                K = minValor[y,x]
                CMYK[y,x,0] = (C[y,x] - K) / (1 - K)
                CMYK[y,x,1] = (M[y,x] - K) / (1 - K) 
                CMYK[y,x,2] = (Y[y,x] - K) / (1 - K) 
                CMYK[y,x,3] = K 
    return (CMYK*255).astype('uint8')