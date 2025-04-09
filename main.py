pip install PyQt5

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect
from PyQt5.QtGui import QPainter, QColor, QBrush
import sys

class DynamicIsland(QWidget):
    def __init__(self):
        super().__init__()
        self.expanded = True  # Başlangıçta geniş durumda
        self.dark_mode = True
        self.is_playing = True
        self.initUI()

    def initUI(self):
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(400, 60)
        self.move_to_top_center()

        # Müzik bilgisi
        self.label = QLabel("🎵 Lo-fi Chill Beats", self)
        self.label.setStyleSheet("color: white; font-size: 16px;")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setGeometry(100, 15, 200, 30)

        # Play / Pause butonu
        self.play_btn = QPushButton("⏸", self)
        self.play_btn.setGeometry(320, 18, 30, 25)
        self.play_btn.setStyleSheet("background: transparent; color: white; border: none; font-size: 18px;")
        self.play_btn.clicked.connect(self.toggle_play)

        # Tema butonu
        self.theme_btn = QPushButton("☀️", self)
        self.theme_btn.setGeometry(50, 18, 30, 25)
        self.theme_btn.setStyleSheet("background: transparent; color: white; border: none; font-size: 18px;")
        self.theme_btn.clicked.connect(self.toggle_theme)

        self.show()

    def toggle_play(self):
        self.is_playing = not self.is_playing
        self.play_btn.setText("▶️" if not self.is_playing else "⏸")
        self.label.setText("🎵 Paused" if not self.is_playing else "🎵 Lo-fi Chill Beats")

    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        self.theme_btn.setText("🌙" if self.dark_mode else "☀️")
        self.update()

    def move_to_top_center(self):
        screen = QApplication.primaryScreen().geometry()
        x = (screen.width() - self.width()) // 2
        y = 40  # Kamera altına sabitle
        self.move(x, y)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        brush = QBrush(QColor(0, 0, 0, 220) if self.dark_mode else QColor(255, 255, 255, 220))
        painter.setBrush(brush)
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(self.rect(), 30, 30)  # Daha yumuşak köşeler

if __name__ == '__main__':
    app = QApplication(sys.argv)
    island = DynamicIsland()
    sys.exit(app.exec_())
