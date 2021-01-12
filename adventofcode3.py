geo=("..##.......",
"#...#...#..",
".#....#..#.",
"..#.#...#.#",
".#...##..#.",
"..#.##.....",
".#.#.#....#",
".#........#",
"#.##...#...",
"#...##....#",
".#..#...#.#")
slope=3
# geo=open("input (2).txt","r").read().split("\n")[:-1]
try:
    geo=open("C:\\Users\\mika1\\OneDrive\\Documents\\AdventOfCode\\input3.txt","r").readlines()
except:
    print("File not found")

def trees_encountered(geo,slope):
    down=0
    trees=0
    for i in geo:
        j=(down*slope)%len(i)
        if(i[j]=="#"):
            trees+=1
        down+=1
    return trees

print("Traversing the map using this slope would cause you to encounter",trees_encountered(geo,slope),"trees.")

slopes=[
    [1,1],
    [3,1],
    [5,1],
    [7,1],
    [1,2]]
def trees_encountered2(geo,slope):
    down=0
    right=0
    trees=0
    while down < len(geo)-1:
        if(geo[down][right]=="#"):
            trees+=1
        down+=slope[1]
        right+=slope[0]
        right=right%len(geo[down])
    return trees

mult=1
for slope in slopes:
    mult*=trees_encountered2(geo,slope)

print("If you multiply together the number of trees encountered on each of the listed slopes, you get",mult)
