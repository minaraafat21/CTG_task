import pandas as pd
import pyqtgraph as pg
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


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

        # Set the initial text on the labels
        self.FHR_label.setText('FHR: 150 bpm')
        self.CTG_label.setText('CTG Interpretation: Normal')

        ## el btn esmo start_btn

        self.load_and_plot_data('1001.csv')

    def load_and_plot_data(self, filename):
        data = pd.read_csv(filename)

        timestamps = data['timestamp'].values
        fhr = data['fhr'].values
        uc = data['uc'].values

        self.FHR_graph.plot(timestamps, fhr, pen='r')  # Red line for FHR

        self.UC_grah.plot(timestamps, uc, pen='g')  # Green line for UC


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()
