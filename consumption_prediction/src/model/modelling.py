from pickle import load, dump
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


df = read_csv("../data/synthetic/data.csv", index_col=0)

D_train, D_test = train_test_split(df, test_size=0.2, random_state=42)

X_train = D_train.drop("target", axis=1)
y_train = D_train["target"]
X_test = D_test.drop("target", axis=1)
y_test = D_test["target"]

rf = RandomForestRegressor(n_estimators=100, random_state=42)

rf.fit(X_train, y_train)

y_pred = rf.predict(X_test)

importances = pd.DataFrame(
    rf.feature_importances_,
    index=X_train.columns,
    columns=["importance"]
)

rf.score(X_test, y_test)

dump(rf, open("model.pkl", "wb"))

rf1 = load(open("model.pkl", "rb"))

rf1.score(X_test, y_test)
