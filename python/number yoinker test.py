

test_string = "Thereare2applesfor4persons"
a = " " .join(test_string)
# print(a) 



res = [int(i) for i in test_string.split() if i.isdigit()]
res2 = [int(i) for i in a.split() if i.isdigit()]
# print result
# print(res)
# print(res2)




#converting word numbers to digits
#eg: one == 1
test_stringer = "o n e 5 0 seven7vnjin e i g h t"
b = test_stringer.replace("o n e", "1" and "e i g h t", "8")

print(b)
