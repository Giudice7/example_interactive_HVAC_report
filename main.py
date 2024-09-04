import pandas as pd
from src import report

data = pd.read_csv("data/AHU_annual.csv")
report.run_report(data, "SDAHU")
