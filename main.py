import sys
from PyQt5.QtWidgets import QApplication
from ui import CalculatorApp  # ui.py 파일에서 CalculatorApp 클래스를 임포트합니다.


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = CalculatorApp()
    ex.show()  # UI를 화면에 표시합니다.
    sys.exit(app.exec_())