import csv
import matplotlib.pyplot as plt

filename = 'data.csv'

with open(filename) as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)    

    avg_rate_index = header.index('int_rate')
    purpose_index = header.index('purpose')

    avg_rate_dict = {}

    for row in reader:
        avg_rate = float(row[avg_rate_index])
        purpose = row[purpose_index]

        if purpose not in avg_rate_dict.keys():
            avg_rate_dict[purpose] = [avg_rate, 1]
        else:
            avg_rate_dict[purpose][0] += avg_rate
            avg_rate_dict[purpose][1] += 1

    plt.bar(list(range(len(avg_rate_dict))),
            list(map(lambda pair: pair[0]/pair[1],
                avg_rate_dict.values())))
    plt.xticks(list(range(len(avg_rate_dict))),
            list(avg_rate_dict.keys()), rotation=90)
    plt.ylabel('mean(int_rate)')
    plt.savefig('plot.png', bbox_inches="tight") 
