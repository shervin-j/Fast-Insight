from math import sqrt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class statistics():
    def mean(self):
        #   Mean
        return sum(self.df['Cost']) / sum(self.df['Quantity'])


    def mode(self):
        #   Mode
        mode = {}
        counter = 0
        repeat_number = 0
        mode_counter = 1
        costs = list(self.df['Cost'])
        costs2 = list(set(costs))
        for cost in costs2:
            for m in costs:
                if m == cost:
                    counter += 1
            if counter > repeat_number:
                mode["mode1"] = cost
                repeat_number = counter
            elif counter == repeat_number:
                mode_counter += 1
                mode[f"mode{mode_counter}"] = cost
                
            counter = 0
        return mode
        

    def median(self):
        #   Median
        costs_list = list(self.df['Cost'])
        costs_list.sort()
        #print(costs_list)
        length = len(costs_list)
        if length%2 == 0:
            return (costs_list[int(length/2)] + costs_list[int(length/2 -1)]) / 2
        else:
            return costs_list[int(length/2)]


    def variance(self):
        return sum((self.df['Cost'] - self.mean()) ** 2) / sum(self.df['Quantity'])


    def standard_deviation(self):
        return sqrt(self.variance())


    def cv(self):   #Coefficient of variation
        return self.standard_deviation() / self.mean()


    def ReadCSV(self, file_address="C:/Users/Sh/Desktop/Fast Insight/Shopping List.csv"):
        self.df = pd.read_csv(file_address)
        self.df['Cost'] = self.df['Cost (each)'] * self.df['Quantity']

    
    def bar_plot(self):
        plt.title('Cost\'s bar plot')
        plt.xlabel('Cost (each)')
        plt.ylabel('Quantity of each Cost')
        plt.bar(self.df['Cost (each)'], self.df['Quantity'], 0.25, color='#1976D2')
        plt.show()


    def pie_plot(self):
        plt.title('Cost\'s pie plot')
        plt.pie(self.df['Cost'], labels = self.df['Item'], autopct = '%.3f')
        plt.show()


    def hist_plot(self):
        plt.title('Cost\'s histogram plot')
        plt.hist(self.df['Cost'], color='#4CAF50')
        plt.show()

    def scatter_plot(self):
        plt.title('Cost\'s scatter plot')
        plt.scatter(self.df['Cost (each)'], self.df['Quantity'], c='#d32f2f')
        plt.xlabel('Cost (each)')
        plt.ylabel('Quantity of each Cost')
        plt.show()

####################    Usefull ########################
#   Claclute Time
#import timeit
# start = timeit.default_timer()

# n = np.array(df['Cost'])
# print(np.sum(n))

# stop = timeit.default_timer()
# print('Time1: ', stop - start)  

###########################
# Mode
# costs1 = list(df['Cost'])
#     costs2 = list(set(costs1))
#     numbers = {}
#     for cost in costs2:
#         numbers[cost] = costs1.count(cost)
    
#     l1 = list(numbers.values())
#     l2 = list(numbers.keys())
#     return l2[l1.index(max(l1))]
#     #max(numbers, key=numbers.get)
###################################