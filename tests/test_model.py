import pickle
import numpy as np 
import pandas as pd 

def test_model():
    rf = pickle.load(open("model/rf.pkl", "rb"))
    x_high = 5*np.ones(7).reshape(1, -1)
    x_low = np.zeros(7).reshape(1, -1)
    fnames = [
        "ecolo score",
        "worday",
        *[f"paysage_{i}" for i in range(4)],
        "nb_habitant",
    ]

    x_high = pd.DataFrame(x_high, columns=fnames)
    x_low = pd.DataFrame(x_low, columns=fnames)
    assert rf.predict(x_high) >= rf.predict(x_low)
    assert rf.predict(x_high) > 0
    assert rf.predict(x_low) > 0
