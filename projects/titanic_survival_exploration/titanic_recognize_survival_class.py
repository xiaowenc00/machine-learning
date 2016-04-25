import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class rec_survival:
    
    def __init__(self,training_data_path):
        self.traning_df = pd.DataFrame().from_csv(training_data_path)


    def get_traning_data(self):
        return self.traning_df

    def get_survive_relation(self,para):
        return self.traning_df[self.traning_df['Survived']== 1][para]
    def get_label_number(self):
        #for para in self.traning_df
        for para in self.traning_df.columns:
            data = self.get_survive_relation(para)
            print(data.value_counts())
    
        
if __name__ == '__main__':
    find_survival = rec_survival(r'titanic_data.csv')
    print(find_survival.get_label_number())
        
