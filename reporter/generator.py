from reporter import Header
import numpy
import matplotlib.pyplot as plt
import pandas as pd
import datetime

class Generator:
    def __init__(self, json_path, xlsx_path, md_path):
        self.json_path = json_path
        self.xlsx_path = xlsx_path
        self.md_path = md_path
        
    def create_graph(self):
        graph(self.xlsx_path)
    
    def create_markdown(self):
        create_header(self.json_path, self.md_path)
