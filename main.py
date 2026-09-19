stations = {

    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C", "E"],
    "E": ["D"],
}

visited = set()

start_station = input("Please enter your station: ").upper()

if start_station in stations:
    visited.add(start_station)
    print("Connected Stations: ")
    for station in stations[start_station]:
        if station not in visited:
            print(station)
            visited.add(station)
    
    print(visited)
else: 
    print('Please choose a correct option: ')


