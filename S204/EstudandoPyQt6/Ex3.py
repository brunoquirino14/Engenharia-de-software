import sys
from PyQt6.QtWidgets import QApplication, QWidget,QPushButton, QLabel

app = QApplication(sys.argv)
janela = QWidget()
janela.resize(800,600)
janela.setWindowTitle("Primeira")

btn = QPushButton("Botao 1", janela)
btn.setGeometry(100,100,150,80)
btn.setStyleSheet('background-color:Blue;color:white')

label = QLabel("Texto",janela)
label.move(400,100)

janela.show()

app.exec()