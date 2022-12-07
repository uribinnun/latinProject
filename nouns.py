class Nouns:
    output = ()
    from database import first_declention_cloud
    from database import second_declention_cloud
    def __init__(self, stem, number, case):
        self.stem = stem
        self.number = number
        self.case = case


class FirstDeclention(Nouns):
    acc_sn = {}
    acc_pl = {}
    nom_voc_abl_sn = {}
    gen_dat_sn_nom_voc_pl = {}
    dat_abl_pl = {}
    gen_pl = {}
    for object in Nouns.first_declention_cloud:
        acc_sn[object] = [f"{object[:-1]}am"]
        acc_pl[object] = [f"{object[:-1]}as"]
        nom_voc_abl_sn[object] = [object]
        gen_dat_sn_nom_voc_pl[object] = [f"{object[:-1]}ae"]
        dat_abl_pl[object] = [f"{object[:-1]}is"]
        gen_pl[object] = [f"{object[:-1]}arum"]

    def case_func_1(self):
        if noun_input in FirstDeclention.first_declention_cloud:
            if case_input == '1':
                if number_input == '2':
                    return FirstDeclention.gen_dat_sn_nom_voc_pl[noun_input]
                return FirstDeclention.nom_voc_abl_sn[noun_input]
            if case_input == '2':
                if number_input == '2':
                    return FirstDeclention.gen_pl[noun_input]
                return FirstDeclention.gen_dat_sn_nom_voc_pl[noun_input]
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
            if case_input == '6':
                if number_input == '2':
                    return FirstDeclention.gen_dat_sn_nom_voc_pl[noun_input]
                return FirstDeclention.nom_voc_abl_sn[noun_input]


class SecondDeclention(Nouns):
    pass


class Masculine(SecondDeclention):
    m_nom_sn = {}
    m_gen_sn__nom_voc_pl = {}
    m_gen_pl = {}
    m_dat_abl_sn = {}
    m_dat_abl_pl = {}
    m_acc_sn = {}
    m_acc_pl = {}
    m_voc_sn = {}

    for object in Nouns.second_declention_cloud['masculine']:
        m_nom_sn[object] = object
        m_gen_sn__nom_voc_pl = f"{object[:-2]}i"
        m_gen_pl = f"{object[:-2]}orum"
        m_dat_abl_sn = f'{object[:-2]}o'
        m_dat_abl_pl = f'{object[:-2]}is'
        m_acc_sn = f"{object[:-2]}um"
        m_acc_pl = f"{object[:-2]}as"
        m_voc_sn = f"{object[:-2]}e"

    def case_func_2m(self):
        if noun_input in Nouns.second_declention_cloud['masculine']:
            if case_input == '1':
                if number_input == '2':
                    return Masculine.m_gen_sn__nom_voc_pl[noun_input]
                return Masculine.m_nom_sn[noun_input]
            if case_input == '2':
                if number_input == '2':
                    return Masculine.m_gen_pl[noun_input]
                return Masculine.m_gen_sn__nom_voc_pl[noun_input]
            if case_input == '3':
                if number_input == '2':
                    return Masculine.m_dat_abl_pl[noun_input]
                return Masculine.m_dat_abl_sn[noun_input]
            if case_input == '4':
                if number_input == '2':
                    return Masculine.m_acc_pl[noun_input]
                return Masculine.m_acc_sn[noun_input]
            if case_input == '5':
                if number_input == '2':
                    return Masculine.m_dat_abl_pl[noun_input]
                return Masculine.m_dat_abl_sn[noun_input]
            if case_input == '6':
                if number_input == '2':
                    return Masculine.m_gen_sn__nom_voc_pl[noun_input]
                return Masculine.m_voc_sn[noun_input]
        else:
            raise TypeError


noun_input = input('noun: ')
case_input = input('choose a case: 1-nom 2-gen 3-dat 4-acc 5-abl 6-voc: ')
number_input = input('1-sn.  2-pl.: ')
if noun_input in Nouns.first_declention_cloud:
    noun = FirstDeclention(noun_input, number_input, case_input)
    print(noun.case_func_1())
elif noun_input in Nouns.second_declention_cloud:
    noun = SecondDeclention(noun_input, number_input, case_input)
    print(noun.case_func_2m())
