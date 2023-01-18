import requests
import json

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
