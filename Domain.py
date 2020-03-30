# o clasa CUVANT cu 2 atribute: stringul si tipul cuvantului
# folosim 2 randomuri:unul pentru a vedea cate cuvinte vom avea in propozitie si al doile apentru a obtine cuvintele random din listele de substantive, adjective, verbe
'''
tip 1-substantiv
tip 2-verb
tip 3-adjektiv
'''

class Cuvant:
    def __init__(self, cuvant, tip):
        self.cuvant=cuvant
        self.tip=tip
        self.aparitii=0

    def get_cuvant(self):
        return self.cuvant

    def get_aparitii(self):
        return self.aparitii

    def get_tip(self):
        return self.tip

    def set_aparitii(self, aparitii):
        self.aparitii=aparitii

    def __str__(self):
        return "%s, %i" % (self.cuvant, self.tip)

