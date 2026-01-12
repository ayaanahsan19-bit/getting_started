import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set the visual style
sns.set_style("whitegrid")
plt.figure(figsize=(15, 12))

# Read the data
df = pd.read_csv('nobel_prize.csv')

# 1. Gender Distribution Pie Chart
plt.subplot(3, 3, 1)
gender_counts = df['sex'].value_counts()
plt.pie(gender_counts.values, labels=gender_counts.index, autopct='%1.1f%%', 
        colors=['skyblue', 'lightcoral', 'lightgreen'])
plt.title('Gender Distribution of Nobel Prize Winners')

# 2. Top 10 Birth Countries Bar Chart
plt.subplot(3, 3, 2)
top_countries = df['birth_country'].value_counts().head(10)
sns.barplot(x=top_countries.values, y=top_countries.index, palette='viridis')
plt.xlabel('Number of Winners')
plt.title('Top 10 Birth Countries')

# 3. Nobel Prizes by Category
plt.subplot(3, 3, 3)
category_counts = df['category'].value_counts()
sns.barplot(x=category_counts.values, y=category_counts.index, palette='Set2')
plt.xlabel('Number of Awards')
plt.title('Nobel Prizes by Category')

# 4. Awards Over Time (Line Chart)
plt.subplot(3, 3, 4)
df['year'] = pd.to_numeric(df['year'], errors='coerce')
yearly_counts = df['year'].value_counts().sort_index()
plt.plot(yearly_counts.index, yearly_counts.values, marker='o', linewidth=2)
plt.xlabel('Year')
plt.ylabel('Number of Awards')
plt.title('Nobel Prizes Awarded Over Time')
plt.grid(True, alpha=0.3)

# 5. Gender Distribution by Category (Heatmap)
plt.subplot(3, 3, 5)
gender_by_category = pd.crosstab(df['category'], df['sex'], normalize='index')
sns.heatmap(gender_by_category, annot=True, fmt='.1%', cmap='YlOrRd', cbar_kws={'label': 'Percentage'})
plt.title('Gender Distribution by Category')
plt.ylabel('Category')
plt.xlabel('Gender')

# 6. Age at Award (if we had birth_year and award_year)
# Assuming we can extract year from birth_date
df['birth_year'] = pd.to_datetime(df['birth_date'], errors='coerce').dt.year
df['age_at_award'] = df['year'] - df['birth_year']

plt.subplot(3, 3, 6)
sns.histplot(data=df.dropna(subset=['age_at_award']), x='age_at_award', bins=20, 
             kde=True, color='purple', alpha=0.6)
plt.xlabel('Age at Award')
plt.ylabel('Frequency')
plt.title('Distribution of Age When Winning')

# 7. Nobel Prizes by Decade
plt.subplot(3, 3, 7)
df['decade'] = (df['year'] // 10) * 10
decade_counts = df['decade'].value_counts().sort_index()
sns.barplot(x=decade_counts.index.astype(str), y=decade_counts.values, palette='coolwarm')
plt.xlabel('Decade')
plt.ylabel('Number of Awards')
plt.title('Nobel Prizes by Decade')
plt.xticks(rotation=45)

# 8. US-born Winners Ratio by Decade
plt.subplot(3, 3, 8)
individuals = df[df['laureate_type'] == 'Individual']
decade_ratios = {}

for decade in sorted(individuals['decade'].unique()):
    decade_data = individuals[individuals['decade'] == decade]
    total = len(decade_data)
    us_born = len(decade_data[decade_data['birth_country'] == 'United States of America'])
    if total > 0:
        decade_ratios[decade] = (us_born / total) * 100

decades = list(decade_ratios.keys())
ratios = list(decade_ratios.values())

plt.bar([str(d) for d in decades], ratios, color='orange', alpha=0.7)
plt.xlabel('Decade')
plt.ylabel('Percentage (%)')
plt.title('Percentage of US-born Winners by Decade')
plt.xticks(rotation=45)

# 9. Repeat Winners (Top 5)
plt.subplot(3, 3, 9)
winner_counts = df['full_name'].value_counts()
repeat_winners = winner_counts[winner_counts > 1].head(5)

if len(repeat_winners) > 0:
    sns.barplot(x=repeat_winners.values, y=repeat_winners.index, palette='mako')
    plt.xlabel('Number of Awards')
    plt.title('Top 5 Repeat Winners')
else:
    plt.text(0.5, 0.5, 'No repeat winners', ha='center', va='center', fontsize=12)
    plt.title('Repeat Winners')

plt.tight_layout()
plt.show()

# Additional Specialized Visualizations

# 1. Timeline of First Women Winners by Category
plt.figure(figsize=(12, 6))
first_women = []

for category in df['category'].unique():
    category_women = df[(df['category'] == category) & (df['sex'] == 'Female')]
    if not category_women.empty:
        first_woman = category_women.loc[category_women['year'].idxmin()]
        first_women.append(first_woman)

first_women_df = pd.DataFrame(first_women)
if not first_women_df.empty:
    first_women_df = first_women_df.sort_values('year')
    
    plt.barh(first_women_df['category'], first_women_df['year'], 
             color=['pink', 'lightblue', 'lightgreen', 'lavender', 'peachpuff', 'lightcyan'])
    plt.xlabel('Year')
    plt.title('Year When First Woman Won in Each Category')
    plt.grid(True, alpha=0.3)
    
    # Add names as text
    for i, (name, year) in enumerate(zip(first_women_df['full_name'], first_women_df['year'])):
        plt.text(year + 0.5, i, name[:15] + '...', va='center', fontsize=8)

plt.tight_layout()
plt.show()

# 2. Comparison of Male vs Female Winners Over Time
plt.figure(figsize=(14, 5))

# Male winners over time
plt.subplot(1, 2, 1)
male_yearly = df[df['sex'] == 'Male'].groupby('year').size().reset_index(name='count')
plt.plot(male_yearly['year'], male_yearly['count'], 'b-', linewidth=2, label='Male')
plt.fill_between(male_yearly['year'], male_yearly['count'], alpha=0.3, color='blue')
plt.xlabel('Year')
plt.ylabel('Number of Awards')
plt.title('Male Winners Over Time')
plt.grid(True, alpha=0.3)
plt.legend()

# Female winners over time
plt.subplot(1, 2, 2)
female_yearly = df[df['sex'] == 'Female'].groupby('year').size().reset_index(name='count')
plt.plot(female_yearly['year'], female_yearly['count'], 'r-', linewidth=2, label='Female')
plt.fill_between(female_yearly['year'], female_yearly['count'], alpha=0.3, color='red')
plt.xlabel('Year')
plt.ylabel('Number of Awards')
plt.title('Female Winners Over Time')
plt.grid(True, alpha=0.3)
plt.legend()

plt.tight_layout()
plt.show()

# 3. Category Distribution by Decade (Heatmap)
plt.figure(figsize=(12, 8))
category_decade = pd.crosstab(df['category'], df['decade'])
sns.heatmap(category_decade, annot=True, fmt='d', cmap='Blues', 
            cbar_kws={'label': 'Number of Awards'})
plt.title('Number of Awards by Category and Decade')
plt.xlabel('Decade')
plt.ylabel('Category')
plt.tight_layout()
plt.show()

# 4. Box Plot of Age by Category
plt.figure(figsize=(12, 6))
if 'age_at_award' in df.columns:
    # Remove outliers for better visualization
    age_data = df.dropna(subset=['age_at_award'])
    age_data = age_data[age_data['age_at_award'].between(age_data['age_at_award'].quantile(0.01), 
                                                          age_data['age_at_award'].quantile(0.99))]
    
    sns.boxplot(data=age_data, x='category', y='age_at_award', palette='Set3')
    plt.xlabel('Category')
    plt.ylabel('Age at Award')
    plt.title('Age Distribution by Category')
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    
plt.tight_layout()
plt.show()

# 5. Interactive-style Visualization: Multiple Awards per Year
plt.figure(figsize=(14, 6))
# Count how many categories were awarded each year
yearly_category_counts = df.groupby('year')['category'].nunique()

plt.bar(yearly_category_counts.index, yearly_category_counts.values, 
        color='teal', alpha=0.7, edgecolor='black')
plt.xlabel('Year')
plt.ylabel('Number of Categories Awarded')
plt.title('Number of Nobel Prize Categories Awarded Each Year (Max = 6)')
plt.grid(True, alpha=0.3)

# Highlight years with fewer than 6 categories
for year, count in yearly_category_counts.items():
    if count < 6:
        plt.bar(year, count, color='red', alpha=0.5)

plt.tight_layout()
plt.show()

print("Visualizations completed! Here are some key insights:")
print(f"1. Total number of Nobel Prize winners: {len(df)}")
print(f"2. Number of unique categories: {df['category'].nunique()}")
print(f"3. Time span: {df['year'].min()} - {df['year'].max()}")
print(f"4. Percentage of female winners: {(df['sex'] == 'Female').sum()/len(df)*100:.1f}%")
print(f"5. Most common category: {df['category'].value_counts().index[0]}")