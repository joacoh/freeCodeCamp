# %%
import numpy as np 

def calculate(input_list):
    if len(input_list)!=9:
        raise ValueError('List must contain nine numbers.')
    else:
        a = np.empty((3,3))
        x = 0
        y = 0
        for i in input_list: 
            if x<=2:
                a[y,x] = i 
                x += 1
            elif x<=5:
                y = 1
                a[y,x-3] = i
                x += 1 
            elif x<=8:
                y = 2
                a[y,x-6] = i
                x += 1
        mean0 = a.mean(axis=0).tolist()
        mean1 = a.mean(axis=1).tolist()
        meant = a.mean()
        meant = [mean0, mean1, meant]

        var0 = a.var(axis=0).tolist()
        var1 = a.var(axis=1).tolist()
        vart = np.var(a)
        vart = [var0, var1, vart]

        std0 = a.std(axis=0).tolist()
        std1 = a.std(axis=1).tolist()
        stdt = np.std(a)
        stdt = [std0, std1, stdt]

        max0 = a.max(axis=0).tolist()
        max1 = a.max(axis=1).tolist()
        maxt = np.max(a)
        maxt = [max0, max1, maxt]

        min0 = a.min(axis=0).tolist()
        min1 = a.min(axis=1).tolist()
        mint = np.min(a)
        mint = [min0, min1, mint]

        sum0 = a.sum(axis=0).tolist()
        sum1 = a.sum(axis=1).tolist()
        sumt = np.sum(a)
        sumt = [sum0, sum1, sumt]

        new_dict = {
            'mean': meant,
            'variance': vart,
            'standard deviation': stdt,
            'max': maxt,
            'min': mint,
            'sum': sumt
        }
        
    return new_dict

li = [0, 1, 2, 3, 4, 5, 6, 7, 8]

print(calculate(li))
# %%
