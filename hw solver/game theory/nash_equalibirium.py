import itertools
import more_itertools as mit
import numpy as np
import nashpy as nash
from pprint import pprint
i = 0
row = []
col = []
for comb in mit.distinct_permutations([1,1,0,0]):
    row.append(list(comb))
    col.append(list(comb))
result = []
for i in range(len(row)):
    temp_result = []
    for j in range(len(col)):
        temp = []
        temprow = []
        temprow.extend(row[i])
        for k in range(len(row[i])):
            a = temprow[k] - col[j][k]
            if a == -1:
                try:
                    temprow[k+1] = 0
                except IndexError:
                    pass
            temp.append(a)
        temp_result.append(temp.count(1))
    result.append(temp_result)

result = np.array(result)
result = np.flip(result,0)
result = np.flip(result,1)
print(result)

rps = nash.Game(result)

pprint(next(rps.support_enumeration(tol=0)))