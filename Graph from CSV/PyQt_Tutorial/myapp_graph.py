import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import pyqtgraph as pg
from pyqtgraph.graphicsItems.GraphicsItem import GraphicsItem
from pyqtgraph.graphicsItems.PlotCurveItem import PlotCurveItem
from pyqtgraph.graphicsItems.PlotItem.PlotItem import PlotItem
from pyqtgraph.widgets.PlotWidget import PlotWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # pitem = PlotItem()
        plt = pg.plot()
        pWidget = PlotWidget()
        
        x = [0,1,2,3,4,5]
        y = [0,1,2,3,4,5]
        y2 = [5,4,3,2,1,0]
        
        p1 = plt.plot(x,y, pen = 'r')
        p2 = plt.plot(x,y2, pen = 'b')

        # pitem.addItem(p1)
        # plt.addItem(p2)
        pWidget.addItem(p1)
        pWidget.addItem(p2)
        self.setWindowTitle("My App")
        
   
4

app = QApplication(sys.argv)

window = MainWindow()

window.show()

app.exec()