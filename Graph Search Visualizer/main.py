from Control_Panel import MyGUI
import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    # don't auto scale when drag app to a different monitor.
    # QApplication.setAttribute(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

    app = QApplication(sys.argv)
    # # app.setStyleSheet('''
    # # 	QWidget {
    # # 		font-size: 30px;
    # # 	}
    # # ''')
    # layout = QHBoxLayout()
    # layout.addWidget(MyApp())
    # window = MyApp()
    window = MyGUI()
    window.setWindowTitle("Graph Algorithms Visualizer")
    # background-color: #f0f0f0;
    # window.setStyleSheet('''
    #     QWidget {
    #         background-color: #a86868;
    #     }
    # ''')
# with open('style.qss', 'r') as f1, open('QPushButton.qss', 'r') as f2:
#     style1 = f1.r
#     window.setStyleSheet(style1 + style2)ead()
#     style2 = f2.read()

    window.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')