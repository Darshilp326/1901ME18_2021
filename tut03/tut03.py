import os

def output_by_subject():
    subPath = r'./output_by_subject' 
    if not os.path.exists(subPath):
        os.makedirs(subPath)
    with open('regtable_old.csv', 'r') as file:
        data = []
        for line in file:
            row = line.split(',')

            rollNo = row[0]
            registerSem = row[1]
            subNo = row[3]
            subType = row[8]

            if(rollNo == 'rollno'):
                continue

            path = 'output_by_subject/' + subNo + '.csv'

            if(subNo in data):
                with open(path, 'a') as f:
                    f.write(rollNo + ',' + registerSem + ',' + subNo + ',' + subType)
            else:
                data.append(subNo)
                with open(path, 'w') as f:
                    f.write('rollNo,' + 'registerSem,' + 'subNo,' + 'subType\n')
                    f.write(rollNo + ',' + registerSem + ',' + subNo + ',' + subType)
    return


def output_individual_roll():
    file = open('regtable_old.csv', 'r')
    lines = []
    for line in file:
        lines.append(line.strip())
    lines.sort()
    result = {}
    lastRoll = ""
    for line in lines:
        words = line.split(',')
        if words[0] == 'rollno':
            continue
        if lastRoll != words[0]:
            subjectList = []
        subjectList.append(
            {"sem": words[1], "subno": words[3], "sub_type": words[8]})
        result[words[0]] = subjectList
        lastRoll = words[0]
    rollPath = r'./output_individual_roll' 
    if not os.path.exists(rollPath):
        os.makedirs(rollPath)
    for x in result:
        file = open('output_individual_roll/%s.csv' % x, 'w')
        file.writelines(["rollNo,registerSem,subno,subType\n"])
        for b in result[x]:
            file.writelines(
                [x+','+b['sem']+","+b["subno"]+","+b['sub_type']+'\n'])
        file.close()
    return

output_individual_roll()
output_by_subject()
