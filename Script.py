
class ChrCounter:
    total = 0

    def __init__(self, file_name):
        self.file_name = file_name
        self.char_dict = {}
        self.char_list = []

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def collect(self):
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                for char in line:
                    if char in self.char_dict and char.isalpha():
                        self.char_dict[char] += 1
                    elif char.isalpha():
                        self.char_dict[char] = 1
                    else:
                        continue

    def convert(self):
        """конвертирует словарь с данными в список"""
        for k, v in self.char_dict.items():
            self.char_list += [[k, v]]
            self.total += v

    def pretty_print(self):
        self.convert()
        headers = ['буква', 'частота']
        print(tabulate(self.char_list, headers, tablefmt='pretty'))
        print('| итого |', self.total, '|\n+-------+---------+')


class ChrCounterAlphOrder(ChrCounter):

    def pretty_print(self):
        self.convert()
        self.char_list.sort()
        headers = ['буква', 'частота']
        print(tabulate(self.char_list, headers, tablefmt='pretty'))
        print('| итого |', self.total, '|\n+-------+---------+')


class ChrCounterAlphReversedOrder(ChrCounter):

    def pretty_print(self):
        self.convert()
        self.char_list.sort(reverse=True)
        headers = ['буква', 'частота']
        print(tabulate(self.char_list, headers, tablefmt='pretty'))
        print('| итого |', self.total, '|\n+-------+---------+')


class ChrCounterFrequencyOrder(ChrCounter):

    def pretty_print(self):
        self.convert()
        self.char_list.sort(key=lambda i: i[1], reverse=True)
        headers = ['буква', 'частота']
        print(tabulate(self.char_list, headers, tablefmt='pretty'))
        print('| итого |', self.total, '|\n+-------+---------+')



# test = ChrCounter("voyna-i-mir.txt.zip")
# test.unzip()
# test.collect()
# test.pretty_print()

