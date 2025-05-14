from pathlib import Path
from sqlalchemy import create_engine
from visualization import Plotter
from connections import Get_connections,process_ideal_function

Path("output/sanjeev_data.db").parent.mkdir(parents=True, exist_ok=True)
Path("output/sanjeev_data.db").touch()

Train_path = r"Datasets1/train.csv"
Ideal_path = r"Datasets1/ideal.csv"
Test_path =  r"Datasets1/test.csv"

Train_data = Get_connections(path = Train_path,title='train')
Ideal_data = Get_connections(path = Ideal_path,title='ideal')
Test_data = Get_connections(path = Test_path,title='Test')

engine = create_engine('sqlite:///output/sanjeev_data.db')

obj_ideal_func = process_ideal_function(Train_data.data, Ideal_data.data)
obj_map_func = obj_ideal_func.Get_best_ideal_function()

ideal_points = obj_map_func.ideal_points

Test_data.new_columns('ideal_function', 'y_delta')
Test_data = Test_data.data

for i, j in Test_data.iterrows():
    ideal_values, y_del = obj_map_func.map_test([j['x'], j['y']])
    Test_data.loc[i, 'ideal_function'] = ideal_values
    Test_data.loc[i, 'y_delta'] = y_del


# Store test data with mappings in SQL table

Ideal_data.to_sql_table('ideal', if_exists='replace', index=False)
Train_data.to_sql_table('train', if_exists='replace', index=False)
Test_data.to_sql('test', con=engine, if_exists='replace', index=False)

obj_plotter = Plotter(Train_data.data, ideal_points, Test_data)
obj_plotter.ideal_function_plot()
obj_plotter.training_data_with_ideal_plot()
obj_plotter.test_data_with_ideal_plot()
