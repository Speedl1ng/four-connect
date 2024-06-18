from dataclasses import dataclass
from pyray import Font, get_font_default

@dataclass
class FontConfig:
    def __init__(self, font:Font = get_font_default(), font_size: float = 20, color: tuple = [0,0,0,255], spacing: int = 4 ):
        self.font = font
        self.font_size = font_size
        self.color = color
        self.spacing = spacing
    