#Numbers are inputted and array "sequence" is created
print("Created By Faisal Ahmed")
number1 = float(input("Number 1"))
number2 = float(input("Number 2"))
number3 = float(input("Number 3"))
number4 = float(input("Number 4"))
number5 = float(input("Number 5"))
sequence = [number1, number2, number3, number4, number5]
print(sequence)

#Calculating difference 1
dif1num1 = number2 - number1
dif1num2 = number3 - number2
dif1num3 = number4 - number3
dif1num4 = number5 - number4

#Calculating difference 2

dif2num1 = dif1num2 - dif1num1
dif2num2 = dif1num3 - dif1num2
dif2num3 = dif1num4 - dif1num3
dif_array = [dif2num1, dif2num2, dif2num3]
print(dif_array)
#Confirming quadratic

valid1 = int(0)
valid2 = int(0)
valid3 = int(0)

if dif2num1 and dif2num2 == dif2num3:
    valid3 = valid3 + 1

if valid3 == 0:
  print("The sequence is not quadratic")

var_ns = dif2num1 / 2

one_n_squared_1 = 1
one_n_squared_2 = 4
one_n_squared_3 = 9
one_n_squared_4 = 16
one_n_squared_5 = 25

new_n_squared_1 = one_n_squared_1 * var_ns
new_n_squared_2 = one_n_squared_2 * var_ns
new_n_squared_3 = one_n_squared_3 * var_ns
new_n_squared_4 = one_n_squared_4 * var_ns
new_n_squared_5 = one_n_squared_5 * var_ns

diff1 = number1 - new_n_squared_1
diff2 = number2 - new_n_squared_2

dif_01 = dif2num1 / 2
dif_02 = str(dif_01)
dif_03 = (dif_02 + "n squared")


diff_final = diff2 - diff1
diff_final_str = str(diff_final)
print(dif_03 + "+" + diff_final_str + "n")