MyJourneys = {"shanghai":{"fuxinggongyuan":{"2023.11.10":{"i like there":{}}}}}
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
    print(dir)
    return 0
files = ["./453.png"]
log(MyJourneys,"shanghai","shanghai","fuxinggongyuan","2023.11.10","i like there",files)
files = ["./888.png"]
log(MyJourneys,"guangxi","wuzhou","ming liangchao","2023.11.20","i like there",files)