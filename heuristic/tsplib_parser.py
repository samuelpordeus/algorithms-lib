# Lendo o arquivo de entrada
def readData(tsp_file):
    cities_list = []
    file = open(tsp_file)
    cities_list = [line[:-1].split() for line in file][6:-1]
    file.close()
    for item in cities_list:
        del item[0]
        item[0] = int(float(item[0]))
        item[1] = int(float(item[1]))
    return cities_list