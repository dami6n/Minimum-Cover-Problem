import os


def print_coding_scheme_info(set_s, collection_c,value_k):



    print("EJERCICIO 2")
    print("----------------------------------")


    # Prints the first and last 5 elements of the set "S"
    if len(set_s) < 10:
        print("Como la lista tiene menos de 10 elementos, se imprime completa: ")
        print(set_s)
    else:
        print("Primeros 5 elementos de S: ")
        print(set_s[0:5])
        print("Ultimos 5 elementos de S: ")
        print(set_s[(len(set_s)-5):(len(set_s))])
        print("----------------------------------")


    # Prints number of subsets of collection "C"

    print("Numero de miembros de C: ")
    print(len(collection_c))
    print("----------------------------------")

    #Prints value of "k"
    print("Valor de k: ")
    print(value_k)
    print("----------------------------------")

    #Prints coding scheme of first element of "C"
    print("Codificacion del primer elemento del primer miembro de C")
    print(collection_c[0])



