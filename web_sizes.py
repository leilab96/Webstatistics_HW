import pickle

with open('./web_size.pickle', 'rb') as handle:
    sites = pickle.load(handle)

with open('./web_size_new.pickle', 'rb') as handle:
    sites_new = pickle.load(handle)


#First excercise
#calculate the total size of all websites and the average site size
sum = 0

for site in sites_new:
    sum += site['size']

total_size_gb = round(sum / 1024, 2)
average_size_mb = round(sum / len(sites_new)/1024, 2)

print(f"The total size is: {total_size_gb} Gb")
print(f"The average site site {average_size_mb} Mb.") 

#second excercise
#If website sizes differ in site and site new it writes out the domain and the difference in percentage
for i, site in enumerate(sites_new):

    if site['size'] != sites[i]['size']:
        diff = site['size'] - sites[i]['size']
        change_ratio = round(diff / (sites[i]['size'] / 100), 2)
        print(f"{site['domain']} changed by: {'+' if diff > 0 else '-'}{abs(change_ratio)} %")
        
        
#third excercise
#Count the number of empty sites
empty_sites = 0

for site in sites_new:
    if site['size'] == 0:
        empty_sites += 1

print(f"There are {empty_sites} empty sites.")

#fourth excercise
for site in sites_new:
    if site['size'] == 0:
        continue
    if site['size'] >= 1024: 
        size_gb = round(site['size'] / 1024, 2)
        print(f"{site['domain']}: {size_gb} Gb")
    else:
        print(f"{site['domain']}: {site['size']} Mb")
