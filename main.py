F_text = input("Enter the temp in degrees F: ")
F = float(F_text)
C = 5 * (F - 32) / 9
print("The temp in degrees C is", C)

C_text = input("Enter the temp in degrees C: ")
C = float (C_text)
F = 1.8 * C + 32
print ("The temp in F is: ", F)
