import os
import info_coding_scheme
import minimum_cover_algorithm


# Ask user for file name
opt = input("Introduzca el numero de ejercicio de la practica que desea probar (opciones validas = 2 o 3): ")
print("----------------------------------")
errorMsg=""

try:
    if (not(opt=="3" or opt=="2")):
        errorMsg="Opcion no valida"
        assert opt=="3" or opt=="2"
        # Ask user for file name
    file_name = input("Introduzca el nombre del archivo: ")
    print("----------------------------------")

    # Check if file exists in project folder
    if os.path.isfile(file_name):
        # Open file and read its contents
        with open(file_name, "r") as file:
            contents = file.read()
    else:
        errorMsg="File not found."
        assert os.path.isfile(file_name)

    # List with finite set "S", collection of subsets "C", and number "k"
    componentList = contents.split("&&")

    # Validate that the input of the file has the correct format: S&&C&&k
    if (len(componentList)!= 3):
        errorMsg="Se ingreso una cadena con formato incorrecto."
        assert len(componentList)== 3

    # Assign value of "S"
    set_s=componentList[0].split(",")

    # Assign value of "C"
    collection_c=componentList[1].split("#")

    # Assign value of "k"
    value_k=componentList[2]


    if opt=="2":
        info_coding_scheme.print_coding_scheme_info(set_s, collection_c,value_k)
    elif opt=="3":
        minimum_cover_algorithm.min_cover_alg(set_s, collection_c, value_k)
except:
    print("Error:" + errorMsg)

