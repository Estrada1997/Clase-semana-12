class Ordenar:
    def __init__(self, lista):
        self.lista = lista
    def borbuja(self):
        for i in range(len(self.lista)):
            for j in range(i + 1, len(self.lista)):
                if self.lista[i] > self.lista[j]:
                    aux = self.lista[i]
                    self.lista[i] = self.lista[j]
                    self.lista[j] = aux
    def insertar(self, valor):
        self.borbuja()
        aux_lista = []
        enc = False
        for pos, ele in enumerate(self.lista):
            if ele > valor:
                aux_lista.append(valor)
                enc = True #enontrado
                break
        if enc == True:
            self.lista = self.lista[0:pos] + aux_lista + self.lista[pos:]
        else:
            self.lista.append(valor)
        return aux_lista
   #manipular las lineas
        # def insertar2(self, valor):
        # self.borbuja()
        # aux_lista = []
        # enc = False
        # for pos, ele in enumerate(self.lista):
        #     if ele > valor:
        #         aux_lista.append(valor)
        #         enc = True #enontrado
        #         break
        # if enc == True:
        #     #for i in range(pos):
        #     aux_lista.apppend(self.lista[i])
        # aux_lista. append(valor)
        # for j in range(pos, len(self.lista)):
        #     aux_lista.append(self.lista[j])
        # self.lista= aux_lista

        # else:
        #     self.lista.append(valor)
        # return aux_lista

ord1 = Ordenar([1,6,8,2,0])
ord1.insertar(5)
ord1.borbuja()
