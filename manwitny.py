# Example of the Mann-Whitney U Test
from scipy.stats import mannwhitneyu
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data_befor=[3555,3148,3288,3416,3098,3171,3026,3446,3976,3776,3526,4003,3642,3505,3198,3814,4435,4189,4227,4359,4451,5012,5189,4814,4548,3961,6998,5861,4087,3163,4271,3965,4140,4091,4099,4606,4225,3706,3285,342,1461,1619,2704,2810,2652,2546,1952,1699,2526,3817,4126,3743,3432,3708,3129,3342,3592,3305,3004,3124,2968,2681,2992,3518,3235,2929,2840,2646,2464,2593,2864,2852,2502,2413,2359,2245,2368,2601,2562,2257,2366,2305,2058,2154,2576,2289,2002,2134]
data_after=[2993,2967,3130,2886,3190,3306,3520,5224,5228,4980,5173,4068,3592,4466,4632,3412,3271,3388,3199,3136,3014,3455,3699,3370,4019,4512,4910,5088,4876,4839,4930,5019,5218,5070,4688,5195,6702,5940,4410,4178,3678,3882,3907,3444,2570,2237,2844,3235,3130,3439,3753,4575,4363,3765,4241,3981,4635,4686,4314,3969,3711,3691,3542,3867,4083,4236,4397,3954,4036,4389,4316,4387,4168,4344,3916,3881,4331,4862,3554,4470,4016,3932,3907,3947,2771,2869,3785,3083]


b = pd.Series(data_befor)
print(b.describe())



plt.hist(data_befor, density=False, bins="auto")  # density=False would make counts
plt.show()

plt.boxplot(data_befor)
plt.show()

a = pd.Series(data_after)
print(a.describe())


plt.hist(data_after, density=False, bins="auto")
plt.show()

plt.boxplot(data_after)
plt.show()



stat, p = mannwhitneyu(data_before, data_after)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably the same distribution')
else:
	print('Probably different distributions')