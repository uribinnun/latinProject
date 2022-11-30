class FirstDeclention:
    gender = 'f.'
    first_declention_cloud = ['magistra', 'dea', 'amica', 'regina', 'discipula', 'silva', 'hora', 'villa', 'lingua'
                                , 'familia', 'cura', 'forma', 'vita', 'olea', 'pugna', 'patria', 'culpa', 'via',
                              'causa', 'gloria', 'sapientia', 'ira', 'fabula', 'porta', 'iustitia', 'roma', 'agricola',
                              'poeta', 'nauta'
                              ]

    def __init__(self, stem, number, case):
        self.stem = stem
        self.number = number
        self.case = case

    def case_func(self):
        if noun_input in FirstDeclention.first_declention_cloud:
            if self.number == '1':
                if self.case == '1':
                    return '{}'.format(self.stem + 'a')
                if self.case == '2':
                    return '{}'.format(self.stem + 'ae')
                if self.case == '3':
                    return '{}'.format(self.stem + 'ae')
                if self.case == '4':
                    return '{}'.format(self.stem + 'am')
                if self.case == '5':
                    return '{}'.format(self.stem + 'a')
                if self.case == '6':
                    return '{}'.format(self.stem + 'a')
            if self.number == '2':
                if self.case == '1':
                    return '{}'.format(self.stem + 'ae')
                elif self.case == '2':
                    return '{}'.format(self.stem + 'arum')
                elif self.case == '3':
                    return '{}'.format(self.stem + 'is')
                elif self.case == '4':
                    return '{}'.format(self.stem + 'as')
                elif self.case == '5':
                    return '{}'.format(self.stem + 'is')
                elif self.case == '6':
                    return '{}'.format(self.stem + 'ae')


noun_input = input('noun: ')
case_input = input('choose a case: 1-nom 2-gen 3-dat 4-acc 5-abl 6-voc: ')
number_input = input('1-sn.  2-pl.: ')
noun_1 = FirstDeclention(f'{noun_input[:-1]}', number_input, case_input)
print(noun_1.case_func())