#!/bin/python
"""Simple Calc App."""
import sys
import PyQt5.QtWidgets as qtwid

from view import CalcView


def main():
    """Run the app and creates a Qt Window."""
    app = qtwid.QApplication(sys.argv)
    v = CalcView()
    v.show()
    app.exec_()


if __name__ == '__main__':
    main()
