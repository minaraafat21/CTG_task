import pandas as pd
import pyqtgraph as pg
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtCore import QTimer


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('EQ.ui', self)
        self.resize(1000, 500)

        # Initialize graphs and labels
        self.FHR_graph.showGrid(x=True, y=True)
        self.FHR_graph.setLabel('left', 'FHR', units='bpm')
        self.FHR_graph.setLabel('bottom', 'Time', units='s')
        self.FHR_graph.setTitle('FHR Graph')

        self.UC_grah.showGrid(x=True, y=True)
        self.UC_grah.setLabel('left', 'UC')
        self.UC_grah.setLabel('bottom', 'Time', units='s')
        self.UC_grah.setTitle('UC Graph')

        self.FHR_label.setText('FHR: 150 bpm')
        self.CTG_label.setText('CTG Interpretation: Normal')

        # Initialize data variables
        self.timestamps = []
        self.fhr = []
        self.uc = []

        # Initialize plot window size
        self.window_size = 30
        self.plot_data_index = 0

        # Initialize timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(100)

        # Load file button (you'll link this button from the UI)
        self.load_button.clicked.connect(self.load_csv_file)

    def load_csv_file(self):
        """ Opens file dialog to load a CSV file dynamically. """
        file_path, _ = QFileDialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv);;All Files (*)")
        
        if file_path:
            # Read the selected CSV file
            try:
                self.data = pd.read_csv(file_path)
                self.timestamps = self.data['timestamp'].values
                self.fhr = self.data['fhr'].values
                self.uc = self.data['uc'].values

                # Reset plot data index to start from the beginning
                self.plot_data_index = 0
                self.update_plot()
            except Exception as e:
                print(f"Error loading CSV file: {e}")

    def update_plot(self):
        if self.plot_data_index + self.window_size <= len(self.timestamps):
            time_window = self.timestamps[self.plot_data_index:self.plot_data_index + self.window_size]
            fhr_window = self.fhr[self.plot_data_index:self.plot_data_index + self.window_size]
            uc_window = self.uc[self.plot_data_index:self.plot_data_index + self.window_size]

            # Clear previous plots
            self.FHR_graph.clear()
            self.UC_grah.clear()

            # Plot new data
            self.FHR_graph.plot(time_window, fhr_window, pen='r')
            self.UC_grah.plot(time_window, uc_window, pen='g')

            # Update the plot index for the next window
            self.plot_data_index += 1

            # Ensure that the X range does not exceed the length of the data
            if self.plot_data_index + self.window_size <= len(self.timestamps):
                self.FHR_graph.setXRange(self.timestamps[self.plot_data_index], self.timestamps[self.plot_data_index + self.window_size])
                self.UC_grah.setXRange(self.timestamps[self.plot_data_index], self.timestamps[self.plot_data_index + self.window_size])
            else:
                self.FHR_graph.setXRange(self.timestamps[self.plot_data_index], self.timestamps[-1])
                self.UC_grah.setXRange(self.timestamps[self.plot_data_index], self.timestamps[-1])

        else:
            self.plot_data_index = 0


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()
