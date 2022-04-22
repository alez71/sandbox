import nashpy as nash
import numpy as np
A = np.array([[-2,0,5,1,2,-4], [3,4,-3,-1,0,8]])
rps = nash.Game(A)
print(rps)
eqs = rps.lemke_howson_enumeration()

print(list(eqs))