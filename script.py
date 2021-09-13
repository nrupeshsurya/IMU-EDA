# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Cleaning and exploring Data

# %%
import pandas as pd
import matplotlib.pyplot as plt 
from mpl_toolkits import mplot3d


# %%
df = pd.read_csv('raw.csv', header=None)


# %%
# df.head()

# %% [markdown]
# ## Making a new dataframe (assuming that this is the right format)

# %%
df1 = pd.DataFrame(columns=['X1','Y1','Z1','X2','Y2','Z2','Label'])


# %%
for j in range(0,15):
    i=1
    while i<596:
        df1 = df1.append({'X1' : df[i][j], 'Y1' : df[i+1][j], 'Z1' : df[i+2][j], 'X2' : df[i+3][j], 'Y2' : df[i+4][j], 'Z2' : df[i+5][j], 'Label' : df[0][j]}, ignore_index=True)
        i=i+6


# %%
# df1.info()


# %%
# df1.head()


# %%
# df.head()


# %%
# df1.tail()


# %%
# df.tail()

# %% [markdown]
# ## Splitting the dataset to visualize 

# %%
lying = df1[df1['Label']==0.0]
standing = df1[df1['Label']==1.0]
walking = df1[df1['Label']==2.0]


# %%
lying_d1 = lying[['X1','Y1','Z1']]
standing_d1 = standing[['X1','Y1','Z1']]
walking_d1 = walking[['X1','Y1','Z1']]

lying_d2 = lying[['X2','Y2','Z2']]
standing_d2 = standing[['X2','Y2','Z2']]
walking_d2 = walking[['X2','Y2','Z2']]

# %% [markdown]
# ## Scatter plot for lying (Sensor 1)

# %%
# threedee = plt.figure().gca(projection='3d')
# threedee.scatter(lying_d1['X1'], lying_d1['Y1'], lying_d1['Z1'], color = 'red')
# # threedee.scatter(standing_d1['X1'], standing_d1['Y1'], standing_d1['Z1'], color = 'green')
# # threedee.scatter(walking_d1['X1'], walking_d1['Y1'], walking_d1['Z1'], color = 'blue')
# threedee.set_xlabel('X')
# threedee.set_ylabel('Y')
# threedee.set_zlabel('Z')
# plt.show()

# %% [markdown]
# ## Scatter plot for standing (Sensor 1)

# %%
# threedee = plt.figure().gca(projection='3d')
# # threedee.scatter(lying_d1['X1'], lying_d1['Y1'], lying_d1['Z1'], color = 'red')
# threedee.scatter(standing_d1['X1'], standing_d1['Y1'], standing_d1['Z1'], color = 'green')
# # threedee.scatter(walking_d1['X1'], walking_d1['Y1'], walking_d1['Z1'], color = 'blue')
# threedee.set_xlabel('X')
# threedee.set_ylabel('Y')
# threedee.set_zlabel('Z')
# plt.show()

# %% [markdown]
# ## Scatter plot for walking (Sensor 1)

# %%
# threedee = plt.figure().gca(projection='3d')
# # threedee.scatter(lying_d1['X1'], lying_d1['Y1'], lying_d1['Z1'], color = 'red')
# # threedee.scatter(standing_d1['X1'], standing_d1['Y1'], standing_d1['Z1'], color = 'green')
# threedee.scatter(walking_d1['X1'], walking_d1['Y1'], walking_d1['Z1'], color = 'blue')
# threedee.set_xlabel('X')
# threedee.set_ylabel('Y')
# threedee.set_zlabel('Z')
# plt.show()

# %% [markdown]
# ## Scatter plot of all three (Sensor 1)

# %%
fig = plt.figure()
ax = plt.axes(projection='3d')
# threedee.scatter(lying_d1['X1'], lying_d1['Y1'], lying_d1['Z1'], color = 'red')
# threedee.scatter(standing_d1['X1'], standing_d1['Y1'], standing_d1['Z1'], color = 'green')
# threedee.scatter(walking_d1['X1'], walking_d1['Y1'], walking_d1['Z1'], color = 'blue')
# threedee.set_xlabel('X')
# threedee.set_ylabel('Y')
# threedee.set_zlabel('Z')
ax.scatter3D(lying_d1['X1'], lying_d1['Y1'], lying_d1['Z1'], color = 'red')
ax.scatter3D(standing_d1['X1'], standing_d1['Y1'], standing_d1['Z1'], color = 'green')
ax.scatter3D(walking_d1['X1'], walking_d1['Y1'], walking_d1['Z1'], color = 'blue')
plt.show()
# %% [markdown]
# ## Scatter plot for lying (Sensor 2)

# %%
# threedee = plt.figure().gca(projection='3d')
# threedee.scatter(lying_d2['X2'], lying_d2['Y2'], lying_d2['Z2'], color = 'red')
# # threedee.scatter(standing_d2['X2'], standing_d2['Y2'], standing_d2['Z2'], color = 'green')
# # threedee.scatter(walking_d2['X2'], walking_d2['Y2'], walking_d2['Z2'], color = 'blue')
# threedee.set_xlabel('X')
# threedee.set_ylabel('Y')
# threedee.set_zlabel('Z')
# plt.show()

# # %% [markdown]
# # ## Scatter plot for standing (Sensor 2)

# # %%
# threedee = plt.figure().gca(projection='3d')
# # threedee.scatter(lying_d2['X2'], lying_d2['Y2'], lying_d2['Z2'], color = 'red')
# threedee.scatter(standing_d2['X2'], standing_d2['Y2'], standing_d2['Z2'], color = 'green')
# # threedee.scatter(walking_d2['X2'], walking_d2['Y2'], walking_d2['Z2'], color = 'blue')
# threedee.set_xlabel('X')
# threedee.set_ylabel('Y')
# threedee.set_zlabel('Z')
# plt.show()

# # %% [markdown]
# # ## Scatter plot for walking (Sensor 2)

# # %%
# threedee = plt.figure().gca(projection='3d')
# # threedee.scatter(lying_d2['X2'], lying_d2['Y2'], lying_d2['Z2'], color = 'red')
# # threedee.scatter(standing_d2['X2'], standing_d2['Y2'], standing_d2['Z2'], color = 'green')
# threedee.scatter(walking_d2['X2'], walking_d2['Y2'], walking_d2['Z2'], color = 'blue')
# threedee.set_xlabel('X')
# threedee.set_ylabel('Y')
# threedee.set_zlabel('Z')
# plt.show()

# # %% [markdown]
# # ## Scatter plot for all three (Sensor 2)

# # %%
# threedee = plt.figure().gca(projection='3d')
# threedee.scatter(lying_d2['X2'], lying_d2['Y2'], lying_d2['Z2'], color = 'red')
# threedee.scatter(standing_d2['X2'], standing_d2['Y2'], standing_d2['Z2'], color = 'green')
# threedee.scatter(walking_d2['X2'], walking_d2['Y2'], walking_d2['Z2'], color = 'blue')
# threedee.set_xlabel('X')
# threedee.set_ylabel('Y')
# threedee.set_zlabel('Z')
fig = plt.figure()
ax = plt.axes(projection='3d')

ax.scatter3D(lying_d2['X2'], lying_d2['Y2'], lying_d2['Z2'], color = 'red')
ax.scatter3D(standing_d2['X2'], standing_d2['Y2'], standing_d2['Z2'], color = 'green')
ax.scatter3D(walking_d2['X2'], walking_d2['Y2'], walking_d2['Z2'], color = 'blue')
plt.show()


