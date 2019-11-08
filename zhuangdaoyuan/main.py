#!/usr/bin/python
# listOdd=[]
# listEven=[]
# for i in range(1,101):
#    if(i%2==0):
#       listEven.append(i)
#    else:
#       listOdd.append(i)
# print("listOdd----",listOdd[0:50])
# print("listEven+---",listEven[0:len(listEven)])
#
# listEven.extend(listOdd)
# listEven.sort()
# print("listEven merge---",listEven[0:len(listEven)])
import sys

# 这里我们提供必要的引用。基本控件位于pyqt5.qtwidgets模块中。
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox, QGridLayout, QDesktopWidget, \
    QLabel, QLineEdit, QTextEdit, QMainWindow, QAction, QMenuBar, qApp, QLCDNumber, QVBoxLayout, QHBoxLayout, QSlider,\
    QTableView,QHeaderView
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont


class Example(QWidget):
    def __init__(self):
        super().__init__()
        # 界面绘制交给InitUi方法
        #地址栏
        self.address =None
        # 查找按鈕
        self.searchBtn = None
        # 动态Tab
        self.tabLayout = None

        # 表格
        self.tableView = None

        self.initUI()

    def closeEvent(self, QCloseEvent):
        reply = QMessageBox.question(self, "MessageBox", "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if (reply == QMessageBox.Yes):
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    #   提示
    def toolTip(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        # 创建一个PushButton并为他设置一个tooltip
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        # btn.sizeHint()显示默认尺寸
        btn.resize(100, 50)
        # 移动窗口的位置
        btn.move(100, 75)

    #   网格布局
    def gridLayout(self):
        grid = QGridLayout()
        self.setLayout(grid)
        names = ['Clear', 'Back', '', 'Close',
                 '7', '8', '9', '/',
                 '6', '5', '4', '*',
                 '3', '2', '1', '+',
                 '0', '.', '=', '-']
        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):
            if (name == ''):
                continue
            btn = QPushButton(name)
            grid.addWidget(btn, *position)

    #   评论
    def editText(self):
        parent = QWidget()
        self.setCentralWidget(parent)
        title = QLabel('标题')
        author = QLabel('作者')
        review = QLabel('评论')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        parent.setLayout(grid)

    #   状态栏
    def statusBarCust(self):
        # self.statusBar().showMessage('Ready')
        self.statusBar().showMessage('Ready')

    #   菜单栏
    def menu(self):
        exitAction = QAction(QIcon('exit.png'), '退出', self)
        exitAction.setStatusTip('退出应用')
        exitAction.setShortcut('Ctrl+Backspace')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()
        menu = self.menuBar()
        self.toolbar = self.addToolBar("退出应用")
        self.toolbar.addAction(exitAction)
        fileMenu = menu.addMenu('File')
        fileMenu.addAction(exitAction)

    #   Slider
    def slider(self):
        parent = QWidget()

        lcd = QLCDNumber()
        sld = QSlider(Qt.Horizontal)
        vLayout = QVBoxLayout()
        vLayout.addWidget(lcd)
        vLayout.addWidget(sld)
        parent.setLayout(vLayout)

        self.setCentralWidget(parent)

        sld.valueChanged.connect(lcd.display)

    #  GitLab项目Tag分析
    # 纵向布局
    def vboxLayout(self):
        mainLayout = QVBoxLayout(self)

        # 顶部项目地址输入栏
        hbox = QHBoxLayout(self)
        self.searchBtn = QPushButton("查找", self)
        self.address = QLineEdit(self)
        hbox.addWidget(self.address)
        hbox.addWidget(self.searchBtn)
        self.searchBtn.clicked.connect(self.queryProject())
        mainLayout.addLayout(hbox)

        # 项目tab
        self.tabLayout = QHBoxLayout()
        mainLayout.addLayout(self.tabLayout)

        # 设置表格属性
        self.tableView = QTableView()
        # 表格宽度的自适应调整
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        mainLayout.addWidget(self.tableView)

        self.setLayout(mainLayout)

    #查询项目
    def queryProject(self):
        if str.__len__(self.address)==0:
            print('地址為空')
        else :
            print('地址不為空')


    def initUI(self):

        # self.toolTip()
        # self.gridLayout()
        # self.editText()
        # self.statusBarCust()
        # self.menu()
        # self.slider()
        self.vboxLayout()


        # 设置窗口的位置和大小gf
        self.setGeometry(300, 300, 900, 500)
        self.center()
        # 设置窗口的标题
        self.setWindowTitle('分析项目TAG')
        # 设置窗口的图标，引用当前目录下的web.png图片
        self.setWindowIcon(QIcon('a.jpg'))
        # 显示窗口j
        self.show()


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
