import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
)
from PyQt5.QtCore import Qt


class CalculatorApp(QWidget):
    """
    두 개의 숫자를 입력받아 덧셈 결과를 보여주는 PyQt 애플리케이션 클래스
    """

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """UI를 초기화하고 위젯을 배치합니다."""
        # 위젯 생성
        self.edit1 = QLineEdit()
        self.edit1.setPlaceholderText("첫 번째 숫자")
        self.edit1.setAlignment(Qt.AlignRight)

        self.edit2 = QLineEdit()
        self.edit2.setPlaceholderText("두 번째 숫자")
        self.edit2.setAlignment(Qt.AlignRight)

        self.add_button = QPushButton("add")
        self.result_label = QLabel("result ")
        self.result_label.setStyleSheet("font-size: 14px; font-weight: bold;")

        # 레이아웃 설정
        # 수평 박스 레이아웃에 숫자 입력창 2개를 추가
        input_box = QHBoxLayout()
        input_box.addWidget(self.edit1)
        input_box.addWidget(QLabel("+"))
        input_box.addWidget(self.edit2)

        # 수직 박스 레이아웃에 위젯들을 순서대로 추가
        main_layout = QVBoxLayout()
        main_layout.addLayout(input_box)
        main_layout.addWidget(self.add_button)
        main_layout.addWidget(self.result_label)

        self.setLayout(main_layout)

        # 시그널과 슬롯 연결
        # 버튼을 클릭하면 calculate_sum 메서드가 호출됩니다.
        self.add_button.clicked.connect(self.calculate_sum)
        # 엔터 키를 눌러도 계산이 되도록 연결합니다.
        self.edit1.returnPressed.connect(self.calculate_sum)
        self.edit2.returnPressed.connect(self.calculate_sum)

        # 윈도우 기본 설정
        self.setWindowTitle("간단한 덧셈 계산기")
        self.setGeometry(300, 300, 350, 150)
        # self.show() # show()는 main.py에서 호출됩니다.

    def calculate_sum(self):
        """입력된 두 숫자를 더하고 결과를 라벨에 표시합니다."""
        try:
            # QLineEdit에서 텍스트를 가져와 float으로 변환합니다.
            num1 = float(self.edit1.text() or 0)
            num2 = float(self.edit2.text() or 0)
            result = num1 + num2

            # 정수이면 소수점 없이 표시
            if result.is_integer():
                self.result_label.setText(f"결과: {int(result)}")
            else:
                self.result_label.setText(f"결과: {result}")

        except ValueError:
            # 숫자로 변환할 수 없는 값이 입력되면 에러 메시지를 표시합니다.
            self.result_label.setText("결과: 유효한 숫자를 입력해주세요.")