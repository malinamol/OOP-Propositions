import random
from random import shuffle
from Domain import Cuvant


class Controller:

    def __init__(self, repository):
        self.repository = repository
        self.nr_korrekt=0           #nr prop corect formate (subst+verb+adj)
        self.nr_topik=0             #nr prop care au topica subst+verb+subst+adj
        self.prop=[]                #aici vom pune propozitiile formate (adica liste cu obiecte)

        self.ap_prop=[]             #in aceasta lista (aparitii propozitii), vom crea pentru fiecare
                                    #propozitie o lista ce va contine lista-uri (daca vor exista),
                                    #adica doua valori dintre care prima e nr de cuvinte identice cu
                                    #propozitia din magic.txt si a doua nr propozitiei (adica indicele din lista ei)
                                    #si indicele fiecarei liste din aceasta lista va corespunde numarului propozitiei din self.prop, a celei generate

    #functii definite in repository

    def print_erscheinungen(self):
        return self.repository.print_erscheinung()

    def get_verbe(self):
        return self.repository.get_verbe()

    def get_substantive(self):
        return self.repository.get_substantive()

    def get_adjektive(self):
        return self.repository.get_adjektive()

    def get_magicSazte(self):
        return self.repository.get_magicSatze()

    def get_nr(self):
        return self.nr_korrekt

    def get_prop(self):
        return self.prop


    def prozent(self, nr,n):
        return nr * 100 / n

    def satz(self,a,b,c):
        '''
        input: a-nr maxim de substantive, b- nr maxim de verbe, c-nr maxim de adj
        Functia concateneaza listele de substantive, verbe si adjective, care le obtinem prin apelarea functiilor pe care le-am definit mai jos

        :return:list - o lista unde fiecare element e un cuvant
        '''
        l_subst = self.list_substantive(a)      #apelam functiile definite mai jos
        l_adj = self.list_adjektive(b)
        l_verbe = self.list_verbe(c)
        self.list = l_subst + l_verbe + l_adj
        random.shuffle(self.list)            #organizam aleatoriu elemnetele listei

        if len(l_adj) == 1 and len(l_verbe) == 1 and len(l_subst) == 1:  #daca exista doar cate un cuvant de fiecare tip
            if self.list[0].get_tip()==1 and self.list[1].get_tip()==2 and self.list[2].get_tip()==3:   #daca primul cuvant este substantiv, al doilea verb si al treilea adjectiv
                self.nr_korrekt += 1                #incrementam nr propozitiilor corect formate

        if len(l_adj) == 1 and len(l_verbe) == 1 and len(l_subst) == 2:     #daca nr cuvinte se incadreaza pentru topica subst+verb+subst+adj
            if self.list[0].get_tip() == 1 and self.list[1].get_tip() == 2 and self.list[2].get_tip() == 1 and self.list[3].get_tip() == 3:     #verificam daca avem topica subst+verb+subst+adj
                self.nr_topik+=1
        self.prop.append(self.list)             #adaugam propozitia nou formata in self.prop
        return self.list


    # Urmatoarele trei functii returneaza cate o lista cu cuvintele generate aleatoriu pentru fiecare tip de cuvant(subst, adj si verb)

    def list_substantive(self,n):
        list = []
        nr_cuvinte = random.randint(1, n)  # se vor putea genera maxim 10 cuvinte de un tip
        list_substantive = self.repository.get_substantive()  # obtin lista cu substantive (tip obiect)
        for i in range(0, nr_cuvinte):
            index = random.randint(0, len(list_substantive) - 1)  # obtin un index intre 0 si lungimea sirului de subtantive
            list.append(list_substantive[index])  # pun in list obiectul substantiv de la indexul 'index'
            list_substantive[index].set_aparitii(list_substantive[index].get_aparitii() + 1)
        return list

    def list_adjektive(self,n):
        list = []
        nr_cuvinte = random.randint(1, n)  # se vor putea genera maxim 10 cuvinte de un tip
        list_adjektive = self.repository.get_adjektive()  # obtin lista cu adjective
        for i in range(0, nr_cuvinte):
            index = random.randint(0,len(list_adjektive) - 1)  # obtin un index intre 0 si lungimea sirului de subtantive
            list.append(list_adjektive[index])  # pun in list cuvantul din lista de adjective
            list_adjektive[index].set_aparitii(list_adjektive[index].get_aparitii() + 1)  # crestem numarul de aparitii al cuvantului
        return list

    def list_verbe(self,n):
        list = []
        nr_cuvinte = random.randint(1, n)  # se vor putea genera maxim 10 cuvinte de un tip
        list_verbe = self.repository.get_verbe()  # obtin lista cu verbe
        for i in range(0, nr_cuvinte):
            index = random.randint(0, len(list_verbe) - 1)  # obtin un index intre 0 si lungimea sirului de subtantive
            list.append(list_verbe[index])  # pun in list cuvantul din lista de verbe
            list_verbe[index].set_aparitii(list_verbe[index].get_aparitii() + 1)
        return list

    """
    LAB 7
    """

    def gleich_worter(self):
        nr=0

        #comparam elementele din cele doua liste unul cate unul

        magicSatze=self.repository.get_magicSatze()
        satze= self.prop
        for i in range (0, len(satze)):    #parcurg lista mare cu propozitiile generate
            for j in range(0, len(magicSatze)):       #iau fiecare lista cu obiecte pe rand
                nr = 0  # pentru fiecare propozitie din magicSatze reinitializam nr cu 0
                for k in range(0, len(satze[i])):     #parcurg lista mare cu propozitii magice
                    for l in range(0, len(magicSatze[j])):      #si compar cu elementele din magicSatze
                       if satze[i][k].get_cuvant() == magicSatze[j][l] :       #daca doua cuvinte sunt egale
                           nr+=1                                    #crestem numarul cuvintelor care coincid
                if nr!=0:                                           #punem nr de cuvinte identice in lista doar daca exista astfel de cuvinte
                    self.ap_prop.append([i,nr, j])                 #primul element dn lista e nr propozitiei generate (i), al doilea e nr
                                                                    # de cuvinte identice, iar al treilea
                                                                    #e nr propozitiei magice unde se afla aceste cuvinte, adica j
        # return self.ap_prop

    def satze_identisch(self):
        '''
        Vom avea lista cu liste unde pe pozitia 0 e numarul propozitiei generate, pe 1 e nr de cuvinte
        comune cu propozitia magica, iar pe 3 e numarul propozitiei magice din fisier
        
        :return: O lista cu indicii propozitiilor care se gasesc si in magicSatze
        '''
        satz_id=[]
        ok=1            #presupunem ca toate cuvintele dintr-o propozitie sunt in aceeasi ordine
        magic=self.get_magicSazte()
        aparitii=self.ap_prop
        for i in range(0, len(aparitii)):   #parg fiecare lista
            ok=1
            if len(self.prop[ aparitii[i][0] ]) == aparitii[i][1] :     # self.ap_prop[i][0] imi va da indicele propozitiei generate,
                                                                                # si verific daca lungimea acestei propozitii, adica nr de cuvinte,
                                                                                # coincide cu valoarea de pe pozitia 1 din lista

                for j in range( 0, aparitii[i][1] ):     #vom compara cuvintele din cele 2 prop pt a verifica daca sunt si in aceeasi ordine
                    if magic[aparitii[i][2]][j] != self.prop[aparitii[i][0]][j].get_cuvant() :
                        ok=0
                if ok==1:
                    satz_id.append(aparitii[i][0])          #adaug indicele propozitiei generate in lista

        return satz_id

    def equality_prozent(self):
        '''
        Parcurg lista cu liste (unde am tripletul cu nr propozitiei, nr de cuvite comune si nr propozitiei magice),
        iar la sfarsitul fiecarei liste mai adaug si procentul de egalitate
        '''

        for i in range(0, len(self.ap_prop)):

            # self.ap_prop[i][1] imi va da nr de cuvinte comune dintre o propozitie generate si una magica
            # len(propozitii[aparitii[i][0]]) imi va da nr de cuvinte din propozitia generata

            prozent=self.prozent( self.ap_prop[i][1] , len(self.prop[self.ap_prop[i][0]]) )
            self.ap_prop[i].append(int(prozent))
        return self.ap_prop

    #creez o propozitie pt testul de egalitate cu ultimul cuvant din fiecare lista, pe care l-am adaugat in repository dupa citirea din fisier
    def test(self):
        list=[]
        subst=self.get_substantive()
        verbe=self.get_verbe()
        adj=self.get_adjektive()
        list.append(adj[len(adj)-1])
        list.append(subst[len(subst)-1])
        list.append(verbe[len(verbe)-1])
        self.prop.append(list)


    """
    LAB 8
    """
    #prima metoda de sortare, pe care o vom folosi pt cerinta 2
    def mergeSort(self,cuvant):
        if len(cuvant) > 1:
            mid = len(cuvant) // 2  # obtinem un numar intreg
            left = cuvant[:mid]  # impartim in doua liste pana ajungem la liste cu un element
            right = cuvant[mid:]

            self.mergeSort(left)  # sortam prima jumatate
            self.mergeSort(right)  # sortam a doua jumatate

            i = 0
            j = 0
            k = 0
            while i < len(left) and j < len(right):
                if left[i].get_aparitii() < right[j].get_aparitii():
                    cuvant[k] = left[i]
                    i = i + 1
                else:
                    cuvant[k] = right[j]
                    j = j + 1
                k = k + 1

            while i < len(left):  # daca au mai ramas elemente in prima lista, le comparam acum
                cuvant[k] = left[i]
                i = i + 1
                k = k + 1

            while j < len(right):  # daca au mai ramas elemente in a doua lista, le comparam acum
                cuvant[k] = right[j]
                j = j + 1
                k = k + 1

    def sortare_aparitii(self):
        self.mergeSort(self.repository.get_adjektive())
        self.mergeSort(self.repository.get_verbe())
        self.mergeSort(self.repository.get_substantive())

    #a doua metoda de sortare
    def bubbleSort(self, cuvant):
        for num in range(len(cuvant) - 1, 0, -1):
            for i in range(0, num):
                if cuvant[i].get_aparitii() > cuvant[i + 1].get_aparitii():
                    aux = cuvant[i]
                    cuvant[i] = cuvant[i + 1]
                    cuvant[i + 1] = aux


    def mergeSortprocent(self,lista):
        if len(lista) > 1:
            mid = len(lista) // 2  # obtinem un numar intreg
            left = lista[:mid]  # impartim in doua liste pana ajungem la liste cu un element
            right = lista[mid:]

            self.mergeSortprocent(left)  # sortam prima jumatate
            self.mergeSortprocent(right)  # sortam a doua jumatate

            i = 0
            j = 0
            k = 0
            while i < len(left) and j < len(right):
                if left[i][3] < right[j][3]:         #pe a treia pozitie se afla procentele (numerotare de la 0)
                    lista[k] = left[i]
                    i = i + 1
                else:
                    lista[k] = right[j]
                    j = j + 1
                k = k + 1

            while i < len(left):  # daca au mai ramas elemente in prima lista, le comparam acum
                lista[k] = left[i]
                i = i + 1
                k = k + 1

            while j < len(right):  # daca au mai ramas elemente in a doua lista, le comparam acum
                lista[k] = right[j]
                j = j + 1
                k = k + 1

    def binary_search(self,lista, procent):
        if lista[0][3]==procent:                    #daca elementul cautat se afla pe prima pozitie
            return 0
        if lista[len(lista)-1][3]==procent:         #daca elementul cautat se afla pe ultima pozitie
            return len(lista)
        st = 0
        dr = len(lista)
        while st < dr:
            mij = st + (dr - st) // 2
            val = lista[mij][3]             #procentul de la pozitia mij
            if procent == val:
                return mij
            elif procent > val:
                if st == mij:
                    break        
                st = mij
            elif procent < val:
                dr = mij







    # def insertionSort(self,aparitii):
    #     for i in range(1, len(aparitii)):
    #         val_curenta = aparitii[i][3]        #pe a treia pozitie se afla procentele (numerotare de la 0)
    #         poz = i
    #         while poz > 0 & aparitii[poz - 1][3] > val_curenta:
    #             aparitii[poz] = aparitii[poz - 1]
    #             poz = poz - 1
    #         aparitii[poz] = val_curenta






