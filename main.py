import sys
import os
import numpy as np
from PyQt4 import QtGui
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from solvers.rk4_N import rk4_N
from solvers.euler_method import euler_method
import csv


class MainWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.form_widget = PWidget(self)
        self.setGeometry(600, 300, 1000, 600)
        self.setWindowTitle('Disease Simulator')
        self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))

        _widget = QtGui.QWidget()
        _layout = QtGui.QVBoxLayout(_widget)
        _layout.addWidget(self.form_widget)
        self.setCentralWidget(_widget)

        extractAction = QtGui.QAction("&Exit", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave The App')
        extractAction.triggered.connect(self.close_application)

        resetAction = QtGui.QAction("&New ", self)
        resetAction.setShortcut("Ctrl+N")
        resetAction.setStatusTip('New Simulation')
        resetAction.triggered.connect(self.form_widget.new_sim)

        saveAction = QtGui.QAction("&Save ", self)
        saveAction.setShortcut("Ctrl+S")
        saveAction.setStatusTip('Save Simulation')
        saveAction.triggered.connect(self.form_widget.save_sim)


        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)
        fileMenu.addAction(resetAction)


        simMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&Simulation')


    def close_application(self):

        choice = QtGui.QMessageBox.question(self, 'Close!',
                                            "Are you sure you want to exit?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()

        else:
            pass


class CAWidget(QtGui.QWidget):
    pass


class PWidget(QtGui.QWidget):
            
    def __init__(self,parent):

        super(PWidget, self).__init__(parent)
        self.center()

        # vertical Box Layout

        solver = QtGui.QLabel('Solver:')
        parameters = QtGui.QLabel('parameters')
        ode_model = QtGui.QLabel('ODE Model:')
        initial_conditions = QtGui.QLabel('Initial Conditions')
        parameters_model = QtGui.QLabel('Parameters model')

        # Dropdown button Solvers

        self.Box_solver = QtGui.QComboBox(self)
        self.Box_solver.addItem("Runge Kuta 4")
        self.Box_solver.addItem("Euler")
        self.Box_solver.addItem("Other")
        self.Box_solver.currentIndexChanged.connect(self.selection_solver)

        # Dropdown button ODE Models

        self.Box_models = QtGui.QComboBox(self)
        self.Box_models.addItem("SI model")
        self.Box_models.addItem("SIR model")
        self.Box_models.addItem("SI model 2")
        self.Box_models.addItem("Other")
        self.Box_models.currentIndexChanged.connect(self.selection_model)

        # Solver parameters grid

        initial_time = QtGui.QLabel('Initial time ')
        final_time = QtGui.QLabel('Final time')
        simulation_steps = QtGui.QLabel('Simulation steps')

        self.val_ti = QtGui.QDoubleSpinBox()
        self.val_ti.setRange(0, 1e7)
        self.val_ti.setValue(0)
        self.val_ti.setSingleStep(0.0001)
        self.val_ti.setDecimals(4)

        self.val_tf = QtGui.QDoubleSpinBox()
        self.val_tf.setRange(0.001, 1e7)
        self.val_tf.setValue(100)
        self.val_tf.setSingleStep(0.0001)
        self.val_tf.setDecimals(4)

        self.val_num_steps = QtGui.QSpinBox()
        self.val_num_steps.setRange(0, 1e7)
        self.val_num_steps.setValue(100)

        grid_p = QtGui.QGridLayout()

        grid_p.addWidget(initial_time, 0, 0)
        grid_p.addWidget(self.val_ti, 0, 1)
        grid_p.addWidget(final_time, 1, 0)
        grid_p.addWidget(self.val_tf, 1, 1)
        grid_p.addWidget(simulation_steps, 2, 0)
        grid_p.addWidget(self.val_num_steps, 2, 1)

        # initial conditions grid

        x01 = QtGui.QLabel('x1(0)')
        x02 = QtGui.QLabel('x2(0)')
        x03 = QtGui.QLabel('x3(0)')
        x04 = QtGui.QLabel('x4(0)')

        self.val_x01 = QtGui.QDoubleSpinBox()
        self.val_x01.setRange(0, 1e7)
        self.val_x01.setValue(10)
        self.val_x01.setDecimals(4)


        self.val_x02 = QtGui.QDoubleSpinBox()
        self.val_x02.setRange(0, 1e7)
        self.val_x02.setValue(2)
        self.val_x02.setDecimals(4)


        self.val_x03 = QtGui.QDoubleSpinBox()
        self.val_x03.setRange(0, 1e7)
        self.val_x03.setValue(1)
        self.val_x03.setDecimals(4)


        self.val_x04 = QtGui.QDoubleSpinBox()
        self.val_x04.setRange(0, 1e7)
        self.val_x04.setValue(0)
        self.val_x04.setDecimals(4)

        grid_i = QtGui.QGridLayout()

        grid_i.addWidget(x01, 0, 0)
        grid_i.addWidget(self.val_x01, 0, 1)
        grid_i.addWidget(x02, 1, 0)
        grid_i.addWidget(self.val_x02, 1, 1)
        grid_i.addWidget(x03, 2, 0)
        grid_i.addWidget(self.val_x03, 2, 1)
        grid_i.addWidget(x04, 3, 0)
        grid_i.addWidget(self.val_x04, 3, 1)

        # Model parameters grid

        alpha_p = QtGui.QLabel('alpha')
        beta_p = QtGui.QLabel('beta')
        gamma_p = QtGui.QLabel('gamma')

        self.val_alpha=QtGui.QDoubleSpinBox()
        self.val_alpha.setRange(-1e7, 1e7)
        self.val_alpha.setValue(1)
        self.val_alpha.setDecimals(4)
        self.val_alpha.setSingleStep(0.0001)

        self.val_beta=QtGui.QDoubleSpinBox()
        self.val_beta.setRange(-1e7, 1e7)
        self.val_beta.setValue(1)
        self.val_beta.setDecimals(4)
        self.val_beta.setSingleStep(0.0001)

        self.val_gamma=QtGui.QDoubleSpinBox()
        self.val_gamma.setRange(-1e7, 1e7)
        self.val_gamma.setValue(0.5)
        self.val_gamma.setDecimals(4)
        self.val_gamma.setSingleStep(0.0001)

        grid_pm = QtGui.QGridLayout()

        grid_pm.addWidget(alpha_p, 0, 0)
        grid_pm.addWidget(self.val_alpha, 0, 1)
        grid_pm.addWidget(beta_p, 1, 0)
        grid_pm.addWidget(self.val_beta, 1, 1)
        grid_pm.addWidget(gamma_p, 2, 0)
        grid_pm.addWidget(self.val_gamma, 2, 1)


        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(solver)
        vbox.addWidget(self.Box_solver)
        #vbox.addWidget(parameters)
        vbox.addLayout(grid_p)
        vbox.addWidget(ode_model)
        vbox.addWidget(self.Box_models)
        #vbox.addWidget(initial_conditions)
        vbox.addLayout(grid_i)
        #vbox.addWidget(parameters_model)
        vbox.addLayout(grid_pm)

        # grid Layout
        grid = QtGui.QGridLayout()
        self.setLayout(grid)
        grid.setSpacing(10)

        grid.addLayout(vbox,1, 2)

        # button Erase
        btn1 = QtGui.QPushButton('Erase', self)
        btn1.resize(btn1.sizeHint())
        btn1.clicked.connect(self.errase)
        grid.addWidget(btn1, 3, 0)

        # button Save
        btn2 = QtGui.QPushButton('Save Data', self)
        btn2.resize(btn2.sizeHint())
        btn2.clicked.connect(self.save_sim)
        grid.addWidget(btn2, 3, 1)

        # button Solve
        btn3 = QtGui.QPushButton('SOLVE', self)
        btn3.resize(btn3.sizeHint())
        btn3.clicked.connect(self.solve)
        grid.addWidget(btn3, 2, 2)

        # progress bar
        #progress_bar =  QtGui.QProgressBar(self)
        #grid.addWidget(progress_bar, 2, 0, 1, 2)

        self.checkBox = QtGui.QCheckBox('Labels', self)
        grid.addWidget(self.checkBox, 2, 1)

        # pyplot
        self.figure = plt.figure(figsize=(15, 10))
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        grid.addWidget(self.toolbar, 0, 0, 1, 2)
        grid.addWidget(self.canvas, 1, 0, 1, 2)

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def new_sim(self):

        plt.cla()
        ax = self.figure.add_subplot(111)
        self.canvas.draw()

        self.val_ti.setValue(0)
        self.val_tf.setValue(50)
        self.val_num_steps.setValue(100)
        self.val_alpha.setValue(0.5)
        self.val_beta.setValue(0.5)
        self.val_gamma.setValue(0.5)
        self.val_x01.setValue(5)
        self.val_x02.setValue(1)
        self.val_x03.setValue(1)
        self.val_x04.setValue(0)

    def errase(self):
        plt.cla()
        ax = self.figure.add_subplot(111)
        self.canvas.draw()

    def file_open(self):
        name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')

        if name[-3:]!='.py':
            choice = QtGui.QMessageBox.question(self, 'Attention!',
                                                "You must choose a .py file",
                                                QtGui.QMessageBox.Ok)
        else:
            return name


    def selection_solver(self):

        ti = np.float(self.val_ti.value())
        tf = np.float(self.val_tf.value())
        num_steps = np.int(self.val_num_steps.value())

        f, X0, consts = self.selection_model()

        if self.Box_solver.currentText() == 'Runge Kuta 4':
            S = rk4_N

        elif self.Box_solver.currentText() == 'Euler':
            S = euler_method

        elif self.Box_solver.currentText() == 'Other':

            filename = str(self.file_open())
            directory, module_name = os.path.split(filename)
            module_name = os.path.splitext(module_name)[0]
            path = list(sys.path)
            sys.path.insert(0, directory)

            try:
                module = __import__(module_name)
            finally:
                sys.path[:] = path  # restore

            name = (filename.replace(os.getcwd() + '/solvers/', ''))[:-3]
            S = getattr(module, name)

        y = S(f, X0, consts, ti, tf, num_steps)
        return y

    def selection_model(self):

        alpha = np.float(self.val_alpha.value())
        beta = np.float(self.val_beta.value())
        gamma = np.float(self.val_gamma.value())

        x01 = np.float(self.val_x01.value())
        x02 = np.float(self.val_x02.value())
        x03 = np.float(self.val_x03.value())
        x04 = np.float(self.val_x04.value())

        if self.Box_models.currentText() == 'SI model':
            consts = [alpha, beta]
            X0 = [x01, x02]
            from models.SI_model import SI_model as model

        elif self.Box_models.currentText() == 'SIR model':
            consts = [alpha, beta]
            X0 = [x01, x02, x03]
            from models.SIR_model import SIR_model as model

        elif self.Box_models.currentText() == 'SI model 2':
            consts = [alpha, beta, gamma]
            X0 = [x01, x02]
            from models.SI_model2 import SI_model2 as model

        elif self.Box_models.currentText() == 'Other':
            filename = str(self.file_open())

            directory, module_name = os.path.split(filename)
            module_name = os.path.splitext(module_name)[0]
            path = list(sys.path)
            sys.path.insert(0, directory)

            try:
                module = __import__(module_name)
            finally:
                sys.path[:] = path  # restore

            name = (filename.replace(os.getcwd()+'/models/', ''))[:-3]
            model = getattr(module, name)
            #X0 =  import it from a file
            #consts = also import them from a file

        return model, X0, consts

    def save_sim(self):

        time_s, results = self.solve()
        name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')+'.csv'
        A = []
        for i in range(len(results[0])):
            a = []
            a.append(time_s[i])
            for j in range(len(results)):
                a.append(results[j][i])
            A.append(a)

        #rows = zip(time_s, A)
        with open(name, 'w') as csvfile:
            writer = csv.writer(csvfile)
            for r, row in enumerate(A):
                writer.writerow(row)

    def solve(self):

        #plt.cla() #this clears the plot
        ax = self.figure.add_subplot(111)
        y = self.selection_solver()

        solutions = [[] for j in range(len(y[1][0]))]

        for ye in y[1]:
            for j in range(len(solutions)):
                solutions[j].append(ye[j])


        consts_names = "".join(['$alpha$=', str(self.val_alpha.value()), ' $beta$=', str(self.val_beta.value()), ' $gamma$=',
                          str(self.val_gamma.value()), '\n',  '$S$'])
        labels = [consts_names, '$I$', '$R$']

        for ind, solution in enumerate(solutions):
            ax.plot(y[0], solution, '-o', label=labels[ind])

        if self.checkBox.isChecked() is True:
            ax.legend(loc='best', prop={'size': 10})

        ax.set_title('Simulation Results')
        plt.xlabel('Simulation time')
        plt.ylabel('Population')

        self.canvas.draw()

        return y[0], solutions

def main():
    app = QtGui.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec_()


if __name__ == '__main__':
    main()
