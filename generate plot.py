import matplotlib.pyplot as plt



# Sample data
data = {
    "Year": ["2009-10", "2010-11", "2011-12", "2012-13", "2013-14", "2014-15", "2015-16", "2016-17", "2017-18", "2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24"],
    "Energy Requirement (MU)": [830594, 861591, 937199, 995557, 1002257, 1068923, 1114408, 1142929, 1213326, 1274595, 1291010, 1275534, 1379812, 1511847, 266951],
    "Availability (MU)": [746644, 788355, 857886, 908652, 959829, 1030785, 1090850, 1135334, 1204697, 1267526, 1284444, 1270663, 1374024, 1504264, 266360],
    "Surplus/Deficit (MU)": [-83950, -73236, -79313, -86905, -42428, -38138, -23558, -7595, -8629, -7070, -6566, -4871, -5787, -7583, -591],
}

years = ["2009-10", "2010-11", "2011-12", "2012-13", "2013-14", "2014-15", "2015-16", "2016-17", "2017-18", "2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24*"]
total_generation = [808.498, 850.387, 928.113, 969.506, 1020.200, 1110.392, 1173.603, 1241.689, 1308.146, 1376.095, 1389.102, 1381.855, 1491.859, 1624.158, 286.176]
percent_growth = [7.56, 5.59, 9.14, 4.46, 5.23, 8.84, 5.69, 5.80, 5.35, 5.19, 0.95, -0.52, 7.96, 8.87, -0.72]

def generate_plot1():
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(data["Year"], data["Energy Requirement (MU)"], label='Energy Requirement (MU)', marker='o')
    plt.plot(data["Year"], data["Availability (MU)"], label='Availability (MU)', marker='s')
    plt.plot(data["Year"], data["Surplus/Deficit (MU)"], label='Surplus/Deficit (MU)', marker='^')
    plt.title('Energy Consumption in India (2009-10 to 2023-24)')
    plt.xlabel('Year')
    plt.ylabel('Energy (MU)')
    plt.legend()
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels by 45 degrees
    plt.show()


def generate_plot2():
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(years, total_generation, label='Total Generation (BU)', marker='o')
    plt.plot(years, percent_growth, label='% of Growth', marker='s')
    plt.title('Total Generation in India (2009-10 to 2023-24)')
    plt.xlabel('Year')
    plt.ylabel('Total Generation (BU) / % of Growth')
    plt.legend()
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels by 45 degrees
    plt.show()


generate_plot1()
generate_plot2()