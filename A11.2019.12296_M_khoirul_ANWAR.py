def rekrusif(bilangan):
    if bilangan > 0 :
        print(bilangan)
        bilangan = bilangan -1
        rekrusif(bilangan)
    else:
        print(bilangan)
angka =int(input("Masukan angka ="))
rekrusif(angka)