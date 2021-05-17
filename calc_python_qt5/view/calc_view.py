"""Calc View Module."""
import sys

from PyQt5 import QtWidgets, uic
from PyQt5.Qt import QTextEdit, QLabel

from model import validate_number, do_calculation

UI_FILE = 'view/calc_view.ui'
Ui_CalcView, QtSuperClass = uic.loadUiType(UI_FILE)


class CalcView(QtWidgets.QMainWindow, Ui_CalcView):
    """Represents the view tier of calc window."""

    def __init__(self):
        """Init all componets of window."""
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.btn_zero.pressed.connect(lambda: self.in_pressed(0))
        self.btn_one.pressed.connect(lambda: self.in_pressed(1))
        self.btn_two.pressed.connect(lambda: self.in_pressed(2))
        self.btn_three.pressed.connect(lambda: self.in_pressed(3))
        self.btn_four.pressed.connect(lambda: self.in_pressed(4))
        self.btn_five.pressed.connect(lambda: self.in_pressed(5))
        self.btn_six.pressed.connect(lambda: self.in_pressed(6))
        self.btn_seven.pressed.connect(lambda: self.in_pressed(7))
        self.btn_eigth.pressed.connect(lambda: self.in_pressed(8))
        self.btn_nine.pressed.connect(lambda: self.in_pressed(9))
        self.btn_comma.pressed.connect(lambda: self.in_pressed(','))
        self.btn_add.pressed.connect(lambda: self.operator_pressed('+'))
        self.btn_subtract.pressed.connect(lambda: self.operator_pressed('-'))
        self.btn_multipl.pressed.connect(lambda: self.operator_pressed('*'))
        self.btn_divide.pressed.connect(lambda: self.operator_pressed('/'))
        self.btn_result.pressed.connect(self.calc_pressed)
        self.btn_clear.pressed.connect(self.clear_pressed)
        self.result_text().setFocus()

    def in_pressed(self, number):
        """Receive the number pressed button."""
        result = self.result_text().toPlainText()
        result = validate_number(result, number)
        self.result_text().setPlainText(result)

    def operator_pressed(self, choose_op):
        """Print the oprator signal on result text."""
        result = self.result_text().toPlainText()
        if result:
            if not result[-1] in ('-', '+', '*', '/'):
                result += choose_op
                self.result_text().setPlainText(result)

    def calc_pressed(self):
        """Execute the calculator."""
        calculation = self.result_text().toPlainText()
        try:
            calculation = do_calculation(calculation)
        except ZeroDivisionError:
            self.error_label().setText('division by zero')
        except Exception:
            self.error_label().setText('NaN')
        else:
            self.result_text().setPlainText(calculation)
            self.error_label().setText('')

    def clear_pressed(self):
        """Clear the result text."""
        self.result_text().clear()

    def result_text(self) -> QTextEdit:
        """Return the strong typed of text edit component."""
        return self.text_result

    def error_label(self) -> QLabel:
        """Return the strong typed of label component."""
        return self.lbl_error

    @staticmethod
    def quit():
        """Quit Calc App."""
        sys.exit()
