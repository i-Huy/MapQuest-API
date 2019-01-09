# @file: final_p_main.py is a module that reads input and generate output
# @author: Huy
# @date: 12.11.18
# @version: Initial HN

"""Your program will take input in the following format. It should not prompt the user in any
way; it should simply read whatever input is typed into the console, and you should
assume that your user knows the precise input format.

• An integer whose value is at least 2, alone on a line, that specifies how many
locations the trip will consist of.

• If there are n locations, the next n lines of input will each describe one location. Each
location can be a city such as Costa Mesa, CA, an address such as 2701 Fairview
Rd, Costa Mesa, CA, or anything that the Open MapQuest API will accept as a
location. (The details of what is acceptable as a location is described here).

• A positive integer (i.e., whose value is at least 1), alone on a line, that specifies how
many outputs will need to be generated.

• If there are m outputs, the next m lines of input will each describe one output. Each
output can be one of the following:
    – STEPS for step-by-step directions, meaning a brief description of each maneuver
    (e.g., a turn, entering or exiting a freeway, etc.) you would have to make to
    drive from one location to another
    – TOTALDISTANCE for the total distance traveled if completing the entire trip
    – TOTALTIME for the total estimated time to complete the entire trip
    – LATLONG for the latitude and longitude of each of the locations specified in the
    input
    – ELEVATION for the elevation, in feet, of each of the locations specified in the
    input
"""

import final_p_maps # module that interacts with MapQuest API
import final_p_out # module that implements output

# main function to run the program
def main():
    print(final_p_out.display_menu())

    try:
        destinations = final_p_out.input_destinations()
        directives = final_p_out.get_input_steps()

        dir_str = final_p_out.get_dir(destinations)
        latlong_str = final_p_out.get_latlong(destinations)
        total_time = final_p_out.get_time(destinations)
        total_dist = final_p_out.get_dist(destinations)
        elv_str = final_p_out.get_elv(destinations)

        final_p_out.execute_steps(directives, dir_str,latlong_str,total_time, total_dist,elv_str)

        print("Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors")

    except final_p_maps.RouteNotFoundError:
        print()
        print("ERROR: Route not found")

    except:
        print()
        print("ERROR: Unknown Input. Try again.")

if __name__ == "__main__":
    main()