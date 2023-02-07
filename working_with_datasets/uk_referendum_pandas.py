import pandas as pd

# Read the datasets into a pandas dataframe
demo_df = pd.read_json(r"https://raw.githubusercontent.com/viveknest/statascratch-solutions/main/UK%20Referendum%20Data/uk_demo.json")
results_df = pd.read_json(r"https://raw.githubusercontent.com/viveknest/statascratch-solutions/main/UK%20Referendum%20Data/uk_results.json")
rejected_df = pd.read_json(r"https://github.com/viveknest/statascratch-solutions/raw/main/UK%20Referendum%20Data/uk_rejected_ballots.json")

# Join the datasets and write to a CSV file
merged_df = pd.merge(left = demo_df, right = results_df, on = 'Area_Code').merge(rejected_df, on = 'Area_Code')
filename = 'uk_ref_pandas.csv'
merged_df.to_csv(filename,sep=',',index=False)

# Summary Statistics
stats = merged_df.describe().loc[['max','min','50%','25%','75%']][['Electorate','Votes_Cast','Valid_Votes','Remain','Leave','Rejected_Ballots']]
filename = 'uk_ref_stats_pandas.csv'
stats.to_csv(filename,sep=',',index=False)

"""
Find Area with highest and lowest electorates
"""
# Method 1: Sorting
lowest_area = merged_df.sort_values(by='Electorate').iloc[0]['Area']
highest_area = merged_df.sort_values(by='Electorate').iloc[-1]['Area']

# Method 2: idxmax() and idxmin() functions
lowest_area = merged_df.loc[merged_df['Electorate'].idxmin()]['Area']
highest_area = merged_df.loc[merged_df['Electorate'].idxmax()]['Area']

"""
Aggregates
"""
### Method 1: Group By
# Find total electorates of each region
aggregates = merged_df.groupby(by='Region').agg({'Electorate':sum})
# find % of total electorates for each region
percentage = merged_df.groupby(by = 'Region').agg({'Electorate': sum}) / merged_df['Electorate'].sum() * 100
# write to CSV
agg_merge = pd.merge(left = aggregates, right = percentage, on = 'Region')
filename = 'uk_ref_agg_pandas.csv'
agg_merge.to_csv(filename,sep=',')

### Method 2: Pivot Table
merged_df.pivot_table(index=['Region'],aggfunc={'Electorate':sum})