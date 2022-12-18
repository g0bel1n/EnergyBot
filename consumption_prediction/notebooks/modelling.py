#%%
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import pickle

#%%
df = pd.read_csv("../data/synthetic/data.csv", index_col=0)
df.head()
#%%
df.info()
#%%
df.describe()
#%%
df.isna().sum()
#%%
D_train, D_test = train_test_split(df, test_size=0.2, random_state=42)
#%%
X_train = D_train.drop("target", axis=1)
y_train = D_train["target"]
X_test = D_test.drop("target", axis=1)
y_test = D_test["target"]
#%%
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
#%%
y_pred = rf.predict(X_test)
#%%
mean_squared_error(y_test, y_pred, squared=False)
#%%
rf.feature_importances_
#%%
importances = pd.DataFrame(rf.feature_importances_, index=X_train.columns, columns=["importance"])
importances.sort_values("importance", ascending=False)
#%%
importances.sort_values("importance", ascending=False).plot(kind="bar")
#%%
rf.score(X_test, y_test)
# %%

pickle.dump(rf, open("model.pkl", "wb")) 

# %%
rf1 = pickle.load(open("model.pkl", "rb"))
# %%
rf1.score(X_test, y_test)
# %%
