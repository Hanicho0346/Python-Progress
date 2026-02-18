import numpy as np
import pandas as pd

age = np.array([22, 24, 50, 34, 55, 19])
salary = np.array([100, 2000, 3000, 4000, 5000, 6000])
gender = np.array(["female", "male", "male", "female", "female", "male"])
bought = np.array([0, 1, 0, 1, 1, 0])

df = pd.DataFrame({
    'age': age,
    'salary': salary,
    'gender': gender,
    'bought': bought
})

df_encoded = pd.get_dummies(df, columns=['gender'])

print(df_encoded)
