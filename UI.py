class UI:
    def __init__(self, controller):
        self.controller = controller

    def menu(self):
        ok = 0
        o = int(input("0: Exit\n1:Zufällige Sätze\n2:Prozent der korrekt formatierten Sätze\n3:Anzahl der Erscheinungen \n4:Substantiv + Verb + Substantiv + Adjektiv\n5:Satze identisch\n6:Equality Prozent\n7: Wörter sortieren\n8:“Equality Prozent” von Tastatur\nOption: "))

        while o != 0:
            if o == 1:
                file = open("saetze.txt", "w")  # deschidem fisirul in care vom scrie propozitiile

                n = int(input("n="))
                a = int(input("Nr maxim de substantive:"))
                b = int(input("Nr maxim de verbe:"))
                c = int(input("Nr maxim de adjective:"))
                print("\n")

                for i in range(0, n):  #mergem pana la n+1 fiindca una am creat-o pentru a testa prop identice

                    list = self.controller.satz(a, b, c)  # accesam lista cu propozitia
                    prop = ""
                    for j in range(0,len(list)):  # afisam pe rand fiecare element din ea, iar dupa trecem pe linie noua
                        file.write(str(list[j].get_cuvant()) + " ")
                        prop = prop + str(list[j].get_cuvant()) + " "
                    print(prop)

                    file.write('\n')

                self.controller.test()
                for i in range(len(self.controller.get_prop())-1, len(self.controller.get_prop())):
                    pr=""
                    for j in range(0, len(self.controller.get_prop()[i])):
                        pr=pr+self.controller.get_prop()[i][j].get_cuvant()+" "
                    print(pr)
                    file.write(pr)
                file.close()

                #urmatoarele metode le apelam dupa ce au fost generate propozitiile pentru a nu fi apelate de mai multe ori
                #in cazul in care se selecteaza optiunea 8, de exemplu, de mai multe ori
                self.controller.gleich_worter()
                prop = self.controller.get_prop()  # propozitiile generate
                aparitii = self.controller.equality_prozent()  # lista cu liste unde sunt stocate procentele
                magic = self.controller.get_magicSazte()
                ok = 1

            if o == 2:
                if ok == 0:
                    print("Muss zuerst Option 1 wahlen")
                else:
                    nr = self.controller.get_nr()  # nr contine numarul de propozitii corect formate (un singur subst, adj si verb)
                    prozent = self.controller.prozent(nr, n)  # calculam procentul
                    print(str(prozent) + "% ist das Prozent der korrekt formatierten Sätze")

            if o == 3:
                if ok == 0:
                    print("Muss zuerst Option 1 wahlen")
                self.controller.print_erscheinungen()

            if o == 4:
                if ok == 0:
                    print("Muss zuerst Option 1 wahlen")
                else:
                    print(str(self.controller.nr_topik) + " Sätze haben den Topik S+V+S+A")

            if o == 5:
                if ok==0:
                    print("Muss zuerst Option 1 wahlen")
                else:
                    indici=self.controller.satze_identisch()
                    print(indici)
                    for i in range(0, len(indici)):
                        pr=""
                        for j in range(0, len(prop[indici[i]])):        #indice[i] ne da numarul propozitiei
                            pr=pr+prop[indici[i]][j].get_cuvant()+" "
                        pr=pr+ "-identica, linia "+str(indici[i]+1)         #mai adunam 1 la indici[i] fiindca numerotarea incepe de la 0
                        print(pr)

            if o == 6:
                if ok == 0:
                    print("Muss zuerst Option 1 wahlen")
                else:
                    nr_prop=aparitii[0][0]                  #la ce propozitie sunt, o initializam cu prima din lista de aparitii
                    i=0
                    print(str(aparitii)+"\n")
                    while i != len(aparitii):
                        pr=""
                        for j in range(0, len(prop[nr_prop])):              #afisez propozitia cu numarul nr_prop
                            pr=pr+prop[nr_prop][j].get_cuvant()+" "
                        print(pr)
                        while nr_prop == aparitii[i][0]:       #atata timp cat si in urmatoarea lista este vorba tot de propozitia generata nr_prop,
                                                                    #afisam propozitiile magice cu care are in comun cuvinte
                            pr="-"
                            for k in range(0, len(magic[aparitii[i][2]])):         #afisam propozitia magica (aparitii[i][2] imi va da numarul propozitiei magice
                                pr=pr+magic[aparitii[i][2]][k]+" "
                            print(pr+"-"+ str(aparitii[i][3])+"% gleich")
                            i += 1                                  # crestem si i-ul fiindca ne mutam la lista urmatoare
                            if i>=len(aparitii):            #punem conditia pt a nu avea eroarea "list index out of range" care s-ar fi intamplat dupa ultima incrementare a lui i
                                break
                        print("\n")
                        if i<len(aparitii):                         #punem conditia pt a nu avea eroarea "list index out of range" care s-ar fi intamplat dupa ultima incrementare a lui i
                            nr_prop=aparitii[i][0]                  #schimbam si numarul propozitiei curente

            if o == 7:
                if ok == 0:
                    print("Muss zuerst Option 1 wahlen")
                else:
                    self.controller.sortare_aparitii()
                    subst=self.controller.get_substantive()
                    adj=self.controller.get_adjektive()
                    verbe=self.controller.get_verbe()
                    for i in range(0, len(subst)):
                        if subst[i].get_aparitii() != 0:
                            print(subst[i].get_cuvant()+" - "+str(subst[i].get_aparitii())+" Erscheinungen")

                        #faul,Maus,isst s-ar putea sa apara de 2 ori in lista fiindca in repository am creat la sfarsit dupa citirea din fisier inca un obiect din cele mentionate pt a testarea optiunii 5
                    print("\n")
                    for i in range(0, len(verbe)):
                        if verbe[i].get_aparitii() != 0:
                            print(verbe[i].get_cuvant()+" - "+str(verbe[i].get_aparitii())+" Erscheinungen")
                    print("\n")
                    for i in range(0, len(adj)):
                        if adj[i].get_aparitii() != 0:
                            print(adj[i].get_cuvant()+" - "+str(adj[i].get_aparitii())+" Erscheinungen")

            if o == 8:
                if ok == 0:
                    print("Muss zuerst Option 1 wahlen")
                else:
                    self.controller.mergeSortprocent(aparitii)
                    print(str(aparitii) + "\n")
                    procent=int(input("Das Prozent: "))
                    #index=self.controller.binarySearch(aparitii, procent)
                    index = self.controller.binary_search(aparitii, procent)
                    index2= self.controller.binary_search(aparitii, procent)
                    #am obtinut dupa cautarea binara pozitia unde se afla prima propozitie cu un procent dat,
                    #dar poate mai exista dupa ea cu acelasi procent, asa ca mai facem o parcurgere incepand cu acea pozitie

                    if index != None:

                        if index!= len(aparitii):       #daca indexul e la ultima propozitie, atunci nu mai avem ce parcurgere sa facem

                            """
                            Vom face doua parcurgeri, prima in stanga indexului obtinut de la cautarea binara, iar a doua in dreapta.
                            Propozitiile s-ar putea sa se repete intrucat o propozitie magica poate sa aiba acelasi procent 
                            de egalitate cu mai multe propozitii generate la optiunea 1.
                            """

                            #parcurgerea spre stanga
                            kk = 1
                            if aparitii[index2][3] == aparitii[index2 - 1][3]:      #daca exista propozitii cu acelasi procent in stanga
                                while kk==1:            #cat timp mai exista propozitii cu acelasi procent
                                    pr=""
                                    for k in range(0, len(magic[aparitii[index2-1][2]]) ):  # afisam propozitia magica (aparitii[index-1][2] imi va da numarul propozitiei magice) si am scazut 1 pentru a nu-mi afisa propozitia de la indexul obtinut de la cautarea binara de doua ori (o afisez doar la cautarea spre dreapta)
                                        pr = pr + magic[aparitii[index2-1][2]][k] + " "
                                    print(pr)
                                    if aparitii[index2-2][3] != aparitii[index2-1][3]:      #daca procentul propozitiei penultime este diferit de cel al antepenultimei propozitii
                                        kk=0                                            #setam ok la 0 pt a nu mai intra in bucla
                                    index2-=1


                            kk=1
                            while kk==1:            #cat timp mai exista propozitii cu acelasi procent
                                pr=""
                                for k in range(0, len(magic[aparitii[index][2]]) ):  # afisam propozitia magica (aparitii[index][2] imi va da numarul propozitiei magice)
                                    pr = pr + magic[aparitii[index][2]][k] + " "
                                print(pr)
                                if aparitii[index][3] != aparitii[index+1][3]:      #daca procentul propozitiei curente este diferit de cel al urmatoarei propozitii
                                    kk=0                                            #setam ok la 0 pt a nu mai intra in bucla
                                index+=1
                        else:
                            if index == len(aparitii):          #daca este vorba de ultima propozitie
                                pr=""
                                for k in range(0, len(magic[aparitii[len(aparitii)-1][2]]) ):  # afisam propozitia magica (aparitii[index][2] imi va da numarul propozitiei magice)
                                    pr = pr + magic[aparitii[len(aparitii)-1][2]][k] + " "
                                print(pr)
                    else:
                        print("Es gibt keine Sätze mit diesem Prozent")




            print("\n")
            o = int(input("Geben Sie ein neues Option: "))
            print("\n")

