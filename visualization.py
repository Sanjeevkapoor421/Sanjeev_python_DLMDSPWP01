from bokeh.plotting import figure, output_file, show
from bokeh.layouts import gridplot


class Plotter:
    def __init__(self, train_data, ideal_data, test_data):
        self.train_data = train_data
        self.ideal_data = ideal_data
        self.test_data = test_data

    def ideal_function_plot(self):
        plots = self.to_plots_generate(self.ideal_data, plot_type='line')
        self.to_output_plot(plots, "ideal_functions")

    def training_data_with_ideal_plot(self):
        plots = self.to_plots_generate(self.train_data, plot_type='line', is_ideal=True)
        self.to_output_plot(plots, "training_data_vs_ideal")

    def to_plots_generate(self, data_set, plot_type, is_ideal=False):
        plot_list = []
        for i in range(1, min(5, len(data_set.columns))):
            x_feature = data_set['x']
            y_label = data_set.iloc[:, i]
            plot_name = f"{data_set.columns[i]} vs x"

            p = figure(title=plot_name, x_axis_label='x', y_axis_label='y', tools="pan,box_zoom,reset,save", 
                          width=400, height=300)
            
            if plot_type == 'line':
                p.line(x_feature, y_label, legend_label=data_set.columns[i], line_width=2, line_color='red' if not is_ideal else 'blue')

            plot_list.append(p)
        return plot_list
    
    def test_data_with_ideal_plot(self):
        plots = self.to_test_plot_generation()
        self.to_output_plot(plots, "test_points_vs_ideal")


    def to_test_plot_generation(self):
        plot_list = []
        for point in self.test_data.itertuples(index=True, name='Pandas'):
            if point.ideal_function:
                p = figure(title=f"Test Point: ({point.x},{round(point.y, 2)}) with Ideal {point.ideal_function}", 
                              x_axis_label='x', y_axis_label='y', tools="pan,box_zoom,reset,save", 
                              width=400, height=300)
                p.line(self.ideal_data.x, self.ideal_data[point.ideal_function], legend_label=f"Ideal {point.ideal_function}",
                          line_width=2, line_color='navy', line_alpha=0.7)
                p.scatter([point.x], [round(point.y, 4)], fill_color="red", legend_label="Test points", size=8, marker='diamond')
                plot_list.append(p)
        return plot_list

    def to_output_plot(self, plots, filename):
        grid = gridplot(plots, ncols=2, width=400, height=400)
        output_file(f"output/{filename}.html")
        show(grid)
