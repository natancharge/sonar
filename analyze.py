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

# Distribution of numeric severity
plt.figure(figsize=(8, 6))
sns.histplot(df['SeverityNumeric'], bins=np.arange(1, 8)-0.5, kde=True)
plt.title("Numeric Severity Distribution")
plt.xlabel("Severity Numeric")
plt.ylabel("Frequency")
plt.xticks(range(1, 7))
plt.show()

# Most common trigger words
trigger_counts = df['TriggerWords'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(y=trigger_counts.index, x=trigger_counts.values)
plt.title("Top 10 Trigger Words")
plt.xlabel("Number of Occurrences")
plt.ylabel("Trigger word")
plt.show()

# Correlation heatmap (numeric fields)
plt.figure(figsize=(8, 6))
sns.heatmap(df.select_dtypes(include=[np.number]).corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap of Numeric Features")
plt.show()

# Proportion of positive triggers
plt.figure(figsize=(6, 6))
df['IsPositiveTrigger'].value_counts().plot.pie(autopct='%1.1f%%', colors=['red', 'green'])
plt.title('Proportion of Positive vs. Negative Triggers')
plt.ylabel('')
plt.show()