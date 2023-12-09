data = input("file: ")

def get_data(file = "test_data.txt") -> list:
    with open(file) as f:
        return f.readlines()

def get_nums(data: list) -> list:
    rec: list = []
    log: list = [[],[],[]]

    for k,v in enumerate(data):
        for i,j in enumerate(v):
            if j.isnumeric():
                rec.append(i)
                continue
            elif rec:
                log[1].append([k,rec])
                rec = []
            if j== '.' or j == '\n':
                continue
            log[0].append([k,i])
    
    nums: list = []

    for s in log[0]:
        y_neighbors: list = [s[0]-1,s[0],s[0]+1]
        x_neighbors: list = [s[1]-1,s[1],s[1]+1]
        
        for n in log[1]:
            n_y = n[0] in y_neighbors
            start = n[1][0] in x_neighbors
            end = n[1][-1] in x_neighbors
            
            if n_y:
                if (start or end):
                    nums.append(int(f"{data[n[0]][n[1][0]:n[1][-1]+1]}"))

    return nums

def get_ratios(data: list) -> list:
    rec: list = []
    log: list = [[],[],[]]

    for k,v in enumerate(data):
        for i,j in enumerate(v):
            if j.isnumeric():
                rec.append(i)
                continue
            elif rec:
                log[1].append([k,rec])
                rec = []
            if j != '*':
                continue
            log[0].append([k,i])
    
    gears: list = []

    for s in log[0]:
        tmp: list = []
        y_neighbors: list = [s[0]-1,s[0],s[0]+1]
        x_neighbors: list = [s[1]-1,s[1],s[1]+1]
        
        for n in log[1]:
            n_y = n[0] in y_neighbors
            start = n[1][0] in x_neighbors
            end = n[1][-1] in x_neighbors
            
            if n_y:
                if (start or end):
                    tmp.append(int(f"{data[n[0]][n[1][0]:n[1][-1]+1]}"))
        if len(tmp) == 2:
            gears.append(tmp[0] * tmp[1])

    return gears

if data:
    print(sum(get_ratios(get_data(data))))
else:
    print(sum(get_ratios(get_data())))
