total_student = input()
A_student = 20
B_student = 0
C_student =30

total_A= (A_student/100)*total_student
total_C= (C_student/100)*total_student

total_B = total_student - (total_A + total_C)
print(f"\nTotal number of A students are {total_A}")
print(f"\nTotal number of C students are {total_C}")

print(f"\nTotal number of B students are {int(total_B)}")

