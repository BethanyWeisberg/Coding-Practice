# Data courtesy of Kaiser Family Foundation
# github link here when finished....

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

US_UNINSURED = 'combined.csv'

def main():
    df = pd.read_csv(US_UNINSURED)
    df[df.Location=="United States"].transpose().iloc[1:,].plot(title = "Plot of US {INSERT CORRECT NAME} over Time",
                                                            xlabel="Year", 
                                                            ylabel="Number")

    
if __name__ == '__main__':
    main()