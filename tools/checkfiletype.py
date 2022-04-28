from flask import Flask, render_template, request, redirect, session
import os
import pandas as pd

ALLOWED_EXTENSION = {"csv"}


def isCSV():
    file = session.get('uploaded_data_file_path', None)
    print(file)
    return '.' in file and file.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSION
