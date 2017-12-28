import sys
from PyQt5.QtWidgets import QApplication, QDialog
from GUI.menu_ui import Ui_Menu
from GUI.solver_ui import Ui_Solver

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

def main():
    app = QApplication(sys.argv)
    form = Menu()
    form.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
