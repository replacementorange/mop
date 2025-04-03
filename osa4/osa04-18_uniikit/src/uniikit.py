# tee ratkaisu tänne
# https://docs.python.org/3/tutorial/datastructures.html, 5.4 Sets
def uniikit(lista):
    uniikit = sorted(set(lista))
    return uniikit

if __name__ == "__main__":
    lista = [3, 2, 2, 1, 3, 3, 1]
    print(uniikit(lista)) # [1, 2, 3]