# 242 Arghire Gabriel

import time
from math import sqrt

class Joc:
    """
    Clasa care defineste jocul.
    """
    NR_COLOANE = None
    NR_LINII = None
    PROTECTIE = 'p'
    GOL = ' '
    OBSTACOL = '#'
    BOMBA_JMIN = 'b'
    BOMBA_JMAX = 'B'
    SIMBOLURI_JUC = [1, 2]
    JMIN = None # 1 sau 2
    JMAX = None # 2 sau 1

    # Pentru Joc
    matr = None

    NR_PROTECTII_JMIN = None
    POZ_X_JMIN = None
    POZ_Y_JMIN = None
    BOMBA_ACTIVA_JMIN = None

    NR_PROTECTII_JMAX = None
    POZ_X_JMAX = None
    POZ_Y_JMAX = None
    BOMBA_ACTIVA_JMAX = None

    # Joc

    def update_tabla(self, tabla):
        Joc.matr = tabla
        self.matr = tabla

    def obtine_tabla(self):
        return self.matr

    def update_linii(self, linii):
        Joc.NR_LINII = linii
        self.NR_LINII = linii

    def update_coloane(self, coloane):
        Joc.NR_COLOANE = coloane
        self.NR_COLOANE = coloane

    # Pentru JMIN
    # pozitie, protectii, BOMBA_ACTIVA_JMIN
    def obtine_JMIN(self):
        return list((self.obtine_pozitie_JMIN(), self.obtine_nr_protectii_JMIN(), self.obtine_bomba_JMIN()))

    def update_JMIN(self, juc_detalii):
        self.update_pozitie_JMIN(juc_detalii[0][0], juc_detalii[0][1])
        self.update_nr_protectii_JMIN(juc_detalii[1])
        self.update_bomba_JMIN(juc_detalii[2])

    def obtine_pozitie_JMIN(self):
        return self.POZ_X_JMIN, self.POZ_Y_JMIN

    def update_pozitie_JMIN(self, new_x, new_y):
        Joc.POZ_X_JMIN = new_x
        Joc.POZ_Y_JMIN = new_y

        self.POZ_X_JMIN = new_x
        self.POZ_Y_JMIN = new_y

    def obtine_nr_protectii_JMIN(self):
        return self.NR_PROTECTII_JMIN

    def update_nr_protectii_JMIN(self, new_nr_prot):
        Joc.NR_PROTECTII_JMIN = new_nr_prot
        self.NR_PROTECTII_JMIN = new_nr_prot

    def obtine_bomba_JMIN(self):
        return self.BOMBA_ACTIVA_JMIN

    def update_bomba_JMIN(self, new_bomb):
        Joc.BOMBA_ACTIVA_JMIN = new_bomb
        self.BOMBA_ACTIVA_JMIN = new_bomb

    # In jos pentru JMAX ------------------
    # pozitie, protectii, BOMBA_ACTIVA_JMAX
    def obtine_JMAX(self):
        return list((self.obtine_pozitie_JMAX(), self.obtine_nr_protectii_JMAX(), self.obtine_bomba_JMAX()))
    
    def update_JMAX(self, juc_detalii):
        self.update_pozitie_JMAX(juc_detalii[0][0], juc_detalii[0][1])
        self.update_nr_protectii_JMAX(juc_detalii[1])
        self.update_bomba_JMAX(juc_detalii[2])

    def obtine_pozitie_JMAX(self):
        return self.POZ_X_JMAX, self.POZ_Y_JMAX

    def update_pozitie_JMAX(self, new_x, new_y):
        Joc.POZ_X_JMAX = new_x
        Joc.POZ_Y_JMAX = new_y

        self.POZ_X_JMAX = new_x
        self.POZ_Y_JMAX = new_y

    def obtine_nr_protectii_JMAX(self):
        return self.NR_PROTECTII_JMAX

    def update_nr_protectii_JMAX(self, new_nr_prot):
        Joc.NR_PROTECTII_JMAX = new_nr_prot
        self.NR_PROTECTII_JMAX= new_nr_prot

    def obtine_bomba_JMAX(self):
        return self.BOMBA_ACTIVA_JMAX

    def update_bomba_JMAX(self, new_bomb):
        Joc.BOMBA_ACTIVA_JMAX = new_bomb
        self.BOMBA_ACTIVA_JMAX = new_bomb

    def bomba_in_raza_JMAX(self, i, j):
        tabla = self.matr

        if tabla[i + 1][j] == Joc.BOMBA_JMAX:
            return i + 1, j
        if tabla[i - 1][j] == Joc.BOMBA_JMAX:
            return i - 1, j
        if tabla[i][j + 1] == Joc.BOMBA_JMAX:
            return i, j + 1
        if tabla[i][j - 1] == Joc.BOMBA_JMAX:
            return i, j - 1
        
        return 0, 0
    
    def curata_harta_JMAX(self, i, j):
        tabla = self.matr

        if tabla[i + 1][j] == Joc.BOMBA_JMAX:
            tabla[i + 1][j] = Joc.GOL
        if tabla[i - 1][j] == Joc.BOMBA_JMAX:
            tabla[i - 1][j] = Joc.GOL
        if tabla[i][j + 1] == Joc.BOMBA_JMAX:
            tabla[i][j + 1] = Joc.GOL
        if tabla[i][j - 1] == Joc.BOMBA_JMAX:
            tabla[i][j - 1] = Joc.GOL

        return tabla

    # Constructorul
    def __init__(self, tabla, prot_nr, poz_x, poz_y, bmb_act, jucator):
        if tabla is not None:
            self.update_tabla(tabla)
            self.update_linii(len(tabla))
            self.update_coloane(len(tabla[0]))

            if jucator == Joc.JMIN:
                self.update_pozitie_JMIN(poz_x, poz_y)
                self.update_nr_protectii_JMIN(prot_nr)
                self.update_bomba_JMIN(bmb_act)
            else:
                self.update_pozitie_JMAX(poz_x, poz_y)
                self.update_nr_protectii_JMAX(prot_nr)
                self.update_bomba_JMAX(bmb_act)

        else:  # generam noi o harta
            Joc.NR_COLOANE = 8
            Joc.NR_LINII = 8

            # declaram si initializam harta
            self.matr = []
            for i in range(Joc.NR_LINII):
                self.matr.append([Joc.GOL] * Joc.NR_COLOANE)

            # TODO umple parametri

            # punem pozitiile jucatorilor
            self.matr[1][1] = '1'
            self.matr[self.NR_LINII - 2][self.NR_COLOANE - 2] = '2'

            # umplem tabla de joc cu #
            # sus si jos
            for j in range(Joc.NR_COLOANE):
                self.matr[0][j] = '#'
                self.matr[Joc.NR_LINII - 1][j] = '#'
            # stanga si dreapta
            for i in range(Joc.NR_LINII):
                self.matr[0][i] = '#'
                self.matr[Joc.NR_COLOANE - 1][i] = '#'

    def print_game_table(self):
        if self.matr is not None:
            for i in range(self.NR_LINII):
                for x in self.matr[i]:
                    print(x, end='')
                print('', flush=True)
        else:
            print("Matrice vida")

    def print_given_table(self, tab):
        if tab is not None:
            for i in range(len(tab)):
                for x in tab[i]:
                    print(x, end='')
                print('', flush=True)
        else:
            print("Matrice vida")

    def final(self):
        # Verificam daca jocul e terminat
        if self.obtine_nr_protectii_JMIN() < 0 and self.obtine_nr_protectii_JMAX() < 0:
            return 'remiza'
        elif self.obtine_nr_protectii_JMIN() < 0 and self.obtine_nr_protectii_JMAX() >= 0:
            return self.JMAX
        elif self.obtine_nr_protectii_JMIN() >= 0 and self.obtine_nr_protectii_JMAX() < 0:
            return self.JMIN
        else:
            return False

    def jucator_in_raza(self, BOMBA_JMIN, harta_cr):
        # numaram cati jucatori sunt atinsi de BOMBA_JMIN
        nr = []

        # mergem de la BOMBA_JMIN spre stanga pe linie
        for j in range(BOMBA_JMIN[1] - 1, 0):
            if harta_cr[BOMBA_JMIN[1]][j] == Joc.JMAX:
                nr.append([True, Joc.JMAX])
                break
            if harta_cr[BOMBA_JMIN[1]][j] == Joc.JMIN:
                nr.append([True, Joc.JMIN])
                break
            if harta_cr[BOMBA_JMIN[1]][j] == Joc.OBSTACOL or harta_cr[BOMBA_JMIN[1]][j] == Joc.BOMBA_JMIN or harta_cr[BOMBA_JMIN[1]][j] == Joc.BOMBA_JMAX:
                break

        # mergem de la BOMBA_JMIN spre dreapta pe linie
        for j in range(BOMBA_JMIN[1] + 1, len(harta_cr[0])):
            if harta_cr[BOMBA_JMIN[1]][j] == Joc.JMAX:
                nr.append([True, Joc.JMAX])
                break
            if harta_cr[BOMBA_JMIN[1]][j] == Joc.JMIN:
                nr.append([True, Joc.JMIN])
                break
            if harta_cr[BOMBA_JMIN[1]][j] == Joc.OBSTACOL or harta_cr[BOMBA_JMIN[1]][j] == Joc.BOMBA_JMIN or harta_cr[BOMBA_JMIN[1]][j] == Joc.BOMBA_JMAX:
                break

        # mergem de la BOMBA_JMIN in sus pe coloana
        for i in range(BOMBA_JMIN[2] - 1, 0):
            if harta_cr[i][BOMBA_JMIN[2]] == Joc.JMAX:
                nr.append([True, Joc.JMAX])
                break
            if harta_cr[i][BOMBA_JMIN[2]] == Joc.JMIN:
                nr.append([True, Joc.JMIN])
                break
            if harta_cr[i][BOMBA_JMIN[2]] == Joc.OBSTACOL or harta_cr[i][BOMBA_JMIN[2]] == Joc.BOMBA_JMIN or harta_cr[BOMBA_JMIN[1]][j] == Joc.BOMBA_JMAX:
                break

        # mergem de la BOMBA_JMIN in jos pe coloana
        for i in range(BOMBA_JMIN[2] + 1, len(harta_cr)):
            if harta_cr[i][BOMBA_JMIN[2]] == Joc.JMAX:
                nr.append([True, Joc.JMAX])
                break
            if harta_cr[i][BOMBA_JMIN[2]] == Joc.JMIN:
                nr.append([True, Joc.JMIN])
                break
            if harta_cr[i][BOMBA_JMIN[2]] == Joc.OBSTACOL or harta_cr[i][BOMBA_JMIN[2]] == Joc.BOMBA_JMIN or harta_cr[BOMBA_JMIN[1]][j] == Joc.BOMBA_JMAX:
                break

        # jucatorii nu erau in raza
        return nr

    # intoarce jucatorii loviti de bomba si numarul lor nou de protectii
    def activare_bomba(self, bomba_parametru, nr_p, harta_cr, juc_cr):
        jucatori_loviti = self.jucator_in_raza(bomba_parametru, harta_cr)

        rezultat = []

        # daca niciun jucator nu a fost lovit
        if len(jucatori_loviti) == 0:
            # jucatorii nu era in raza bombei
            rezultat.append([juc_cr, nr_p])
            return rezultat

        # daca doar un jucator a fost lovit de BOMBA_JMIN sau BOMBA_JMAX
        elif len(jucatori_loviti) == 1:
            ce_jucator = jucatori_loviti[0][1]

            if ce_jucator == juc_cr:  # daca BOMBA_JMIN sau BOMBA_JMAX a nimerit pe jucatorul curent
                rezultat.append([juc_cr, nr_p - 1])
            else:  # BOMBA_JMIN  sau BOMBA_JMAX a nimerit pe adversar
                juc_op = self.jucator_opus_doi(juc_cr)

                if juc_op == Joc.JMAX:
                    rezultat.append([juc_op, self.obtine_nr_protectii_JMAX() - 1])
                else:
                    rezultat.append([juc_op, self.obtine_nr_protectii_JMIN() - 1])

            return rezultat

        # daca BOMBA_JMIN sau BOMBA_JMAX a lovit ambii jucatori
        elif len(jucatori_loviti) == 2:

            for i in range(0, 2):
                ce_jucator = jucatori_loviti[i][1]

                if ce_jucator == juc_cr:  # daca BOMBA_JMIN a nimerit pe jucatorul curent
                    rezultat.append([juc_cr, nr_p - 1])
                else:  # BOMBA_JMIN sau BOMBA_JMAX a nimerit pe adversar
                    juc_op = self.jucator_opus_doi(juc_cr)

                    if juc_op == Joc.JMAX:
                        rezultat.append([juc_op, self.obtine_nr_protectii_JMAX() - 1])
                    else:
                        rezultat.append([juc_op, self.obtine_nr_protectii_JMIN() - 1])

            return rezultat

    # intorc coordonatele urmatoarelor mutari posibile (maxim 4)
    def available_moves_player(self, simbol, jucator):
        mvs = []
        tabla = self.matr

        # pozitia jucatorului
        if jucator == Joc.JMIN:
            i, j = self.obtine_pozitie_JMIN()
        else:
            i, j = self.obtine_pozitie_JMAX()

        # incercam sa obtinem cele 4 posibile mutari daca este spatiu sau protectie
        if tabla[i + 1][j] == simbol:
            mvs.append([i + 1, j])
        if tabla[i - 1][j] == simbol:
            mvs.append([i - 1, j])
        if tabla[i][j - 1] == simbol:
            mvs.append([i, j - 1])
        if tabla[i][j + 1] == simbol:
            mvs.append([i, j + 1])

        return mvs


    # functie de generarea a urmatoarelor mutari
    def expandeaza_mutari_calculator(self, jucator):
        mutari_posibile_expandeaza = []
        tabla = self.matr

        # preluam mutarile posibile
        avlb_moves_space = self.available_moves_player(Joc.GOL, jucator)
        avlb_moves_prot = self.available_moves_player(Joc.PROTECTIE, jucator)

        # preluam datele jucatorului curent si adversarului
        if jucator == Joc.JMIN:
            fct_coord_x, fct_coord_y = self.obtine_pozitie_JMIN()
            fct_nr_prot = self.obtine_nr_protectii_JMIN()
            fct_bmb_act = self.obtine_bomba_JMIN()

            hit_bmb_act = self.obtine_bomba_JMAX()
            other_coord_x, other_coord_y = self.obtine_pozitie_JMAX()
        else:
            fct_coord_x, fct_coord_y = self.obtine_pozitie_JMAX()
            fct_nr_prot = self.obtine_nr_protectii_JMAX()
            fct_bmb_act = self.obtine_bomba_JMAX()

            hit_bmb_act = self.obtine_bomba_JMIN()
            other_coord_x, other_coord_y = self.obtine_pozitie_JMIN()

        # print("T: ", self.print_given_table(tab=tabla))

        # generam urmatoarele mutari posibile pentru pozitiile cu spatiu
        for x, y in avlb_moves_space:
            aux = [x[:] for x in tabla]

            # punem pozitia jucatorului pe harta
            aux[x][y] = jucator

            # generam posibilitatile:
            # 0) cu spatiu in urma si nimic cu bombe
            # 1) sau spatiu in urma si activare BOMBA_JMIN - daca se poate
            # 2) sau plasare BOMBA_JMIN in urma - cu activare BOMBA_JMIN daca exista
            for k in range(0, 3):

                if k == 0:  # 0) cu spatiu in urma si nimic cu bombe
                    # punem spatiu in locul unde a fost jucatorul
                    aux[fct_coord_x][fct_coord_y] = Joc.GOL

                    # facem append
                    mutari_posibile_expandeaza.append(Joc(aux, fct_nr_prot, x, y, fct_bmb_act, jucator))

                elif k == 1:  # 1) sau spatiu in urma si activare BOMBA_JMIN - daca se poate
                    # punem spatiu in locul unde a fost jucatorul
                    aux[fct_coord_x][fct_coord_y] = Joc.GOL

                    # daca este vreo BOMBA_JMIN activa de-a jucatorului
                    if fct_bmb_act[0]:
                        # activam BOMBA_JMIN
                        juc_dupa_BOMBA_JMIN = self.activare_bomba(fct_bmb_act, fct_nr_prot, aux, jucator)

                        # punem spatiu in locul unde a fost bomba
                        aux[fct_bmb_act[1]][fct_bmb_act[2]] = Joc.GOL

                        # dezamorsam bomba
                        fct_bmb_act = [False, 0, 0]

                        if len(juc_dupa_BOMBA_JMIN) == 1:
                            fct_juc = juc_dupa_BOMBA_JMIN[0][0]
                            fct_nr_prot = juc_dupa_BOMBA_JMIN[0][1]

                            if fct_juc == jucator:
                                mutari_posibile_expandeaza.append(
                                    Joc(aux, fct_nr_prot, x, y, fct_bmb_act, jucator))
                            else:
                                mutari_posibile_expandeaza.append(
                                    Joc(aux, fct_nr_prot, other_coord_x, other_coord_y, hit_bmb_act, fct_juc))

                        else:
                            for j in range(0, 2):
                                fct_juc = juc_dupa_BOMBA_JMIN[j][0]
                                fct_nr_prot = juc_dupa_BOMBA_JMIN[j][1]

                                if fct_juc == jucator:
                                    mutari_posibile_expandeaza.append(
                                        Joc(aux, fct_nr_prot, x, y, fct_bmb_act, jucator))
                                else:
                                    mutari_posibile_expandeaza.append(
                                        Joc(aux, fct_nr_prot, other_coord_x, other_coord_y, hit_bmb_act, fct_juc))

                elif k == 2:  # 2) sau plasare BOMBA_JMIN in urma - cu activare BOMBA_JMIN daca exista
                    # punem BOMBA_JMIN in locul unde a fost jucatorul
                    if jucator == Joc.JMIN:
                        aux[fct_coord_x][fct_coord_y] = Joc.BOMBA_JMIN
                    else:
                        aux[fct_coord_x][fct_coord_y] = Joc.BOMBA_JMAX

                    # daca este vreo BOMBA_JMIN activa de-a jucatorului
                    if fct_bmb_act[0]:
                        # activam BOMBA_JMIN
                        juc_dupa_BOMBA_JMIN = self.activare_bomba(fct_bmb_act, fct_nr_prot, aux, jucator)

                        # punem spatiu in locul unde a fost bomba
                        aux[fct_bmb_act[1]][fct_bmb_act[2]] = Joc.GOL

                        # dezamorsam bomba
                        fct_bmb_act = [False, 0, 0]

                        if len(juc_dupa_BOMBA_JMIN) == 1:
                            fct_juc = juc_dupa_BOMBA_JMIN[0][0]
                            fct_nr_prot = juc_dupa_BOMBA_JMIN[0][1]

                            if fct_juc == jucator:
                                mutari_posibile_expandeaza.append(
                                    Joc(aux, fct_nr_prot, x, y, fct_bmb_act, jucator))
                            else:
                                mutari_posibile_expandeaza.append(
                                    Joc(aux, fct_nr_prot, other_coord_x, other_coord_y, hit_bmb_act, fct_juc))

                        else:
                            for j in range(0, 2):
                                fct_juc = juc_dupa_BOMBA_JMIN[j][0]
                                fct_nr_prot = juc_dupa_BOMBA_JMIN[j][1]

                                if fct_juc == jucator:
                                    mutari_posibile_expandeaza.append(
                                        Joc(aux, fct_nr_prot, x, y, fct_bmb_act, jucator))
                                else:
                                    mutari_posibile_expandeaza.append(
                                        Joc(aux, fct_nr_prot, other_coord_x, other_coord_y, hit_bmb_act, fct_juc))
                    
                    else:  # nu am avut bomba de activat
                        # punem detaliile bombei
                        bmb_de_pus = [True, fct_coord_x, fct_coord_y]

                        mutari_posibile_expandeaza.append(Joc(aux, fct_nr_prot, x, y, bmb_de_pus, jucator))

        # TODO 3 cazuri ca mai sus
        # generam urmatoarele mutari posibile pentru pozitiile cu protectie
        for x, y in avlb_moves_prot:
            aux = [x[:] for x in tabla]

            # punem pozitia jucatorului pe harta
            aux[x][y] = jucator

            # generam posibilitatile:
            # 0) cu spatiu in urma si nimic cu bombe
            # 1) sau spatiu in urma si activare BOMBA_JMIN - daca se poate
            # 2) sau plasare BOMBA_JMIN in urma - cu activare BOMBA_JMIN daca exista
            for k in range(0, 3):

                if k == 0:  # 0) cu spatiu in urma si nimic cu bombe
                    # punem spatiu in locul unde a fost jucatorul
                    aux[fct_coord_x][fct_coord_y] = Joc.GOL

                    # facem append
                    mutari_posibile_expandeaza.append(Joc(aux, fct_nr_prot + 1, x, y, fct_bmb_act, jucator))

                elif k == 1:  # 1) sau spatiu in urma si activare BOMBA_JMIN - daca se poate
                    # punem spatiu in locul unde a fost jucatorul
                    aux[fct_coord_x][fct_coord_y] = Joc.GOL

                    # daca este vreo BOMBA_JMIN activa de-a jucatorului
                    if fct_bmb_act[0]:
                        # activam BOMBA_JMIN
                        juc_dupa_BOMBA_JMIN = self.activare_bomba(fct_bmb_act, fct_nr_prot, aux, jucator)

                        # punem spatiu in locul unde a fost bomba
                        aux[fct_bmb_act[1]][fct_bmb_act[2]] = Joc.GOL

                        # dezamorsam bomba
                        fct_bmb_act = [False, 0, 0]

                        if len(juc_dupa_BOMBA_JMIN) == 1:
                            fct_juc = juc_dupa_BOMBA_JMIN[0][0]
                            fct_nr_prot = juc_dupa_BOMBA_JMIN[0][1]

                            if fct_juc == jucator:
                                mutari_posibile_expandeaza.append(
                                    Joc(aux, fct_nr_prot + 1, x, y, fct_bmb_act, jucator))
                            else:
                                mutari_posibile_expandeaza.append(
                                    Joc(aux, fct_nr_prot, other_coord_x, other_coord_y, hit_bmb_act, fct_juc))

                        else:
                            for j in range(0, 2):
                                fct_juc = juc_dupa_BOMBA_JMIN[j][0]
                                fct_nr_prot = juc_dupa_BOMBA_JMIN[j][1]

                                if fct_juc == jucator:
                                    mutari_posibile_expandeaza.append(
                                        Joc(aux, fct_nr_prot + 1, x, y, fct_bmb_act, jucator))
                                else:
                                    mutari_posibile_expandeaza.append(
                                        Joc(aux, fct_nr_prot, other_coord_x, other_coord_y, hit_bmb_act, fct_juc))

                elif k == 2:  # 2) sau plasare BOMBA_JMIN in urma - cu activare BOMBA_JMIN daca exista
                    # punem BOMBA_JMIN in locul unde a fost jucatorul
                    if jucator == Joc.JMIN:
                        aux[fct_coord_x][fct_coord_y] = Joc.BOMBA_JMIN
                    else:
                        aux[fct_coord_x][fct_coord_y] = Joc.BOMBA_JMAX

                    # daca este vreo BOMBA_JMIN activa de-a jucatorului
                    if fct_bmb_act[0]:
                        # activam BOMBA_JMIN
                        juc_dupa_BOMBA_JMIN = self.activare_bomba(fct_bmb_act, fct_nr_prot, aux, jucator)

                        # punem spatiu in locul unde a fost bomba
                        aux[fct_bmb_act[1]][fct_bmb_act[2]] = Joc.GOL

                        # dezamorsam bomba
                        fct_bmb_act = [False, 0, 0]

                        if len(juc_dupa_BOMBA_JMIN) == 1:
                            fct_juc = juc_dupa_BOMBA_JMIN[0][0]
                            fct_nr_prot = juc_dupa_BOMBA_JMIN[0][1]

                            if fct_juc == jucator:
                                mutari_posibile_expandeaza.append(
                                    Joc(aux, fct_nr_prot + 1, x, y, fct_bmb_act, jucator))
                            else:
                                mutari_posibile_expandeaza.append(
                                    Joc(aux, fct_nr_prot, other_coord_x, other_coord_y, hit_bmb_act, fct_juc))

                        else:
                            for j in range(0, 2):
                                fct_juc = juc_dupa_BOMBA_JMIN[j][0]
                                fct_nr_prot = juc_dupa_BOMBA_JMIN[j][1]

                                if fct_juc == jucator:
                                    mutari_posibile_expandeaza.append(
                                        Joc(aux, fct_nr_prot + 1, x, y, fct_bmb_act, jucator))
                                else:
                                    mutari_posibile_expandeaza.append(
                                        Joc(aux, fct_nr_prot, other_coord_x, other_coord_y, hit_bmb_act, fct_juc))
                    
                    else:  # nu am avut bomba de activat
                        # punem detaliile bombei
                        bmb_de_pus = [True, fct_coord_x, fct_coord_y]

                        mutari_posibile_expandeaza.append(Joc(aux, fct_nr_prot + 1, x, y, bmb_de_pus, jucator))

        # print("EXP: ", mutari_posibile_expandeaza[0])
        return mutari_posibile_expandeaza

    # mergem pe increderea ca 
    # un numar de protectii mai mare fata de adversar
    # este mai bun
    def fct_euristica(self):
        if self.JMIN == 1:
            return self.obtine_nr_protectii_JMAX() - self.obtine_nr_protectii_JMIN() + 2
        else:
            return self.obtine_nr_protectii_JMIN() - self.obtine_nr_protectii_JMAX() + 2

    # incercam sa ne apropiem de jucator
    # pentru a pune bombe mai aproape
    # (cu distanta euclidiana)
    def fct_euristica_doi(self):
        # luam pozitiile jucatorilor
        p_x_jmin, p_y_jmin = self.obtine_pozitie_JMIN()
        p_x_jmax, p_y_jmax = self.obtine_pozitie_JMAX()
        
        return abs(sqrt((p_x_jmin - p_x_jmax)**2 + (p_y_jmin - p_y_jmax)**2))

    def estimeaza_scor(self, adancime, tip_estimare_scor):
        t_final = self.final()
        if t_final == Joc.JMAX:
            return 999 + adancime
        elif t_final == Joc.JMIN:
            return -999 - adancime
        elif t_final == 'remiza':
            return 0
        else:
            if tip_estimare_scor == 1:
                return self.fct_euristica()
            else:
                return self.fct_euristica_doi()

    def jucator_opus_doi(self, jucator_curent):
        if jucator_curent == Joc.JMIN:
            return Joc.JMAX
        else:
            return Joc.JMIN

    def __str__(self):
        sir ='\n'

        for i in range(Joc.NR_LINII):
            for j in range(Joc.NR_COLOANE):
                sir += str(self.matr[i][j])
            sir += '\n'

        return sir

class Stare:

    ADANCIME_MAX = None

    def __init__(self, tabla_joc, j_curent, adancime, parinte=None, scor=0):
        self.tabla_joc = tabla_joc
        self.j_curent = j_curent

        #adancimea in arborele de stari
        self.adancime=adancime

        #scorul starii (daca e finala) sau al celei mai bune stari-fiice (pentru jucatorul curent)
        self.scor=scor

        #lista de mutari posibile din starea curenta
        self.mutari_posibile=[]

        #cea mai buna mutare din lista de mutari posibile pentru jucatorul curent
        self.stare_aleasa=None

    def jucator_opus(self):
        if self.j_curent == Joc.JMIN:
            return Joc.JMAX
        else:
            return Joc.JMIN

    def mutari_stare(self):
        l_mutari=self.tabla_joc.expandeaza_mutari_calculator(self.j_curent)
        juc_opus=self.jucator_opus()
        l_stari_mutari=[Stare(mutare, juc_opus, self.adancime-1, parinte=self) for mutare in l_mutari]

        return l_stari_mutari

    def __str__(self):
        sir = str(self.tabla_joc) + "(Juc curent: " + str(self.j_curent) + ")\n"
        return sir

""" Algoritmul MinMax """


def min_max(stare, tip_estimare_scor):

    if stare.adancime == 0 or stare.tabla_joc.final():
        stare.scor = stare.tabla_joc.estimeaza_scor(stare.adancime, tip_estimare_scor)
        return stare

    #calculez toate mutarile posibile din starea curenta
    stare.mutari_posibile = stare.mutari_stare()

    #aplic algoritmul minimax pe toate mutarile posibile (calculand astfel subarborii lor)
    mutari_scor=[min_max(mutare, tip_estimare_scor) for mutare in stare.mutari_posibile]

    if stare.j_curent==Joc.JMAX :
        #daca jucatorul e JMAX aleg starea-fiica cu scorul maxim
        stare.stare_aleasa = max(mutari_scor, key=lambda x: x.scor)
    else:
        #daca jucatorul e JMIN aleg starea-fiica cu scorul minim
        stare.stare_aleasa = min(mutari_scor, key=lambda x: x.scor)

    stare.scor=stare.stare_aleasa.scor
    return stare


def alpha_beta(alpha, beta, stare, tip_estimare_scor):
    if stare.adancime==0 or stare.tabla_joc.final() :
        stare.scor = stare.tabla_joc.estimeaza_scor(stare.adancime, tip_estimare_scor)
        return stare

    if alpha >= beta:
        return stare #este intr-un interval invalid deci nu o mai procesez

    stare.mutari_posibile = stare.mutari_stare()
    if len(stare.mutari_posibile) == 0:
        return stare

    if stare.j_curent == Joc.JMAX :
        scor_curent = float('-inf')

        for mutare in stare.mutari_posibile:
            #calculeaza scorul
            stare_noua = alpha_beta(alpha, beta, mutare, tip_estimare_scor)

            if (scor_curent < stare_noua.scor):
                stare.stare_aleasa = stare_noua
                scor_curent = stare_noua.scor
            if(alpha < stare_noua.scor):
                alpha = stare_noua.scor
                if alpha >= beta:
                    break

    elif stare.j_curent == Joc.JMIN :
        scor_curent = float('inf')

        for mutare in stare.mutari_posibile:
            stare_noua = alpha_beta(alpha, beta, mutare, tip_estimare_scor)

            if scor_curent > stare_noua.scor:
                stare.stare_aleasa = stare_noua
                scor_curent = stare_noua.scor

            if beta > stare_noua.scor:
                beta = stare_noua.scor
                if alpha >= beta:
                    break

    stare.scor = stare.stare_aleasa.scor

    return stare


def afis_daca_final(stare_curenta):

    final = stare_curenta.tabla_joc.final()
    if final:
        if final == 'remiza':
            print("Remiza!")
        else:
            print("A castigat " + str(final))
        return True
    return False


def coordonate_initiale_jucatori(tabla_de_joc, simbol):
    for i in range(len(tabla_de_joc)):
        for j in range(len(tabla_de_joc[0])):
            if tabla_de_joc[i][j] == simbol:
                return (i, j)


def main_console():
    # timpul total de joc
    inceput_program = time.time()

    # deshidem fisierul cu tabla de joc
    fisier_input = "./242_Arghire_Gabriel_Lab9_Pb4_input2.txt"

    print("Fisierul input: ", fisier_input)
    print("\n")

    # deschidem fisierul
    f_in_open = open(fisier_input, "r")

    # declaram matricea care va fi tabla de joc initiala
    tbl_joc = []

    # citim din fisier
    for f_line in f_in_open:
        f_line = f_line.replace('\n', '')
        tbl_joc.append(list(f_line))

    f_in_open.close()

    # initializare algoritm
    raspuns_valid = False
    while not raspuns_valid:
        try:
            tip_algoritm = int(input("Algorimul folosit? (raspundeti cu 1 sau 2)\n 1. Minimax\n 2. Alpha-beta\n "))
            if tip_algoritm in [1, 2]:
                raspuns_valid = True
                break
            else:
                print("Nu ati ales o varianta corecta.")
        except ValueError:
            print("Nu ati ales o varianta corecta.")

    # initializare ADANCIME_MAX
    raspuns_valid = False
    while not raspuns_valid:
        try:
            dificultate = int(input("Nivel de dificultate (raspundeti cu 1, 2 sau 3)\n 1. Usor \n 2. Mediu \n 3. "
                                    "Avansat \n"))

            if dificultate == 1:
                raspuns_valid = True
                Stare.ADANCIME_MAX = 3

            elif dificultate == 2:
                raspuns_valid = True
                Stare.ADANCIME_MAX = 10

            elif dificultate == 3:
                raspuns_valid = True
                Stare.ADANCIME_MAX = 20

            else:
                print("Trebuie sa introduceti valoarea 1, 2 sau 3")
        except ValueError:
            print("Trebuie sa introduceti valoarea 1, 2 sau 3")

    # initializare jucatori
    [s1, s2] = Joc.SIMBOLURI_JUC.copy()  # lista de simboluri posibile
    raspuns_valid = False
    while not raspuns_valid:
        try:
            Joc.JMIN = int(input("Doriti sa jucati cu {} sau cu {}? ".format(s1, s2)))
            if Joc.JMIN in Joc.SIMBOLURI_JUC:
                raspuns_valid = True
            else:
                print("Raspunsul trebuie sa fie {} sau {}.".format(s1, s2))
        except ValueError:
            print("Raspunsul trebuie sa fie {} sau {}.".format(s1, s2))

    if Joc.JMIN == s1:
        Joc.JMAX = s2
    else:
        Joc.JMAX = s1

    # apelare constructor
    tabla_curenta = Joc(tabla=tbl_joc, prot_nr=2, poz_x=1, poz_y=1, bmb_act=[False, 0, 0], jucator=Joc.JMIN)
    
    # initializare tabla
    tabla_curenta.NR_LINII = len(tbl_joc)
    tabla_curenta.NR_COLOANE = len(tbl_joc[0])

    # fiecare jucator incepe cu 2 protectii
    tabla_curenta.update_nr_protectii_JMIN(2)
    tabla_curenta.update_nr_protectii_JMAX(2)

    # fiecare jucator incepe cu nicio bomba activa
    tabla_curenta.update_bomba_JMIN([False, 0, 0])
    tabla_curenta.update_bomba_JMAX([False, 0, 0])

    # obtine coordonate initiale
    poz_min_x, poz_min_y = coordonate_initiale_jucatori(tbl_joc, '1')
    poz_max_x, poz_max_y = coordonate_initiale_jucatori(tbl_joc, '2')

    # stabilire pozitie jucatori 
    if Joc.JMIN == s1:
        tabla_curenta.update_pozitie_JMIN(poz_min_x, poz_min_y)
        tabla_curenta.update_pozitie_JMAX(poz_max_x, poz_max_y)
    else:
        tabla_curenta.update_pozitie_JMIN(poz_max_x, poz_max_y)
        tabla_curenta.update_pozitie_JMAX(poz_min_x, poz_min_y)

    # pozitia de start a jucatorului
    linie, coloana = tabla_curenta.obtine_pozitie_JMIN()
    
    # afisare tabla initiala
    print("Tabla initiala")
    print(tabla_curenta.print_game_table())

    # creare stare initiala
    stare_curenta = Stare(tabla_joc=tabla_curenta, j_curent=Joc.JMIN, adancime=Stare.ADANCIME_MAX)
    
    # pentru afisarea timpului rundelor
    start_time = 0.0
    end_time = 0.0

    # nr mutari
    nr_mutari_jmin = 0
    nr_mutari_jmax = 0

    while True:
        if stare_curenta.j_curent == Joc.JMIN:
            # muta jucatorul

            # daca e game over
            if afis_daca_final(stare_curenta):
                break

            else:  # jucatorul poate muta

                print("Sunteti de rand sa mutati")

                start_time = time.time()

                # intrebam daca doreste sa paraseasca jocul
                while True:
                    actiune = int(input("Doriti sa parasiti jocul? (raspundeti cu 1 sau 2)\n 1. Parasire joc \n 2. Continuare joc\n")) 

                    if actiune == 1:
                        print("Jocul a durat %s secunde" % (time.time() - inceput_program))
                        
                        print("Jucatorul JMIN a avut %d mutari" % nr_mutari_jmin)
                        print("Jucatorul JMAX a avut %d mutari" % nr_mutari_jmax)
                        
                        print("Scor jucator: ", stare_curenta.tabla_joc.estimeaza_scor(5000, tip_algoritm))
                        stare_curenta.j_curent = stare_curenta.jucator_opus()
                        print("Scor calculator: ", stare_curenta.tabla_joc.estimeaza_scor(5000, tip_algoritm))

                        exit(0)
                    elif actiune == 2:
                        break
                    else:
                        print("Trebuie sa introduceti valoarea 1 sau 2") 

                nr_mutari_jmin += 1

                raspuns_valid = False
                iau_protectie = False

                print("Detalii jucator inainte de mutare: \n")

                # luam pozitia curenta
                linie_cr, coloana_cr = stare_curenta.tabla_joc.obtine_pozitie_JMIN()
                print("Pozitie curenta: ", linie_cr, coloana_cr)
                print("Numar de protectii: ", stare_curenta.tabla_joc.obtine_nr_protectii_JMIN())
                
                bomba_jucator = stare_curenta.tabla_joc.obtine_bomba_JMIN()
                if (bomba_jucator[0]):
                    print("Bomba activa la coordonatele: ", bomba_jucator[1], bomba_jucator[2])
                else:
                    print("Nu exista bomba activa")

                print("\n")

                while not raspuns_valid:
                    try:
                        # cerem urmatoarea pozitie
                        print("Introduceti coordonate pentru urmatoarea mutare: ")
                        linie = int(input("linie= "))
                        coloana = int(input("coloana = "))
                        
                        # daca mutarea se face in interiorul hartii
                        if 0 < coloana < tabla_curenta.NR_COLOANE and 0 < linie < tabla_curenta.NR_LINII:
                            # daca pe acea pozitie se poate muta
                            if stare_curenta.tabla_joc.matr[linie][coloana] == Joc.GOL:
                                # daca mutarea se face in apropierea pozitiei dinainte
                                if abs(linie - linie_cr) <= 1:
                                    if abs(coloana - coloana_cr) <= 1:
                                        # daca nu se muta pe diagonala
                                        if abs(linie + coloana - (linie_cr + coloana_cr)) < 2:
                                            raspuns_valid = True
                            # daca pe pozitia pe care vrea sa se mute este o protectie
                            elif stare_curenta.tabla_joc.matr[linie][coloana] == Joc.PROTECTIE:
                                # daca mutarea se face in apropierea pozitiei dinainte
                                if abs(linie - linie_cr) <= 1:
                                    if abs(coloana - coloana_cr) <= 1:
                                        # daca nu se muta pe diagonala
                                        if abs(linie + coloana - (linie_cr + coloana_cr)) < 2:
                                            iau_protectie = True
                                            raspuns_valid = True

                            if not raspuns_valid:
                                print("Mutarea nu este valida")
                        else:
                            print("Coloana si/sau linie invalida")

                    except ValueError:
                        print("Va rugam introduceti date valabile")


                # plasez simbolul pe "tabla de joc"
                stare_curenta.tabla_joc.matr[linie][coloana] = Joc.JMIN

                # actualizam ce se vede pe harta - sterg vechea valoare
                stare_curenta.tabla_joc.matr[linie_cr][coloana_cr] = ' '

                # daca jucatorul a luat o protectie
                if iau_protectie: 
                    # crestem numarul de protectii cu 1
                    stare_curenta.tabla_joc.update_nr_protectii_JMIN(stare_curenta.tabla_joc.obtine_nr_protectii_JMIN() + 1)

                # facem update al pozitiei
                stare_curenta.tabla_joc.update_pozitie_JMIN(linie, coloana)

                # cerem acum o actiune din partea jucatorului
                raspuns_valid = False
                while not raspuns_valid:
                    try:
                        actiune = int(input("Actiune dorita (raspundeti cu 1, 2 sau 3)\n 1. Activare bomba \n 2. Plasare bomba \n 3. "
                                                "Nimic \n"))

                        if actiune == 1:
                            raspuns_valid = True

                            bmb_jmin = stare_curenta.tabla_joc.obtine_bomba_JMIN()
                            nr_p_jmin = stare_curenta.tabla_joc.obtine_nr_protectii_JMIN()

                            if bmb_jmin[0]:
                                jc_loviti = stare_curenta.tabla_joc.activare_bomba(bmb_jmin, nr_p_jmin, stare_curenta.tabla_joc.obtine_tabla(), Joc.JMIN)
                                
                                if len(jc_loviti) == 1:
                                    ce_juc_lovit = jc_loviti[0][0]
                                    ce_nr_protec = jc_loviti[0][1] - 1

                                    if ce_juc_lovit == Joc.JMIN:
                                        # update protectii
                                        stare_curenta.tabla_joc.update_nr_protectii_JMIN(ce_nr_protec)

                                        # update harta
                                        tbl_up = stare_curenta.tabla_joc.obtine_tabla()
                                        tbl_up[bmb_jmin[1]][bmb_jmin[2]] = Joc.GOL
                                        stare_curenta.tabla_joc.update_tabla(tbl_up)
                                        
                                        # dezamorsam bomba si updatam
                                        bmb_jmin = [False, 0, 0]
                                        stare_curenta.tabla_joc.update_bomba_JMIN(bmb_jmin)
                                    else:
                                        # update protectii
                                        stare_curenta.tabla_joc.update_nr_protectii_JMAX(ce_nr_protec)

                                        # update harta
                                        tbl_up = stare_curenta.tabla_joc.obtine_tabla()
                                        tbl_up[bmb_jmin[1]][bmb_jmin[2]] = Joc.GOL
                                        stare_curenta.tabla_joc.update_tabla(tbl_up)
                                        
                                        # dezamorsam bomba si updatam
                                        bmb_jmin = [False, 0, 0]
                                        stare_curenta.tabla_joc.update_bomba_JMIN(bmb_jmin)
                                else:
                                    for j in range(0, 2):
                                        ce_juc_lovit = jc_loviti[j][0]
                                        ce_nr_protec = jc_loviti[j][1] - 1

                                        if ce_juc_lovit == Joc.JMIN:
                                            # update protectii
                                            stare_curenta.tabla_joc.update_nr_protectii_JMIN(ce_nr_protec)
                                            
                                        else:
                                            # update protectii
                                            stare_curenta.tabla_joc.update_nr_protectii_JMAX(ce_nr_protec)

                                    # update harta
                                    tbl_up = stare_curenta.tabla_joc.obtine_tabla()
                                    tbl_up[bmb_jmin[1]][bmb_jmin[2]] = Joc.GOL
                                    stare_curenta.tabla_joc.update_tabla(tbl_up)

                                    # dezamorsam bomba si updatam
                                    bmb_jmin = [False, 0, 0]
                                    stare_curenta.tabla_joc.update_bomba_JMIN(bmb_jmin)


                                print("Bomba a fost activata")
                            else:
                                print("Nu a fost nicio bomba de activat. Trecem mai departe.\n")

                        elif actiune == 2:  # plasare bomba
                            raspuns_valid = True

                            # verificam daca are deja o bomba activa
                            bmb_jmin = stare_curenta.tabla_joc.obtine_bomba_JMIN()
                            nr_p_jmin = stare_curenta.tabla_joc.obtine_nr_protectii_JMIN()

                            # activam bomba daca are
                            if bmb_jmin[0]:
                                jc_loviti = stare_curenta.tabla_joc.activare_bomba(bmb_jmin, nr_p_jmin, stare_curenta.tabla_joc.obtine_tabla(), Joc.JMIN)
                                
                                if len(jc_loviti) == 1:
                                    ce_juc_lovit = jc_loviti[0][0]
                                    ce_nr_protec = jc_loviti[0][1] - 1

                                    if ce_juc_lovit == Joc.JMIN:
                                        # update protectii
                                        stare_curenta.tabla_joc.update_nr_protectii_JMIN(ce_nr_protec)

                                        # update harta
                                        tbl_up = stare_curenta.tabla_joc.obtine_tabla()
                                        tbl_up[bmb_jmin[1]][bmb_jmin[2]] = Joc.GOL
                                        stare_curenta.tabla_joc.update_tabla(tbl_up)
                                        
                                        # dezamorsam bomba si updatam
                                        bmb_jmin = [False, 0, 0]
                                        stare_curenta.tabla_joc.update_bomba_JMIN(bmb_jmin)
                                    else:
                                        # update protectii
                                        stare_curenta.tabla_joc.update_nr_protectii_JMAX(ce_nr_protec)

                                        # update harta
                                        tbl_up = stare_curenta.tabla_joc.obtine_tabla()
                                        tbl_up[bmb_jmin[1]][bmb_jmin[2]] = Joc.GOL
                                        stare_curenta.tabla_joc.update_tabla(tbl_up)
                                        
                                        # dezamorsam bomba si updatam
                                        bmb_jmin = [False, 0, 0]
                                        stare_curenta.tabla_joc.update_bomba_JMIN(bmb_jmin)
                                else:
                                    for j in range(0, 2):
                                        ce_juc_lovit = jc_loviti[j][0]
                                        ce_nr_protec = jc_loviti[j][1] - 1

                                        if ce_juc_lovit == Joc.JMIN:
                                            # update protectii
                                            stare_curenta.tabla_joc.update_nr_protectii_JMIN(ce_nr_protec)

                                        else:
                                            # update protectii
                                            stare_curenta.tabla_joc.update_nr_protectii_JMAX(ce_nr_protec)

                                    # update harta
                                    tbl_up = stare_curenta.tabla_joc.obtine_tabla()
                                    tbl_up[bmb_jmin[1]][bmb_jmin[2]] = Joc.GOL
                                    stare_curenta.tabla_joc.update_tabla(tbl_up)
                                    
                                    # dezamorsam bomba si updatam
                                    bmb_jmin = [False, 0, 0]
                                    stare_curenta.tabla_joc.update_bomba_JMIN(bmb_jmin)

                            # daca a avut bomba de activat -> am activat
                            # acum plasam bomba in vechea lui pozitie
                            bmb_pentru_pus = [True, linie_cr, coloana_cr]

                            # facem update parametri
                            stare_curenta.tabla_joc.update_bomba_JMIN(bmb_pentru_pus)

                            # update harta
                            tbl_up = stare_curenta.tabla_joc.obtine_tabla()
                            tbl_up[bmb_pentru_pus[1]][bmb_pentru_pus[2]] = Joc.BOMBA_JMIN
                            stare_curenta.tabla_joc.update_tabla(tbl_up)
                            
                            print("Am plasat bomba")

                        elif actiune == 3:
                            raspuns_valid = True

                        else:
                            print("Trebuie sa introduceti valoarea 1, 2 sau 3") 
                    except ValueError:
                        print("Trebuie sa introduceti valoarea 1, 2 sau 3") 

                # afisarea starii jocului in urma mutarii utilizatorului
                print("\nTabla dupa mutarea jucatorului\n")
                print(tabla_curenta.print_game_table())

                print("Detalii jucator dupa mutare: \n")

                # luam pozitia curenta
                linie_cr, coloana_cr = stare_curenta.tabla_joc.obtine_pozitie_JMIN()
                print("Pozitie curenta: ", linie_cr, coloana_cr)
                print("Numar de protectii: ", stare_curenta.tabla_joc.obtine_nr_protectii_JMIN())
                
                bomba_jucator = stare_curenta.tabla_joc.obtine_bomba_JMIN()
                if (bomba_jucator[0]):
                    print("Bomba activa la coordonatele: ", bomba_jucator[1], bomba_jucator[2])
                else:
                    print("Nu exista bomba activa")

                print("Scor jucator: ", stare_curenta.tabla_joc.estimeaza_scor(5000, tip_algoritm))

                print("\n")

                # testez daca jocul a ajuns intr-o stare finala
                # si afisez un mesaj corespunzator in caz ca da
                if afis_daca_final(stare_curenta):
                    break

                # S-a realizat o mutare. Schimb jucatorul cu cel opus
                stare_curenta.j_curent = stare_curenta.jucator_opus()

                end_time = time.time() - start_time

                print("Timpul rundei jucatorului a durat %s secunde" % end_time)


        # --------------------------------
        else:  # jucatorul e JMAX (calculatorul)
            # Mutare calculator

            # daca e game over
            if afis_daca_final(stare_curenta):
                    break
            
            nr_mutari_jmax += 1

            print("Este randul calculatorului sa mute")

            start_time = time.time()

            print("Detalii calculator inainte de mutare: \n")

            print("Pozitie curenta: ", stare_curenta.tabla_joc.obtine_pozitie_JMAX())
            print("Numar de protectii: ", stare_curenta.tabla_joc.obtine_nr_protectii_JMAX())
            
            bomba_jucator = stare_curenta.tabla_joc.obtine_bomba_JMAX()
            if (bomba_jucator[0]):
                print("Bomba activa la coordonatele: ", bomba_jucator[1], bomba_jucator[2])
            else:
                print("Nu exista bomba activa")

            print("\n")

            # luam ceea ce stim despre jucator
            jucator_detalii = []
            if stare_curenta.j_curent == Joc.JMAX:
                # facem copy lui JMIN
                jucator_detalii = stare_curenta.tabla_joc.obtine_JMIN()
            else:
                # facem copy lui JMAX
                jucator_detalii = stare_curenta.tabla_joc.obtine_JMAX()

            aux = stare_curenta.tabla_joc.expandeaza_mutari_calculator(Joc.JMAX)
            # daca nu poate face nici o miscare
            if len(aux) == 0:
                print(f'Jucatorul {stare_curenta.j_curent} - calculatorul - nu poate efectua nicio mutare')
                stare_curenta.j_curent = stare_curenta.jucator_opus()

            else:
                if tip_algoritm == 1:
                    stare_actualizata = min_max(stare_curenta, tip_algoritm)
                else: # tip_algoritm = 2
                    stare_actualizata = alpha_beta(-5000, 5000, stare_curenta, tip_algoritm)

                stare_curenta.tabla_joc = stare_actualizata.stare_aleasa.tabla_joc

                # facem update bombei lui JMAX
                poz_new_max = stare_curenta.tabla_joc.obtine_pozitie_JMAX()
                bomba_x, bomba_y = stare_curenta.tabla_joc.bomba_in_raza_JMAX(poz_new_max[0], poz_new_max[1])

                # daca calculatorul a pus bomba
                if bomba_x != 0 and bomba_y != 0:
                    jmax_bmb = [True, bomba_x, bomba_y]
                    stare_curenta.tabla_joc.update_bomba_JMAX(jmax_bmb)
                    # preiau harta noua
                    new_tbl_joc = stare_curenta.tabla_joc.curata_harta_JMAX(bomba_x, bomba_y)
                    stare_curenta.tabla_joc.update_tabla(new_tbl_joc)

                print("Tabla dupa mutarea calculatorului")
                print(stare_curenta.tabla_joc.print_game_table())

                # refacem
                if stare_curenta.j_curent == Joc.JMAX:
                    # refacem JMIN
                    stare_curenta.tabla_joc.update_JMIN(jucator_detalii)
                else:
                    # refacem JMAX
                    stare_curenta.tabla_joc.update_JMAX(jucator_detalii)
                
                print("Detalii calculator dupa mutare: \n")

                print("Pozitie curenta: ", stare_curenta.tabla_joc.obtine_pozitie_JMAX())
                print("Numar de protectii: ", stare_curenta.tabla_joc.obtine_nr_protectii_JMAX())
                
                bomba_jucator = stare_curenta.tabla_joc.obtine_bomba_JMAX()
                if (bomba_jucator[0]):
                    print("Bomba activa la coordonatele: ", bomba_jucator[1], bomba_jucator[2])
                else:
                    print("Nu exista bomba activa")

                print("Scor calculator: ", stare_curenta.tabla_joc.estimeaza_scor(5000, tip_algoritm))

                print("\n")

                if afis_daca_final(stare_curenta):
                    break

                # S-a realizat o mutare. Schimb jucatorul cu cel opus
                stare_curenta.j_curent = stare_curenta.jucator_opus()

                end_time = time.time() - start_time

                print("Timpul rundei calculatorului a durat %s secunde" % end_time)

    print("Jocul a durat %s secunde" % (time.time() - inceput_program))

    print("Jucatorul JMIN a avut %d " % nr_mutari_jmin)
    print("Jucatorul JMAX a avut %d " % nr_mutari_jmax)

    if stare_curenta.j_curent == Joc.JMIN:
        print("Scor jucator: ", stare_curenta.tabla_joc.estimeaza_scor(5000, tip_algoritm))
        stare_curenta.j_curent = stare_curenta.jucator_opus()
        print("Scor calculator: ", stare_curenta.tabla_joc.estimeaza_scor(5000, tip_algoritm))
    else:
        print("Scor calculator: ", stare_curenta.tabla_joc.estimeaza_scor(5000, tip_algoritm))
        stare_curenta.j_curent = stare_curenta.jucator_opus()
        print("Scor jucator: ", stare_curenta.tabla_joc.estimeaza_scor(5000, tip_algoritm))


if __name__ == "__main__" :
    main_console()
