import numpy as np
import math as m

array0 = np.zeros((3, 4))
print("This an empty array filled with 0s")
print(array0)

degrees = np.degrees(m.pi)
print(f"Conversion of radians to degrees {degrees}")

hyp = np.hypot(4, 3)
print(f"Hypotenuse of a triangule with sides of 3 and 4: {hyp}")

log = np.log10(1000)
print(f"Logarithm of 1000 is {log}")

mod = np.mod(15, 3)
print(f"The remainder of 15 / 3 is {mod}")
