import sys
import PyQt5.QtWidgets as qtw
from PyQt5.uic import loadUi
import GeneticAlgorithm as GA


class MainWindow(qtw.QMainWindow):
    tableKeys = ['Name', 'Calories', 'Protein', 'Carbs', 'Fats', 'Price']
    foodDict = []

    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("mainwindow.ui", self)
        self.loadItemData()
        self.runButton.clicked.connect(self.runGA)

    def loadItemData(self):
        for i in range(len(GA.foods)):
            self.foodDict.append(dict(zip(self.tableKeys, GA.foods[i])))
        #print(self.foodDict)
        self.itemsTableWidget.setRowCount(len(self.foodDict))
        for i in range(len(self.foodDict)):
            self.itemsTableWidget.setItem(i, 0, qtw.QTableWidgetItem(self.foodDict[i]["Name"]))
            self.itemsTableWidget.setItem(i, 1, qtw.QTableWidgetItem(str(self.foodDict[i]["Calories"])))
            self.itemsTableWidget.setItem(i, 2, qtw.QTableWidgetItem(str(self.foodDict[i]["Protein"])))
            self.itemsTableWidget.setItem(i, 3, qtw.QTableWidgetItem(str(self.foodDict[i]["Carbs"])))
            self.itemsTableWidget.setItem(i, 4, qtw.QTableWidgetItem(str(self.foodDict[i]["Fats"])))
            self.itemsTableWidget.setItem(i, 5, qtw.QTableWidgetItem(str(self.foodDict[i]["Price"])))

    def runGA(self):
        funds = float(self.fundsLine.text())
        size = int(self.pobLine.text())
        generations = int(self.genLine.text())
        print(funds, size, generations)
        result = []
        actualIndex = 0
        if funds > 0 and size > 0 and generations > 0:
            result = GA.run(size, generations, funds)
            self.offspringTableWidget.setRowCount(result.count(1))
            for i in range(len(GA.foods)):
                self.foodDict.append(dict(zip(self.tableKeys, GA.foods[i])))
            for i in range(len(result)):
                if result[i] == 1:

                    self.offspringTableWidget.setItem(actualIndex, 0, qtw.QTableWidgetItem(self.foodDict[i]["Name"]))
                    self.offspringTableWidget.setItem(actualIndex, 1, qtw.QTableWidgetItem(str(self.foodDict[i]["Calories"])))
                    self.offspringTableWidget.setItem(actualIndex, 2, qtw.QTableWidgetItem(str(self.foodDict[i]["Protein"])))
                    self.offspringTableWidget.setItem(actualIndex, 3, qtw.QTableWidgetItem(str(self.foodDict[i]["Carbs"])))
                    self.offspringTableWidget.setItem(actualIndex, 4, qtw.QTableWidgetItem(str(self.foodDict[i]["Fats"])))
                    self.offspringTableWidget.setItem(actualIndex, 5, qtw.QTableWidgetItem(str(self.foodDict[i]["Price"])))
                    actualIndex += 1


app = qtw.QApplication(sys.argv)
mainWindow = MainWindow()
widget = qtw.QStackedWidget()
widget.addWidget(mainWindow)
widget.show()
app.setStyle('Fusion')
try:
    sys.exit(app.exec_())
except:
    print('Exiting')
