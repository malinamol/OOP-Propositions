from Domain import Cuvant


class Repository:
    def __init__(self):
        self.substantive = []
        self.adjektive = []
        self.verbe = []
        self.magicSatze = []
        self.read_file()            #la initializarea repository-ului se vor citi automat cuvintele din fisiere
        self.read_magicSatze()


    #functia printeaza aparitiile fiecarui cuvant
    def print_erscheinung(self):
        file2 = open("erscheinungen.txt", "w")
        for i in range(0, len(self.verbe)):
            file2.write(str(self.verbe[i].get_cuvant()) + "-" + str(self.verbe[i].get_aparitii()) + " Erscheinungen-Verb")
            file2.write("\n")

        file2.write("\n")

        for i in range(0, len(self.substantive)):
            file2.write(str(self.substantive[i].get_cuvant()) + "-" + str(self.substantive[i].get_aparitii()) + " Erscheinungen-Substantiv")
            file2.write("\n")

        file2.write("\n")

        for i in range(0, len(self.adjektive)):
            file2.write(str(self.adjektive[i].get_cuvant()) + "-" + str(self.adjektive[i].get_aparitii()) + " Erscheinungen-Adjektiv")
            file2.write("\n")
        file2.close()

    #functie pentru citirea celor trei tipuri de cuvinte din fisiere si crearea obiectelor
    def read_file(self):
        file = open("substantive.txt", "r")
        for line in file:
            item = line.split(",")
            for i in range(0, len(item)):
                self.substantive.append(Cuvant(item[i].strip(), 1))
        self.substantive.append(Cuvant("Maus", 1))
        self.substantive[len(self.substantive) - 1].set_aparitii(1)
        file.close()

        file = open("verbe.txt", "r")
        for line in file:
            item = line.split(",")
            for i in range(0, len(item)):
                self.verbe.append(Cuvant(item[i].strip(), 2))
        self.verbe.append(Cuvant("isst", 2))
        self.verbe[len(self.verbe)-1].set_aparitii(1)
        file.close()

        file = open("adjektive.txt", "r")
        for line in file:
            item = line.split(",")
            for i in range(0, len(item)):
                self.adjektive.append(Cuvant(item[i].strip(), 3))
        self.adjektive.append(Cuvant("faul", 3))
        self.adjektive[len(self.adjektive) - 1].set_aparitii(1)
        file.close()


    #functie pentru citirea cuvintelor magice
    def read_magicSatze(self):
        file=open("magic.txt", "r")
        for line in file:
            items = line.split()  # despartim cuvintele de pe o linie
            self.magicSatze.append(items)  # punem lista cu cuvintele intr-o lista
        file.close()

    def get_substantive(self):
        return self.substantive

    def get_adjektive(self):
        return self.adjektive

    def get_verbe(self):
        return self.verbe

    def get_magicSatze(self):
        return self.magicSatze

