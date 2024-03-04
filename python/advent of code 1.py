import csv

file = "C:\\Users\\hfchi\python\\bob\\inputadvent1.csv"

def digit_grabber(file):
    all_digits = []
    with open(file) as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            res = []
            x=file.split()
            for i in x:
                if i.isnumeric():
                    res.append(int(i))  
            # first_digit = 
        print(res)


def read_list(file):
    list = []
    total = 0
    with open(file) as csv_file:
        reader = csv.reader(csv_file, delimiter=',', quotechar='"')
        for line in reader:
            string_kekeke = line[0].strip()
            string_keke = " ".join(string_kekeke)
            string_keke = string_keke.replace("o n e", "o 1 e")
            string_keke = string_keke.replace("t w o", "t 2 o")
            string_keke = string_keke.replace("t h r e e", "t 3 e")
            string_keke = string_keke.replace("f o u r", "f 4 r")
            string_keke = string_keke.replace("f i v e", "f 5 e")
            string_keke = string_keke.replace("s i x", "s 6 x")
            string_keke = string_keke.replace("s e v e n", "s 7 n")
            string_keke = string_keke.replace("e i g h t", "e 8 t")
            string_keke = string_keke.replace("n i n e", "n 9 e")

            
            res = [int(i) for i in string_keke.split() if i.isdigit()]
            print(res)
            #taking first and last numbers
            first_number = res[0]
            last_number = res[-1]
            #first number x 10 + last number
            final_number = int(first_number)*10 + int(last_number)
            #adding them all up
            total = total + final_number

    print(total)
   

read_list(file)



