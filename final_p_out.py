# @file: final_p_out.py implements outputs
# @author: Huy
# @date: 12.11.18
# @version: Initial HN

import final_p_maps

def display_menu() -> str:
    menu = """
    FINAL PROJECT: MAPQUEST

    Directions: enter input in the following order (separate lines):

    # of destinations
    Address for each destination
    # of outputs
    STEPS, TOTALDISTANCE, TOTALTIME, LATLONG, ELEVATION
    """
    return menu

# get the number of destinations and the name of each destination, return destinations as a list
def input_destinations() -> list:
    dest_num = int(input())
    destinations = []
    for num in range(dest_num):
        destinations.append(input().replace(" ", "+"))
    return destinations

# take what the user wants to display, return list of steps
def get_input_steps() -> list:
    steps = int(input())
    directives = []
    for num in range(steps):
        directives.append(input())
    return directives

# takes the list of destinations and returns a string of directions
def get_dir(destinations:list) -> str:
    dir_str = ""
    for pos in range(len(destinations) - 1):
        start_end = destinations[pos],destinations[pos + 1]
        dir_str += directions().generate(start_end)
    return dir_str

# takes the list of destinations and returns the total time
def get_time(destinations:list) -> float:
    total_time = 0
    for pos in range(len(destinations) - 1):
        start_end = destinations[pos], destinations[pos + 1]
        total_time += float(time().generate(start_end))
    return total_time

# takes the list of destinations, and returns a string for total distance
def get_dist(destinations:list) -> str:
    total_dist = 0
    for pos in range(len(destinations) - 1):
        start_end = destinations[pos], destinations[pos + 1]
        total_dist += float(distance().generate(start_end))
    return total_dist

# takes list of destinations, return string of elevations
def get_elv(destinations:list) -> str:
    elv_str = ""
    for pos in range(len(destinations)):
        loc = destinations[pos]
        start_end=loc,loc
        elv_str += elevation().generate(start_end)
    return elv_str

# takes list of destinations, return string of latitudes and longitudes
def get_latlong(destinations:list) -> str:
    latlong_str = ""
    for pos in range(len(destinations)):
        loc = destinations[pos]
        start_end = loc, loc
        latlong_str += latlong().generate(start_end)
    return latlong_str

# execute directives
def execute_steps(directives: list, dir_str: str, latlong_str: str,
                  total_time: str, total_dist: str, elv_str: str) -> None:
    for step in directives:
        print()
        if step == "LATLONG":
            print("LATLONGS")
            print(latlong_str)

        elif step == "STEPS":
            print("DIRECTIONS")
            print(dir_str)

        elif step == "TOTALTIME":
            print("TOTAL TIME: {:.0f} minutes".format(total_time))

        elif step == "TOTALDISTANCE":
            print("TOTAL DISTANCE: {:.0f} miles".format(total_dist))

        elif step == "ELEVATION":
            print("ELEVATIONS")
            print(elv_str)

# makes directions string
class directions:
    def generate(self, start_end:tuple)->str:
        routedict = final_p_maps.handle_api_dir(start_end)
        dir_str = ""
        for item in routedict["route"]["legs"][0]["maneuvers"]:
             dir_str += item["narrative"] + "\n"
        return dir_str

# makes latitude and longitude string
class latlong:
    def generate(self, start_end:tuple) -> str:
        routedict = final_p_maps.handle_api_dir(start_end)
        latlong_dict = routedict["route"]["legs"][0]["maneuvers"][0]["startPoint"]
        l_string = ""
        if latlong_dict["lat"] >= 0:
            str_temp ="{:.2f}".format(latlong_dict["lat"])
            l_string += str_temp + "N "
        else:
            str_temp = "{:.2f}".format(latlong_dict["lat"])
            l_string += str_temp[1:] + "S "
        if latlong_dict["lng"] >= 0:
            str_temp = "{:.2f}".format(latlong_dict["lng"])
            l_string += str_temp + "E"
        else:
            str_temp = "{:.2f}".format(latlong_dict["lng"])
            l_string += str_temp[1:] + "W"
        return l_string + "\n"

# makes string of total time
class time:
    def generate(self, start_end:tuple) -> str:
        routedict = final_p_maps.handle_api_dir(start_end)
        return str(routedict["route"]["time"] / 60)

# makes string of total distance
class distance:
    def generate(self, start_end:tuple) -> str:
        routedict = final_p_maps.handle_api_dir(start_end)
        return str(routedict["route"]["distance"])

# makes string of elevation
class elevation:
    def generate(self, start_end:tuple) -> str:
        routedict = final_p_maps.handle_api_dir(start_end)
        latlong_dict = routedict["route"]["legs"][0]["maneuvers"][0]["startPoint"]
        routedict_elv = final_p_maps.handle_api_elv(latlong_dict)
        return str("{:.0f}".format(routedict_elv["elevationProfile"][0]["height"])) + "\n"