import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df_og = pd.read_excel('./Dataset_for_suicide_prevention.xlsx')
df = df_og.drop_duplicates()
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
plt.figure(figsize=(10, 8))
numeric_corr = df.select_dtypes(include=[np.number]).corr()  # Compute correlation matrix
sns.heatmap(
    numeric_corr,
    annot=True,
    fmt=".2f",  # Format numbers to 2 decimal places
    cmap="coolwarm",
    linewidths=0.5,  # Borders between cells
    cbar_kws={"shrink": 0.8}  # Shrink color bar for nicer fit
)
plt.title("Correlation Heatmap of Numeric Features", fontsize=14)
plt.xticks(rotation=45, ha='right')  # Rotate labels for clarity
plt.yticks(rotation=0)
plt.tight_layout()  # Prevent label cutoff
plt.show()


# Proportion of positive triggers
plt.figure(figsize=(6, 6))
df['IsPositiveTrigger'].value_counts().plot.pie(autopct='%1.1f%%', colors=['red', 'green'])
plt.title('Proportion of Positive vs. Negative Triggers')
plt.ylabel('')
plt.show()


def get_recommendations(level: int) -> str:
    recommendations = {
        1: """🟢 רמה 1 – נמוכה מאוד:
- האזן למוזיקה אהובה 🎵
- צא לטיול קצר 🚶‍♂️
- כתוב יומן רגשי חיובי 📓
- שתף חבר בתחושות קלות 🗣️""",

        2: """🟡 רמה 2 – נמוכה:
- תרגול נשימות עמוקות 🧘‍♂️
- מדיטציה מונחית קצרה (5-10 דק׳) 🧘‍♀️
- פעילות גופנית קלה 🤸‍♀️
- אפליקציה לניהול רגשות (כמו Headspace או Calm) 📱""",

        3: """🟠 רמה 3 – בינונית:
- תרגול יומיומי של מיינדפולנס 🧠
- שיחה עם יועץ, חבר תומך או מורה 🗨️
- הפסקה ממסכים ורשתות 📵
- כתיבה אינטואיטיבית או יצירה חופשית 🎨""",

        4: """🔴 רמה 4 – גבוהה:
- פנייה לייעוץ רגשי מקצועי 🧑‍⚕️
- הפחתת גירויים מתוחים (כמו חדשות) 📺
- שמירה על סדר יום יציב 🗓️
- קבוצה טיפולית או קבוצת תמיכה 👥""",

        5: """🚨 רמה 5 – גבוהה מאוד:
- שיחה דחופה עם פסיכולוג/עו״ס 📞
- קירבה לאנשים תומכים ❤️
- יצירת סביבה רגועה ובטוחה 🛋️
- הפחתה בגירויים שליליים 💡""",

        6: """❗ רמה 6 – בלתי ניתנת להכלה:
⚠️ יש לפנות מיד לעזרה מקצועית:
- ☎️ התקשר למוקד עזרה ראשונה נפשית: 1201 (ער״ן)
- אל תישאר לבד – שתף אדם קרוב 🧍‍♂️🧍‍♀️
- אם יש סכנה מיידית – פנה לחדר מיון או התקשר 101 🚑"""
    }

    return recommendations.get(level, "רמת סיווג לא חוקית. אנא בחר מספר בין 1 ל-6.")


# Testing succeded
'''advice = get_recommendations(4)
print(advice)'''
