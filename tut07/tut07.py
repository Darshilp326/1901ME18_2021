import csv
import openpyxl
import pandas as pd
import os
from pathlib import Path

studRollToSub = {}
subToLTP = {}
rollToSem = {}
subToSem = {}
feedbackRemaining = []

feedbackFile = pd.read_csv("course_feedback_submitted_by_students.csv")
studInfo = pd.read_csv("studentinfo.csv")
courseRegisteredFile = pd.read_csv("course_registered_by_all_students.csv")       

if os.path.exists('course_feedback_remaining.xlsx'):
    os.remove('course_feedback_remaining.xlsx')


# Read course registered file and create a dict with key as roll and value as list of all subjects
def readCourse():
    file = open('course_registered_by_all_students.csv')
    csvreader = csv.reader(file)
    for row in csvreader:
        if row[0] == 'rollno':
            continue
        else:
            rollToSem[row[0]] = row[1]
            studRollToSub.setdefault(row[0], []).append(row[3])

# Read course master file and store each subject's ltp
def readSubjects():
    course_file = open("course_master_dont_open_in_excel.csv")
    csvreader = csv.reader(course_file)
    for row in csvreader:
        if row[0]=='subno':
            continue
        else:
            subToLTP[row[0]] = row[2]


def checkIfExistInFeedback(roll, subno, feedback_type):
    # Checking if a row exists in feedback submitted file with given values
    if not ((feedbackFile["stud_roll"] == roll) & (feedbackFile['course_code'] == subno) & (feedbackFile['feedback_type']==feedback_type)).any():
        # Finding student info from studinfo.csv
        row = studInfo.loc[studInfo['Roll No'] == roll]
        x = courseRegisteredFile[(courseRegisteredFile["rollno"] == roll) & (courseRegisteredFile["subno"] == subno)]                                                                                                                                                                        
        schedule_sem = x["schedule_sem"].values[0]
        if row.values.tolist():
            studInfoList = row.values.tolist()[0]
            studentDetailList = [studInfoList[1], rollToSem[roll], schedule_sem,
                        subno, studInfoList[0], studInfoList[8], studInfoList[9], studInfoList[10]]
            feedbackRemaining.append(studentDetailList)
        else:
            # As studinfo file had no information,adding 'Notfound' to some fields
            studentDetailList = [roll, rollToSem[roll], schedule_sem,
                        subno, "Notfound", "Notfound", "Notfound", "Notfound"]
            feedbackRemaining.append(studentDetailList)


def feedback_not_submitted():

    ltp_mapping_feedback_type = {1: 'lecture', 2: 'tutorial', 3: 'practical'}
    output_file_name = "course_feedback_remaining.xlsx"
    readCourse()
    readSubjects()

    # Iterate over roll to subject dictionary and find if feedback was filled for ltp.
    for roll, list in studRollToSub.items():
        for sub in list:
            ltpList = subToLTP[sub].split('-')
            ltpType = 1
            for i in ltpList:
                if int(i) > 0:
                    # Checking in feedback submitted file, if any row is present with same roll,subject and ltp mapping. 
                    checkIfExistInFeedback(roll, sub, ltpType)
                ltpType += 1

    # Output file may contain some duplicates with same roll no and subject code, as the student might have not filled more than one ltp feedbacks.
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.append(['rollno','register_sem','schedule_sem','subno','name','email','aemail','contact'])
    for list in feedbackRemaining:
        sheet.append(list)
    wb.save(output_file_name)



feedback_not_submitted()