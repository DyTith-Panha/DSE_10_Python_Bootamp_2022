def dict_values(dict_yes):
    for yeskey, yesvalue in dict_yes.items():
        print(yeskey, ":", *yesvalue)
        print('*****')
dict_values(({120:("Visal", "Borey", "Sovann"), 130:("Hout", "Mouyleng", "Pidor"), 140:("Nary", "Misora","Masaki")}))