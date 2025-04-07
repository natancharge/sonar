import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_excel('./Dataset_for_suicide_prevention.xlsx')
print(df.info())

# Severity distribution
plt.figure(figsize=(8, 6))
sns.countplot(x='Severity', data=df, order=['בלתי ניתנת להכלה', 'גבוהה מאוד', 'גבוהה', 'בינונית', 'נמוכה', 'נמוכה מאוד'])
plt.title("Distribution of Severity Levels")
plt.xlabel("Severity Level")
plt.ylabel("Number of Records")
plt.xticks(rotation=45)
plt.show()

