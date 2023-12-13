# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy as np

# Read the Bowling Data from CSV
Bowling_data = pd.read_csv('Bowling_Stats.csv')
Bowling_data

# Display information about the dataset
Bowling_data.info()

# Display descriptive statistics of the dataset
Bowling_data.describe()

# Display the columns of the dataset
Bowling_data.columns

# Extract and visualize the top 10 wicket-takers with bar chart
bar_1 = Bowling_data[['Bowlers','Wkts']]
bar_1

bar_1_sorted = bar_1.sort_values(by='Wkts', ascending=False)
top_10_wicket_takers = bar_1_sorted.head(10)

plt.figure(figsize=(17, 6)) 
plt.bar(top_10_wicket_takers['Bowlers'], top_10_wicket_takers['Wkts'],color='gray')
plt.xlabel('Bowlers')
plt.ylabel('Wickets')
plt.title('Top 10 Wicket-Taking Bowlers')
plt.show()

# Extract and visualize maiden overs by bowlers with more than 4 maidens with bar chart
bar_2 = Bowling_data[['Bowlers','maiden']]
bar_2

Bowling_data['maiden'] = pd.to_numeric(Bowling_data['maiden'], errors='coerce')
filtered_data = Bowling_data[Bowling_data['maiden'] > 4]

plt.figure(figsize=(12, 6))
plt.bar(filtered_data['Bowlers'], filtered_data['maiden'], color='green', alpha=0.7)
plt.xlabel('Bowlers')
plt.ylabel('Maiden Overs')
plt.title('Maiden Overs by Bowlers (More than 4 maidens)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Analyze and visualize total wickets by country using a pie chart
country_wkts_total = Bowling_data.groupby('Country')['Wkts'].sum()
pie_1 = pd.DataFrame({'Country': country_wkts_total.index, 'Total_Wkts': country_wkts_total.values})
print(pie_1)

plt.pie(pie_1['Total_Wkts'], labels=pie_1['Country'], autopct='%1.1f%%', startangle=90)
plt.title('Total Wickets by Country')
plt.show()

# Analyze and visualize correlations between key bowling metrics
# Correlation Heatmap 1
corelation_1 = Bowling_data[['Innings', 'Balls', 'Overs','Runs', 'Wkts']]
corelation_1

corelation_1 = corelation_1.corr()
corelation_1

plt.figure(figsize=(7,6))
sns.heatmap(data= corelation_1, annot= True, cmap = 'mako', center = 0)

# Correlation Heatmap 2
corelation_2 = Bowling_data[['Average', 'Economy', 'Strike Rate']]
corelation_2

corelation_2 = corelation_2.corr()
corelation_2

plt.figure(figsize=(7,6))
sns.heatmap(data= corelation_2, annot= True, cmap = 'flare', center = -1)

# Correlation Heatmap 3
corelation_3 = Bowling_data[['Match_Played','Overs','Wkts', 'Strike Rate']]
corelation_3

corelation_3 = corelation_3.corr()
corelation_3

plt.figure(figsize=(7,6))
sns.heatmap(data= corelation_3, annot= True)

# Correlation Heatmap 4
corelation_4 = Bowling_data[['Average', 'Economy','Wkts']]
corelation_4

corelation_4 = corelation_4.corr()
corelation_4

plt.figure(figsize=(7,6))
sns.heatmap(data= corelation_4, annot= True, cmap = 'magma', center = -1)
