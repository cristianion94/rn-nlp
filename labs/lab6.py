# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import csv
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


# %%
glove_data_file = "glove.6B/glove.6B.50d.txt"


# %%
df = pd.read_csv(glove_data_file, sep=" ", index_col=0, header=None, quoting=csv.QUOTE_NONE)


# %%
n_components = 2


# %%
dfsample = df[:50]


# %%
dfsample.index.values


# %%
pca = PCA(n_components=n_components)
components = pca.fit_transform(dfsample)

# %% [markdown]
# ## PCA in two dimensions

# %%
plt.scatter(components[:,0], components[:,1])

for i in range(components.shape[0]):
    plt.annotate(df.index.values[i], (components[i,0], components[i,1]))


# %%
components.shape[0]


# %%
nparr = dfsample.to_numpy()

# %% [markdown]
# ## Plot with 2 random dimensions

# %%
plt.scatter(nparr[:,5], nparr[:,7])

for i in range(components.shape[0]):
    plt.annotate(df.index.values[i], (nparr[i,5], nparr[i,7]))

# %% [markdown]
# 

# %%



