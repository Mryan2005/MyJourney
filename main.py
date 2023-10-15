import os,sys
""" 
MyJourneys = dict(
    "shanghai"={
        "waitan" = {
            "time1"= {
                "thinks1":['files']
            },
            "time2"= {
                "thinks1":['files']
            },
        },
    }
)
"""
def roading():
    MyJourneyFile = open(".//date//main.mj",'w+')
    for i in MyJourney.read():
        pass
    return 0

def log(dir, province, city, sights, time, thinkings, files):
    if province == city:
        dir[province] = {}
        dir[province][sights] = {}
        dir[province][sights][time] = {}
        dir[province][sights][time][thinkings] = files

    else:
        dir[province] = {}
        dir[province][city] = {}
        dir[province][city][sights] = {}
        dir[province][city][sights][time] = {}
        dir[province][city][sights][time][thinkings] = files
    return 0