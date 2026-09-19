stations = {

    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C", "E"],
    "E": ["D"],
}


start_station = input("Please enter your station: ").upper()

if start_station in stations:
    print(stations.get(start_station))
else: 
    print('Please choose a correct option: ')

