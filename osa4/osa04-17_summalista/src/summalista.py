# tee ratkaisu tänne
# https://stackoverflow.com/questions/14050824/add-sum-of-values-of-two-lists-into-new-list
# https://peps.python.org/pep-0201/
# https://www.w3schools.com/python/ref_func_zip.asp
def summa(lista1, lista2):
    #summa_lista = []

    summa_lista = [luku1 + luku2 for luku1, luku2 in zip(lista1, lista2)]

    return summa_lista

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(summa(a, b)) # [8, 10, 12]