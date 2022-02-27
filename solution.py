
from contributor import Contributor
from project import Project
files = [
         'a_an_example.in.txt',
         'b_better_start_small.in.txt',
         'c_collaboration.in.txt',
         'd_dense_schedule.in.txt',
         'e_exceptional_skills.in.txt', 
         'f_find_great_mentors.in.txt'  
        ]

for filename in files:
    # indent back from line 14 to run all the files
    # pass

# filename = 'a_an_example.in.txt'
    f = open('files/' + filename, 'r')

    C_COUNT, P_COUNT = list(map(int, f.readline().split(' ')))
    conts = []
    projects = []
    languages = {}
    DAYS = 0

    for _ in range(C_COUNT):
        name, l = f.readline().split(' ')
        name = name.strip()
        langs = {}
        
        c = Contributor(langs, name)
        for _ in range(int(l)):
            lang, level = f.readline().split(' ')
            lang = lang.strip()
            langs[lang] = int(level)

            if lang in languages:
                languages[lang].add(c)
            else:
                languages[lang] = set([c])
        c.langs = langs
        conts.append(c)

    print(conts[-1])

    for _ in range(P_COUNT):
        # print(f.readline)
        name, days, score, bbefore, roles = f.readline().split(' ')
        name = name.strip()
        langs = {}
        rs = 0
        DAYS += int(days)
        for _ in range(int(roles)):
            lang, level = f.readline().split(' ')
            lang = lang.strip()
            rs += int(level)
            if lang in langs:
                langs[lang].append(int(level))
            else:
                langs[lang] = [int(level)]
        projects.append(Project(langs, name, int(days), int(score), int(bbefore), int(roles), rs))

    print(conts, projects)

    print(P_COUNT, C_COUNT)

    # sc = x.score / (x.days-x.bbefore)
    projects.sort(key=lambda x: x.score / x.days, reverse=True) 
    # projects.sort(key=lambda x: x.roles)
    # projects.sort(key=lambda x: x.days-x.bbefore)
    # projects.sort(key=lambda x: x.score)
    # print(projects[0])
    res = ''

    def projectDoable(p, conts, languages):
        doable = 0
        for lang in p.langs:
            for level in p.langs[lang]:
                if lang in languages:
                    for cont in languages[lang]:
                        if cont.langs[lang] >= level:
                            doable += 1
                            break
                        
                else:
                    return False
        return doable == len(p.langs)

    def hasAMentor(lang, contributors, level):
        for c in contributors:
            if lang in c.langs and c.langs[lang] >= level:
                return True
        return False

    def doProject(p, conts, languages):
        contributors = []
        contss = []
        for lang in p.langs:
            for level in p.langs[lang]:
                done = False
                if lang in languages:
                    for cont in sorted(languages[lang].copy(), key=lambda x: x.langs[lang]):
                        if cont.langs[lang] >= level:
                            if cont.name not in contributors:
                                contributors.append(cont.name)
                                contss.append(cont)
                                # languages[lang].remove(cont)
                                # if cont.langs[lang] == level:
                                #     cont.langs[lang] += 1
                                done = True
                                break
                        elif cont.langs[lang] == level - 1 and hasAMentor(lang, contss, level):
                            if cont.name not in contributors:
                                contributors.append(cont.name)
                                # contss.append(cont)
                                # languages[lang].remove(cont)
                                # if cont.langs[lang] == level:
                                #     cont.langs[lang] += 1
                                done = True
                                break

                if not done:
                    return [] 
                # if contss[-1].langs[lang] == level:
                #     contss[-1].langs[lang] +=1
                
                        
        return contributors


    i = 0
    pcount = 0
    while i < len(projects):
        project = projects[i]
        if projectDoable(project, conts, languages):
            p = projects.pop(i)
            print(p)
            
            contributors = doProject(p, conts, languages)
            if len(contributors):
                pcount += 1
                res += p.name + '\n'
                res += ' '.join(contributors) + '\n'
                print(contributors)
            continue
        i += 1
                

    print(res)

    output = open(filename + '.output', 'w')
    output.write(str(pcount) + '\n' + str(res))
    output.close()


