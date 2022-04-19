import sys
import PyQt5.QtWidgets as qtw
from PyQt5.uic import loadUi
import GeneticAlgorithm as GA


class MainWindow(qtw.QMainWindow):
    tableKeys = ['Name', 'Price', 'Importance']
    expenseDict = []

    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("mainwindow.ui", self)
        self.loadItemData()
        self.runButton.clicked.connect(self.runGA)

    def loadItemData(self):
        for i in range(len(GA.expenses)):
            self.expenseDict.append(dict(zip(self.tableKeys, GA.expenses[i])))
        #print(self.foodDict)
        self.itemsTableWidget.setRowCount(len(self.expenseDict))
        for i in range(len(self.expenseDict)):
            self.itemsTableWidget.setItem(i, 0, qtw.QTableWidgetItem(self.expenseDict[i]["Name"]))
            self.itemsTableWidget.setItem(i, 1, qtw.QTableWidgetItem(str(self.expenseDict[i]["Price"])))
            self.itemsTableWidget.setItem(i, 2, qtw.QTableWidgetItem(str(self.expenseDict[i]["Importance"])))

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
            for i in range(len(GA.expenses)):
                self.expenseDict.append(dict(zip(self.tableKeys, GA.expenses[i])))
            for i in range(len(result)):
                if result[i] == 1:

                    self.offspringTableWidget.setItem(actualIndex, 0, qtw.QTableWidgetItem(self.expenseDict[i]["Name"]))
                    self.offspringTableWidget.setItem(actualIndex, 1, qtw.QTableWidgetItem(str(self.expenseDict[i]["Price"])))
                    self.offspringTableWidget.setItem(actualIndex, 2, qtw.QTableWidgetItem(str(self.expenseDict[i]["Importance"])))
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
