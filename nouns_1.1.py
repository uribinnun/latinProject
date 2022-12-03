class FirstDeclention:
    # Importing the database of 1st declention nouns in nom. sn. and iterating over it to create
    # dictionaries for each variation
    from database import first_declention_cloud
    acc_sn = {}
    acc_pl = {}
    nom_voc_abl_sn = {}
    gen_dat_sn_nom_voc_pl = {}
    dat_abl_pl = {}
    gen_pl = {}
    for object in first_declention_cloud:
        acc_sn[object] = [f"{object[:-1]}am"]
        acc_pl[object] = [f"{object[:-1]}as"]
        nom_voc_abl_sn[object] = [object]
        gen_dat_sn_nom_voc_pl[object] = [f"{object[:-1]}ae"]
        dat_abl_pl[object] = [f"{object[:-1]}is"]
        gen_pl[object] = [f"{object[:-1]}arum"]

    def __init__(self, stem, number, case):
        self.stem = stem
        self.number = number
        self.case = case


    def case_func(self):
        if noun_input in FirstDeclention.first_declention_cloud:
            if case_input == '1' or '6' and number_input == '2':
                if number_input == '2':
                    return FirstDeclention.gen_dat_sn_nom_voc_pl[noun_input]
                return FirstDeclention.nom_voc_abl_sn[noun_input]
            if case_input == '2':
                if number_input == '2':
                    return FirstDeclention.gen_pl[noun_input]
                return FirstDeclention.gen_dat_sn_nom_voc_pl
            if case_input == '3':
                if number_input == '2':
                    return FirstDeclention.dat_abl_pl[noun_input]
                return FirstDeclention.gen_dat_sn_nom_voc_pl[noun_input]
            if case_input == '4':
                if number_input == '2':
                    return FirstDeclention.acc_pl[noun_input]
                return FirstDeclention.acc_sn[noun_input]
            if case_input == '5':
                if number_input == '2':
                    return FirstDeclention.dat_abl_pl[noun_input]
                return FirstDeclention.nom_voc_abl_sn[noun_input]


noun_input = input('noun: ')
case_input = input('choose a case: 1-nom 2-gen 3-dat 4-acc 5-abl 6-voc: ')
number_input = input('1-sn.  2-pl.: ')
noun = FirstDeclention(noun_input, number_input, case_input)
print(noun.case_func())
