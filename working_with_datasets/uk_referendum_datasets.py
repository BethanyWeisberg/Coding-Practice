import requests
import csv
import itertools

# reading data into python
uk_demo_src = r"https://raw.githubusercontent.com/viveknest/statascratch-solutions/main/UK%20Referendum%20Data/uk_demo.json"
f = requests.get(uk_demo_src)
uk_demo = f.json()
uk_demo[:5]

uk_results_src = r"https://raw.githubusercontent.com/viveknest/statascratch-solutions/main/UK%20Referendum%20Data/uk_results.json"
f = requests.get(uk_results_src)
uk_results = f.json()
uk_results[:5]

uk_rejected_src = r"https://github.com/viveknest/statascratch-solutions/raw/main/UK%20Referendum%20Data/uk_rejected_ballots.json"
f = requests.get(uk_rejected_src)
uk_rejected = f.json()
uk_rejected[:5]

# Convert lists into a dictionary of dictionaries
def dict_convert(data, key = 'Area_Code'):
    out_dict = {}
    for row in data:
        out_dict.update({
            row[key]: row
        })
    return out_dict

uk_demo_dict = dict_convert(uk_demo)
uk_results_dict = dict_convert(uk_results)
uk_rejected_dict = dict_convert(uk_rejected)

# merge the dictionaries using the key
merged_dict = {}
for key in uk_demo_dict.keys():
    merged_dict.update({
        key: {**uk_demo_dict[key], **uk_results_dict[key], **uk_rejected_dict[key]}
    })
local_filename = "uk_referendum_merged.csv"

keys = list(merged_dict.keys())

# Write nested dictionary values to csv file
with open(local_filename, 'w', newline='') as fp:
    csv_w = csv.DictWriter(fp,fieldnames=list(merged_dict[keys[0]].keys()))
    csv_w.writeheader()
    for i in merged_dict.values():
        csv_w.writerow(i)
fp.close()

"""
Summary Statistics
Find: max, min, median, 25th % and 75%
For: Electorate, votes cast, valid votes, 
remain votes, leave votes, rejected votes
"""

filename = "uk_referendum_summ_stats.csv"
def summ_stats(source_data, variable):
    # extract data points into a sorted list
    out_list = []
    for k,v in source_data.items():
        out_list.append(v[variable])
    out_list.sort()
    # stat values
    max_value = max(out_list)
    min_value = min(out_list)
    num_items = len(out_list)

    # Median value
    if num_items % 2 == 0:
        mid_value1 = num_items // 2 - 1
        mid_value2 = num_items // 2
        median_value = (out_list[mid_value1] + out_list[mid_value2]) / 2
    else:
        mid_value = (num_items + 1) // 2 - 1
        median_value = out_list[mid_value]

    # quartiles, using the nearest rank method
    q1_rank = (num_items * 0.25).__ceil__() - 1
    q3_rank = (num_items * 0.75).__ceil__() - 1

    q1 = out_list[q1_rank]
    q3 = out_list[q3_rank]

    out_dict = {
        'variable': variable,
        'max': max_value,
        'min': min_value,
        'median': median_value,
        'q1': q1,
        'q3': q3
    }
    return out_dict

fields = ['variable','max','min','median','q1','q3']
variable_list = ['Electorate','Votes_Cast','Valid_Votes','Remain','Leave','Rejected_Ballots']
with open(filename, 'w', newline='') as fp:
    csv_w = csv.DictWriter(fp,fieldnames=fields)
    csv_w.writeheader()
    for v in variable_list:
        csv_w.writerow(summ_stats(merged_dict,v))
fp.close()

"""
Find the Area with the highest and
lowest electorates using object properties
for sorting
"""
# Unnest the merged dictionary:
merged_list = [v for k,v in merged_dict.items()]

# Use a lamda function to sort dictionary based on Electorate values
# and return the
lowest_electorate_area = sorted(merged_list, key = lambda x: x['Electorate'])[0]['Area']
highest_electorate_area = sorted(merged_list, key = lambda x: x['Electorate'],reverse=True)[0]['Area']
print(f'The area with the lowest electorates is {lowest_electorate_area}.\nThe area with the lowest electorates is {highest_electorate_area}.')

"""
Aggregation
Find the electorate totals for each region
and the % of electorates in each
"""

# Get all the regions by using a Python set
regions = set([area['Region'] for area in merged_list])

# add electorate sum total for each region
region_dict = {}

total_region_sum = sum(area['Electorate'] for area in merged_list)
region_aggregations = []
for region in regions:
    region_sum = sum([area['Electorate'] for area in merged_list if area['Region'] ==  region])
    region_dict= {
        "region": region,
        "electorate_sum": region_sum,
        "electorate_percentage": "{:.2%}".format(region_sum/total_region_sum)
    }
    region_aggregations.append(region_dict)

region_aggregations.sort(key = lambda x: x['electorate_sum'], reverse=True)

filename = 'uk_referendum_aggregations.csv'
fields = ['region','electorate_sum','electorate_percentage']
with open(filename, 'w', newline='') as fp:
    csv_w = csv.DictWriter(fp,fieldnames=fields)
    csv_w.writeheader()
    for item in region_aggregations:
        csv_w.writerow(item)
fp.close()