import sys
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem
from GUI.menu_ui import Ui_Menu
from GUI.solver_ui import Ui_Solver
import solver

class Menu(QDialog, Ui_Menu):
    def __init__(self, parent=None):
        super(Menu, self).__init__(parent)
        self.setupUi(self)
        self.solve_btn.clicked.connect(self.openSolver)
        self.solver = Solver(self)

    def openSolver(self):
        self.solver.show()

class Solver(QDialog, Ui_Solver):
    def __init__(self, parent=None):
        super(Solver, self).__init__(parent)
        self.setupUi(self)
        self.solve_btn.clicked.connect(self.solveClick)
        self.reset_btn.clicked.connect(self.tableWidget.clear)
        self.cancel_btn.clicked.connect(self.close)

    def solveClick(self):
        puzzle = []
        for i in range(9):
            row = []
            for j in range(9):
                item = self.tableWidget.item(i, j)
                if item == None:
                    item = '0'
                else:
                    item = item.text()
                if item not in list('123456789'):
                    item = '0'
                row.append(int(item))
            puzzle.append(row[:])
        soln = solver.solve(puzzle)
        self.showSolution(soln)

    def showSolution(self, soln):
        for i in range(9):
            for j in range(9):
                item = QTableWidgetItem(str(soln[i][j]))
                self.tableWidget.setItem(i, j, item)

def main():
    app = QApplication(sys.argv)
    form = Menu()
    form.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
