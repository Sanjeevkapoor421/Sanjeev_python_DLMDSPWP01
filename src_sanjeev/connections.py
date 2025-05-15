from pydoc import locate
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

class Get_connections:

    def __init__(self,path,title):
        self.dataFrame = []
        try:
            self.data = pd.read_csv(path)
        except FileNotFoundError:
            print("Issue while reading file {}".format(path))
            raise

        self.title = title 

    def to_sql_table(self, table_name, if_exists="replace", index=True):
        engine = create_engine('sqlite:///output/sanjeev_data.db', echo=False)
        data = self.data.copy()
        data.columns = [name.capitalize() + self.title for name in data.columns]
        data.set_index(data.columns[0], inplace=True)
        data.to_sql(table_name, engine, if_exists=if_exists, index=index)

    def new_columns(self, *column_names):
        for column_name in column_names:
            self.data[column_name] = ''


class parent_func:
    def __init__(self,ideal,name):
        self.name = name
        self.ideal = ideal         

class Ideal_func_instance(parent_func):

    def __init__(self,ideal,train,name):
        self.train_function = train
        super().__init__(ideal,name)

    def max_deviation_calculation(self):
        deviation = self.train_function - self.ideal
        return max(deviation.abs())
    
class put_ideal_function_map:


    def __init__(self, train_data,ideal_points):
        self.train_data = train_data
        self.ideal_points = ideal_points

    def map_test(self, test_points):
        ideal_counts = None
        delta = float('inf')

        for i,  ideal_set in enumerate(self.ideal_points.columns[1:5]):
            try:
                deviation =  Ideal_func_instance(self.ideal_points[ideal_set],self.train_data.iloc[:,i+1],ideal_set)
                max_deviation = deviation.max_deviation_calculation()
                y_loc = to_map_y(test_points[0],self.ideal_points['x'],self.ideal_points[ideal_set])
            except IndexError:
                print("IndexError") 
                raise IndexError


            curr_deviation = abs(y_loc - test_points[1])


            if abs(curr_deviation < max_deviation * np.sqrt(2)):
               if(ideal_counts is None) or (curr_deviation < delta):
                   ideal_counts = ideal_set
                   delta = curr_deviation

        if ideal_counts is None:
           return None, None
        return ideal_counts, delta


def to_map_y(x, ideal_x, ideal_y):

        try:
            match = ideal_y[ideal_x == x]
            if not match.empty:
                return match.iloc[0]
            else:
                raise IndexError
        except IndexError:
            raise IndexError    
                         

class process_ideal_function:

    def __init__(self, train_data, ideal_set):
        self.train_data = train_data
        self.ideal_set = ideal_set

    def  Get_best_ideal_function(self):
        ideal_pos = {}
        for train in self.train_data.columns:
            if train != 'x':
                trains = []
                for ideal in self.ideal_set.columns:
                    if ideal != 'x':
                        deviations = np.mean((self.ideal_set[ideal] - self.train_data[train]) ** 2)
                        trains.append(deviations)

                ideal_pos[train] = trains.index(min(trains)) + 1
        ideal_pos['x'] = 0
        unique_indices = list(set(ideal_pos.values()))
        best_fit = self.ideal_set.iloc[:, unique_indices].copy()
        
        best_fit.columns = [
            col if col == 'x' else f"{col}_{i}"
            for i, col in enumerate(best_fit.columns)
        ]


        return  put_ideal_function_map(self.train_data,best_fit)       
