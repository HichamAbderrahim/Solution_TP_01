import numpy as np


# ------------------- Ex 01 -------------------
def calc_somme_1(_n):
    return _n * (_n + 1) / 2


def calc_somme_2(_n):
    s = 0
    for i in range(1, _n + 1):
        s += i
    return s


# ------------------- Ex 02 -------------------
def calc_fact_1(_n):
    f = 1
    for i in range(1, _n + 1):
        f *= i
    return f


def calc_fact_2(_n):
    if _n <= 1:
        return 1
    return _n * calc_fact_2(_n - 1)


# ------------------- Ex 03 -------------------
def calc_mono(_x, _n):
    m = 1
    if _n >= 0:
        for i in range(1, _n + 1):
            m = m * _x
    else:
        m = 1 / calc_mono(_x, -_n)
    return m


# ------------------- Ex 04 -------------------
def calc_fact_cnp(_n, _p):
    _c = calc_fact_1(_p) * calc_fact_1(_n - _p)
    _c = int(calc_fact_1(_n) / _c)
    return calc_fact_1(_c)


# ------------------- Ex 05 -------------------
def calc_suit(_n):
    if _n == 0:
        return 1
    return 2 * calc_suit(_n - 1) + 1


# ------------------- Ex 06 -------------------
def calc_fibo(_n):
    if _n == 0 or _n == 1:
        return 1
    return calc_fibo(_n - 1) + calc_fibo(_n - 2)


# ------------------- Ex 07 -------------------
def perm_2(_x, _y):
    z = _x
    _x = _y
    _y = z
    return _x, _y


def perm_3(_x, _y, _z):
    _x, _y = perm_2(_x, _y)
    _y, _z = perm_2(_y, _z)
    return _x, _y, _z


# ------------------- Ex 08 -------------------
def max_2(_x, _y):
    if _x > _y:
        return _x
    return _y


def max_3(_x, _y, _z):
    m = max_2(_x, _y)
    return max_2(m, _z)


# ------------------- Ex 09 -------------------
def exp(_x, _n):
    _e = 0
    for i in range(_n + 1):
        _e += calc_mono(_x, i) / calc_fact_1(i)
    return _e


def calc_exp(_x, _n):
    eps = 0.000001
    test = False
    e = 0
    while not test:
        e = exp(_x, _n)
        test = e - exp(_x, _n - 1) < eps
        _n += 1
    return e


# ------------------- Ex 10 -------------------
def max_t(_tableau):
    _pos = 0
    _max = _tableau[_pos]
    for i in range(1, len(_tableau)):
        if _tableau[i] > _max:
            _pos = i
            _max = _tableau[_pos]
    return _pos, _max


# ------------------- Ex 11 -------------------
def inv_t(_tableau):
    for i in range(int(len(_tableau) / 2)):
        _t = _tableau[i]
        _tableau[i] = _tableau[len(_tableau) - i - 1]
        _tableau[len(_tableau) - i - 1] = _t


# ------------------- Ex 12 -------------------
def fusion(tableau, g, m, d, comparer):
    G = [None] * (m - g + 1)
    D = [None] * (d - m)

    for i in range(G.__len__()):
        G[i] = tableau[g + i]

    for i in range(D.__len__()):
        D[i] = tableau[m + 1 + i]

    i = j = 0
    k = g

    while i < G.__len__() and j < D.__len__():
        if comparer(G[i], D[j]):
            tableau[k] = G[i]
            i = i + 1
        else:
            tableau[k] = D[j]
            j = j + 1
        k = k + 1

    while i < G.__len__():
        tableau[k] = G[i]
        i = i + 1
        k = k + 1

    while j < D.__len__():
        tableau[k] = D[j]
        j = j + 1
        k = k + 1


def tri_fusion(tableau, g, d, comparer):
    if g < d:
        m = int(g + (d - g) / 2)
        tri_fusion(tableau, g, m, comparer)
        tri_fusion(tableau, m + 1, d, comparer)
        fusion(tableau, g, m, d, comparer)


# ------------------- Ex 13 -------------------
def somme_2_m(a, b):
    c = np.zeros((a.__len__(), a[0].__len__()))
    for i in range(c.__len__()):
        for j in range(c[0].__len__()):
            c[i][j] = a[i][j] + b[i][j]
    return c


# ------------------- Ex 14 -------------------
def prod_2_m(a, b):
    if a[0].__len__() == b.__len__():
        c = np.zeros((a.__len__(), b[0].__len__()))
        for i in range(c.__len__()):
            for j in range(c[0].__len__()):
                for k in range(b.__len__()):
                    c[i][j] += a[i][k] * b[k][j]
        return c


class Main:
    def __init__(self, numero):
        getattr(self, "ex_" + str(numero), self.par_defaut)()

    def ex_01(self):
        n = int(input("Entrer la valeur de N : "))
        print("Méthode 1: " + str(calc_somme_1(n)))
        print("Méthode 1: " + str(calc_somme_2(n)))

    def ex_02(self):
        n = int(input("Entrer la valeur de N : "))
        print("Méthode 1: " + str(calc_fact_1(n)))
        print("Méthode 2: " + str(calc_fact_2(n)))

    def ex_03(self):
        x = int(input("Entrer la valeur de X : "))
        n = int(input("Entrer la valeur de N : "))
        print(calc_mono(x, n))

    def ex_04(self):
        x = int(input("Entrer la valeur de N : "))
        n = int(input("Entrer la valeur de P : "))
        print(calc_fact_cnp(x, n))

    def ex_05(self):
        n = int(input("Entrer la valeur de N : "))
        print(calc_suit(n))

    def ex_06(self):
        n = int(input("Entrer la valeur de N : "))
        print(calc_fibo(n))

    def ex_07(self):
        x = float(input("Entrer la valeur de X : "))
        y = float(input("Entrer la valeur de Y : "))
        z = float(input("Entrer la valeur de Z : "))

        print("avant: ", x, y, z)
        x, y, z = perm_3(x, y, z)
        print("après: ", x, y, z)

    def ex_08(self):
        x = float(input("Entrez la valeur du premier nombre : "))
        y = float(input("Entrez la valeur du deuxième nombre :"))
        z = float(input("Entrez la valeur du troisième nombre :"))
        print(max_3(x, y, z))

    def ex_09(self):
        x = int(input("Entrer la valeur de X : "))
        n = int(input("Entrer la valeur de N : "))
        print(calc_exp(x, n))

    def ex_10(self):
        n = int(input("Entrez le nombre d'éléments: "))
        tableau = [0] * n
        for i in range(len(tableau)):
            tableau[i] = int(input('Entrez tableau[' + str(i) + ']: '))
        maximum = max_t(tableau)
        print("pos: " + str(maximum[0]))
        print("val: " + str(maximum[1]))

    def ex_11(self):
        n = int(input("Entrez le nombre d'éléments: "))
        tableau = [0] * n
        for i in range(len(tableau)):
            tableau[i] = int(input('Entrez tableau[' + str(i) + ']: '))
        print(tableau)
        inv_t(tableau)
        print(tableau)

    def ex_12(self):
        n = int(input("Entrez le nombre d'éléments: "))
        tableau = [0] * n
        for i in range(len(tableau)):
            tableau[i] = int(input('Entrez tableau[' + str(i) + ']: '))
        print(tableau)
        tri_fusion(tableau, 0, n - 1, lambda n1, n2: n1 < n2)
        print(tableau)

    def ex_13(self):
        n = int(input("Entrez le nombre de lignes: "))
        m = int(input("Entrez le nombre de colonnes: "))
        print("Entrez les valeurs de la première matrice")
        a = np.zeros((n, m))
        for i in range(a.__len__()):
            for j in range(a[0].__len__()):
                a[i][j] = float(input('Entrez tableau[' + str(i) + ', ' + str(j) + ']: '))
        print("Entrez les valeurs de la deuxième matrice")
        b = np.zeros((n, m))
        for i in range(a.__len__()):
            for j in range(a[0].__len__()):
                b[i][j] = float(input('Entrez tableau[' + str(i) + ', ' + str(j) + ']: '))
        c = somme_2_m(a, b)
        for i in range(c.__len__()):
            for j in range(c[0].__len__()):
                print(c[i][j], end=" ")
            print()

    def ex_14(self):
        print("La première matrice")
        an = int(input("--> Entrez le nombre de lignes: "))
        am = int(input("--> Entrez le nombre de colonnes: "))
        print("Entrez les valeurs")
        a = np.zeros((an, am))
        for i in range(a.__len__()):
            for j in range(a[0].__len__()):
                a[i][j] = float(input('Entrez tableau[' + str(i) + ', ' + str(j) + ']: '))
        print("La deuxième matrice")
        bn = int(input("--> Entrez le nombre de lignes: "))
        bm = int(input("--> Entrez le nombre de colonnes: "))
        print("Entrez les valeurs")
        b = np.zeros((bn, bm))
        for i in range(b.__len__()):
            for j in range(b[0].__len__()):
                b[i][j] = float(input('Entrez tableau[' + str(i) + ', ' + str(j) + ']: '))
        c = prod_2_m(a, b)
        if c is None:
            print("Multiplication impossible")
        else:
            for i in range(c.__len__()):
                for j in range(c[0].__len__()):
                    print(c[i][j], end=" ")
                print()

    def par_defaut(self):
        print("Il n'y a pas d'exercice avec ce numéro")


# ------------------- Main -------------------
print("Il s'agit d'un programme qui contient la solution de la série d'exercices joints à ce code\n")
exercices = {
    1: "Ecrire un algorithme qui calcule la somme de 𝑛 premiers entiers",
    2: "Ecrire un algorithme qui calcule le factoriel de 𝑛",
    3: "Ecrire un algorithme qui calcule le monôme 𝑋^𝑛",
    4: "Ecrire un algorithme qui calcule le factoriel de 𝐶𝑛𝑝",
    5: "Ecrire un algorithme pour trouver le terme général de la suite 𝑈𝑛 = 2 · 𝑈𝑛−1 + 1, où 𝑈0 = 1",
    6: "Ecrire un algorithme pour calculer la suite de Fibonacci 𝑈𝑛 =· 𝑈𝑛−1 + 𝑈𝑛−2 + 1, où 𝑈0 = 𝑈1 = 1",
    7: "Ecrire une procédure qui permute deux nombres réels. En utilisant cette procédure, écrire un algorithme "
       "qui permute 3 nombres",
    8: "Ecrire une procédure qui trouve le max deux nombres. En utilisant cette procédure, écrire un algorithme "
       "qui peut trouve le Max de 3 nombres",
    9: "Ecrire un algorithme qui calcule 𝑒𝑥𝑝(𝑥) sachant que 𝑒𝑥𝑝(𝑥) = 1 + 𝑥 + 𝑥^2/2!/+ . . . + x^n/n! + "
       "o(n)\nLa condition d’arrêt 𝑒𝑠𝑡 𝑒𝑥𝑝𝑛(𝑥) − 𝑒𝑥𝑝𝑛−1(𝑥) < 𝜖, où 𝜀 = 10−6",
    10: "Ecrire un algorithme pour trouver la valeur Max dans un tableau d’entiers",
    11: "Ecrire un algorithme pour inverser les éléments d’un tableau d’entiers",
    12: "Ecrire un algorithme pour trier un tableau d’entiers par ordre ascendant",
    13: "Ecrire un algorithme qui calcule la somme de 2 matrices",
    14: "Ecrire un algorithme qui calcule le produit de 2 matrices, Quelle est la condition pour que la "
        "multiplication soit correcte ?",
}
for key in exercices.keys():
    print(str(key).zfill(2) + " --> " + exercices.get(key))
exo = int(input("\nEntrez le numéro de l'exercice: "))
Main(str(exo).zfill(2))
