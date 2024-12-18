import pandas as pd
import pyqtgraph as pg
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('EQ.ui', self)
        self.resize(1000, 500)

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

        self.data = pd.read_csv('1001.csv')
        self.timestamps = self.data['timestamp'].values
        self.fhr = self.data['fhr'].values
        self.uc = self.data['uc'].values

        self.window_size = 30
        self.plot_range = self.timestamps[:self.window_size]
        self.plot_data_index = 0

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(100)

        # el btn esmo start_btn

    def update_plot(self):
        if self.plot_data_index + self.window_size <= len(self.timestamps):
            time_window = self.timestamps[self.plot_data_index:self.plot_data_index + self.window_size]
            fhr_window = self.fhr[self.plot_data_index:self.plot_data_index + self.window_size]
            uc_window = self.uc[self.plot_data_index:self.plot_data_index + self.window_size]

            self.FHR_graph.clear()
            self.UC_grah.clear()

            self.FHR_graph.plot(time_window, fhr_window, pen='r')
            self.UC_grah.plot(time_window, uc_window, pen='g')

            self.plot_data_index += 1

            self.FHR_graph.setXRange(self.timestamps[self.plot_data_index], self.timestamps[self.plot_data_index + self.window_size])
            self.UC_grah.setXRange(self.timestamps[self.plot_data_index], self.timestamps[self.plot_data_index + self.window_size])

        else:
            self.plot_data_index = 0


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()
