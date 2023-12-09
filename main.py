def get_data(file = "test_data.txt") -> list:
    with open(file) as f:
        return f.readlines()

data = get_data(input("file: "))

def get_nums(data: list) -> list:
    rec: list = []
    log: list = [[],[]]

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
            if n[0] in y_neighbors:
                if n[1][0] in x_neighbors or n[1][-1] in x_neighbors:
                    nums.append(int(f"{data[n[0]][n[1][0]:n[1][-1]+1]}"))
    
    return nums

print(sum(get_nums(data)))
