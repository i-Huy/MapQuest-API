# MapQuest-API

A basic locations/directions/information program using the MapQuest API to retrieve wanted information from user input. Built with Python.

Program will take input in the following format.

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
![mapquest-api](https://i.imgur.com/M39e75v.png)
