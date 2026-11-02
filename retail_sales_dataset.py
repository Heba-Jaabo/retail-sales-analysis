import pandas as pd
import numpy as np

# قراءة ملف البيانات
df = pd.read_csv('retail_sales_dataset.csv')

# استعراض أول 5 صفوف للتعرف على شكل البيانات والأعمدة
print("First 5 rows of the dataset:")
df.head()

# معرفة معلومات عامة عن الأعمدة وأنواع البيانات وهل توجد قيم مفقودة (Missing Values)
print("\nDataset Info:")
df.info()

# فحص القيم المفقودة بالأرقام
print("\nMissing values per column:")
print(df.isnull().sum())
# 1. تحويل عمود التاريخ إلى صيغة زمنيّة صحيحة (ملاحظة: استبدلي 'Date' باسم عمود التاريخ تماماً كما ظهر عندك)
df['Date'] = pd.to_datetime(df['Date'])

# 2. إزالة أي صفوف مكررة إن وجدت لضمان دقة التحليل
df.drop_duplicates(inplace=True)

# 3. عرض ملخص إحصائي سريع للأرقام (مثل أقل وأعلى سعر، ومتوسط المبيعات)
print("--- ملخص إحصائي سريع ---")
df.describe()
# التأكد من تحويل التاريخ بشكل صحيح
df['Date'] = pd.to_datetime(df['Date'])

# 1. إجمالي المبيعات حسب فئة المنتجات (Product Category)
sales_by_category = df.groupby('Product Category')['Total Amount'].sum().reset_index()
print("--- إجمالي المبيعات حسب فئة المنتجات ---")
print(sales_by_category)

# 2. إجمالي المبيعات حسب الجنس (Gender)
sales_by_gender = df.groupby('Gender')['Total Amount'].sum().reset_index()
print("\n--- إجمالي المبيعات حسب الجنس ---")
print(sales_by_gender)

# 3. متوسط أعمار العملاء حسب الفئة أو بشكل عام
print(f"\nمتوسط عمر العملاء: {df['Age'].mean():.1f} سنة")
import matplotlib.pyplot as plt
import seaborn as sns

# ضبط تنسيق الرسم البياني
plt.figure(figsize=(8, 5))

# رسم المبيعات حسب الفئة
sns.barplot(x='Product Category', y='Total Amount', data=sales_by_category, palette='viridis')
plt.title('Total Sales by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.show()