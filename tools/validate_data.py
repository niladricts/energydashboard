import csv
import re
from flask import Flask, render_template, request, redirect, session


def checkCSV():
    file = session.get('uploaded_data_file_path', None)
    validate = []

    with open(file, 'r', encoding="UTF-8") as csvfile:
        read_file = csv.reader(csvfile)
        line = ""
        for row in read_file:
            column = row[0]
            value = row[1]
            print(column)
            if column == 'date' and (re.match(r'^\d{2}-\d{2}-\d{4}\s\d{2}:\d{2}:\d{2}$', value)):
                line = value
                validate.append("yes")
            elif column == 'Appliances' and (re.match(r'^\d{2,4}$', value)):
                line = value
                validate.append("yes")
            elif column == 'lights' and (re.match(r'^\d{2,4}$', value)):
                line = value
                validate.append("yes")
            elif column == 'T1' and (re.match(r'^\d{1,9}.\d{1,9}$', value)):
                line = value
                validate.append("yes")
            elif column == 'RH_1' and (re.match(r'^\d{1,9}.\d{1,9}$', value)):
                line = value
                validate.append("yes")
            elif column == 'T2' and (re.match(r'^\d{1,9}.\d{1,9}$', value)):
                line = value
                validate.append("yes")
            elif column == 'RH_2' and (re.match(r'^\d{1,9}.\d{1,9}$', value)):
                line = value
                validate.append("yes")
            elif column == 'T3' and (re.match(r'^\d{1,9}.\d{1,9}$', value)):
                line = value
                validate.append("yes")
            elif column == 'RH_3' and (re.match(r'^\d{1,9}.\d{1,9}$', value)):
                line = value
                validate.append("yes")
            elif column == 'T4' and (re.match(r'^\d{1,9}.\d{1,9}$', value)):
                line = value
                validate.append("yes")
            elif column == 'RH_4' and (re.match(r'^\d{1,9}.\d{1,9}$', value)):
                line = value
                validate.append("yes")
            elif column == 'T5' and (re.match(r'^\d{1,9}.\d{1,9}$', value)):
                line = value
                validate.append("yes")
            elif column == 'RH_5' and (re.match(r'^\d{1,9}.\d{1,9}$', value)):
                line = value
                validate.append("yes")
            elif column == 'T6' and (re.match(r'^\d{1,9}.\d{1,9}$', value)):
                line = value
                validate.append("yes")
            elif column == 'RH_6' and (re.match(r'^\d{1,9}.\d{1,9}$', value)):
                line = value
                validate.append("yes")
            elif column == 'T7' and (re.match(r'^\d{1,9}.\d{1,9}$', value)):
                line = value
                validate.append("yes")
            elif column == 'RH_7' and (re.match(r'^\d{1,9}.\d{1,9}$', value)):
                line = value
                validate.append("yes")
            elif column == 'T8' and (re.match(r'^\d{1,9}.\d{1,9}$', value)):
                line = value
                validate.append("yes")
            elif column == 'RH_8' and (re.match(r'^\d{1,9}.\d{1,9}$', value)):
                line = value
                validate.append("yes")
            elif column == 'T9' and (re.match(r'^\d{1,9}.\d{1,9}$', value)):
                line = value
                validate.append("yes")
            elif column == 'RH_9' and (re.match(r'^\d{1,9}.\d{1,9}$', value)):
                line = value
                validate.append("yes")
            elif column == 'To' and (re.match(r'^\d{1,9}.\d{1,9}$', value)):
                line = value
                validate.append("yes")
            elif column == 'Pressure' and (re.match(r'^\d{1,9}.\d{1,9}$', value)):
                line = value
                validate.append("yes")
            elif column == 'RH_out' and (re.match(r'^\d{1,9}.\d{1,9}$', value)):
                line = value
                validate.append("yes")
            elif column == 'Wind speed' and (re.match(r'^\d{1,9}.\d{1,9}$', value)):
                line = value
                validate.append("yes")
            elif column == 'Visibility' and (re.match(r'^\d{1,9}.\d{1,9}$', value)):
                line = value
                validate.append("yes")
            elif column == 'Tdewpoint' and (re.match(r'^\d{1,9}.\d{1,9}$', value)):
                line = value
                validate.append("yes")
            elif column == 'rv1' and (re.match(r'^\d{1,9}.\d{1,9}$', value)):
                line = value
                validate.append("yes")
            elif column == 'rv2' and (re.match(r'^\d{1,9}.\d{1,9}$', value)):
                line = value
                validate.append("yes")
            else:
                validate.append("no")

    error_values = [validate.index(i) for i in validate if i == "no"]
    if len(error_values) == 0:
        return "Yes"
    else:
        return f"Error at column positions {error_values}"
