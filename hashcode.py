import math

def algo(file):
    (dictlib,dictbook,nbdays_for_scanning,scorebook) = in_parser(file)
    nbdays_for_scanning = min(len(dictlib),nbdays_for_scanning)
    scores = []
    for i in range (len(dictlib)):
        sum_score_book = 0
        for j in dictlib[i][3]:
            sum_score_book += dictbook[int(j)][0]
        score = sum_score_book * int(dictlib[i][2])/int(dictlib[i][1])
        scores.append((score,i))
    scores.sort(key=lambda tup: tup[0],reverse=True)
    res = []
    for i in range(nbdays_for_scanning):
        res.append((scores[i][1],dictlib[scores[i][1]][3]))
    out_parser(res,file)

def in_parser(filename):
    librarylist = dict()
    bookslist = dict()
    with open(filename, 'r') as filein:
        param = filein.readline().strip('\n')
        param = param.split(' ')
        nbbook = int(param[0])
        nblibrary = int(param[1])
        nbdays_for_scanning = int(param[2])

        scorebook = filein.readline().strip('\n')
        scorebook = scorebook.split(' ')

        for i in range(0,nblibrary):
            l = filein.readline().strip('\n')
            l = l.split(' ')
            l2 = filein.readline().strip('\n')
            l2 = l2.split(' ')

            librarylist[(i)] = l[0],l[1],l[2],set(l2)
            for j in l2:
                j = int(j)
                if j in bookslist:
                    bookslist[j][1].add(i)
                else:
                    bookslist[j] = int(scorebook[j]),set([i])
    return(librarylist,bookslist,nbdays_for_scanning,scorebook)


def out_parser(list_library,filename):
    with open("./output/"+ filename[7:-3] + 'out', 'w') as f:
        s = "{}\n".format(len(list_library))

        for index_library in range(len(list_library)):
            s += "{} {}\n".format(list_library[index_library][0],len(list_library[index_library][1]))

            for e in list_library[index_library][1]:
                s += "{} ".format(e)
            s+="\n"
        f.write("{}\n".format(s))

files = [
"./input/a_example.txt",
"./input/b_read_on.txt",
"./input/c_incunabula.txt",
"./input/d_tough_choices.txt",
"./input/e_so_many_books.txt",
"./input/f_libraries_of_the_world.txt"
]

for i in files:
    algo(i)
