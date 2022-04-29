import csv
import pandas as pd
from flask import Flask, render_template, request, redirect, session
from csvvalidator import *


def checkCSV():
    file = session.get('uploaded_data_file_path', None)
    headers = pd.read_csv(file, index_col=0, nrows=0).columns.tolist()
    validator = CSVValidator(headers)
    data = pd.read_csv(file)
    issues = CSVValidator.validate(validator, data, expect_header_row=True, ignore_lines=0, limit=0)
    return issues
