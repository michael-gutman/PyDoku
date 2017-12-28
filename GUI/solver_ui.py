# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'solver.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Solver(object):
    def setupUi(self, Solver):
        Solver.setObjectName("Solver")
        Solver.resize(296, 344)
        Solver.setMinimumSize(QtCore.QSize(296, 344))
        Solver.setMaximumSize(QtCore.QSize(296, 344))
        self.verticalLayout = QtWidgets.QVBoxLayout(Solver)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Solver)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableWidget = QtWidgets.QTableWidget(Solver)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(9)
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(30)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(23)
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(Solver)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Reset)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Solver)
        self.buttonBox.accepted.connect(Solver.accept)
        self.buttonBox.rejected.connect(Solver.reject)
        QtCore.QMetaObject.connectSlotsByName(Solver)

    def retranslateUi(self, Solver):
        _translate = QtCore.QCoreApplication.translate
        Solver.setWindowTitle(_translate("Solver", "PyDoku Solver"))
        self.label.setText(_translate("Solver", "Enter the puzzle below, then hit \'Apply\' to show solution."))

