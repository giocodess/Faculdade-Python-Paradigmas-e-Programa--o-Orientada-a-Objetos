import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({'lab':['A', 'B', 'C','D'], 'val':[3, 8, 1,10]})
ax = df.plot.bar(x='lab', y='val', rot=0)

##x [A,B,C,D]
##Y [3,8,1,10]

