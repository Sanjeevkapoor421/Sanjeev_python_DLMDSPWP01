import unittest
import pandas as pd
from connections import Ideal_func_instance,process_ideal_function, to_map_y, put_ideal_function_map


class Testconnections(unittest.TestCase):

    def setUp(self):
        self.df_sample_train = pd.DataFrame({
            'x': [1,2,3],
            'y1': [2,4,6],
            'y2': [1,2,3]
        })
        self.df_sample_test= pd.DataFrame({
            'x': [2],
            'y': [3]})
    
    def test_max_deviation_calculation(self):
        obj = Ideal_func_instance(
            ideal=self.df_sample_train['y1'],
            train=self.df_sample_train['y2'],
            name='test'
        )
        deviation = obj.max_deviation_calculation()
        self.assertIsInstance(deviation, (int, float))

    def test_to_map_y(self):
        y = to_map_y(2, self.df_sample_train['x'], self.df_sample_train['y1'])
        self.assertEqual(y, 4)
        with self.assertRaises(IndexError):
            to_map_y(5, self.df_sample_train['x'], self.df_sample_train['y1'])

    def test_put_ideal_function_map(self):
        train_data = self.df_sample_train[['x', 'y2']].copy()
        ideal_data = self.df_sample_train[['x', 'y1']].copy()
        mapper = put_ideal_function_map(train_data, ideal_data)
        result = mapper.map_test((2, 4))
        self.assertIsInstance(result, tuple)

    def test_process_ideal_function(self):
        obj_process = process_ideal_function(self.df_sample_train, self.df_sample_train)
        result = obj_process.Get_best_ideal_function()
        self.assertIsInstance(result, put_ideal_function_map)

if __name__ == '__main__':
    unittest.main()


