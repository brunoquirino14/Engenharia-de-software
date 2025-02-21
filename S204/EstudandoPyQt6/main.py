from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt6.QtGui import QPixmap, QFont, QPalette, QBrush
from PyQt6.QtCore import Qt
import sys

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Game Launcher - Login")
        self.setGeometry(100, 100, 400, 500)
        self.setFixedSize(400, 500)
        
        # Definir fundo
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(QPixmap("background.jpg")))
        self.setPalette(palette)
        
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Título
        self.title_label = QLabel("Game Launcher", self)
        self.title_label.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        self.title_label.setStyleSheet("color: white;")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Campo de Usuário
        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Usuário")
        self.username_input.setFont(QFont("Arial", 12))
        self.username_input.setStyleSheet(self.input_style())
        
        # Campo de Senha
        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Senha")
        self.password_input.setFont(QFont("Arial", 12))
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setStyleSheet(self.input_style())
        
        # Botão de Login
        self.login_button = QPushButton("Entrar", self)
        self.login_button.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        self.login_button.setStyleSheet(self.button_style())
        self.login_button.clicked.connect(self.login)
        
        # Adicionar widgets ao layout
        layout.addWidget(self.title_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        
        self.setLayout(layout)
        
    def input_style(self):
        return (
            "QLineEdit {"
            "    border: 2px solid white;"
            "    border-radius: 10px;"
            "    padding: 10px;"
            "    background-color: rgba(255, 255, 255, 0.2);"
            "    color: white;"
            "}"
            "QLineEdit::placeholder { color: lightgray; }"
        )
    
    def button_style(self):
        return (
            "QPushButton {"
            "    background-color: #0078D7;"
            "    border-radius: 10px;"
            "    padding: 10px;"
            "    color: white;"
            "}"
            "QPushButton:hover { background-color: #0056A3; }"
        )
    
    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if username == "admin" and password == "1234":
            print("Login bem-sucedido!")
        else:
            print("Usuário ou senha incorretos!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
