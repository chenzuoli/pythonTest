# 1.导入模块
import time
# 2022-12-10   20221210
import turtle
from threading import Thread


class Circle(Thread):
    x: float
    y: float
    radius: float
    color: str

    def __init__(self, x: float, y: float, radius: float, color: str):
        Thread.__init__(self)
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def run(self):
        """
        画圆
        """
        # 2.设置线宽
        turtle.width(10)
        turtle.color(self.color)
        turtle.goto(self.x, self.y)
        turtle.circle(self.radius)


if __name__ == '__main__':
    circle = Circle(0, 0, 50, 'green')
    circle.setDaemon(True)
    circle.start()
    circle1 = Circle(120, 0, 50, 'blue')
    circle1.setDaemon(True)
    circle1.start()
    circle2 = Circle(240, 0, 50, 'black')
    circle2.setDaemon(True)
    circle2.start()
    circle3 = Circle(60, -50, 50, 'red')
    circle3.setDaemon(True)
    circle3.start()
    circle4 = Circle(180, -50, 50, 'yellow')
    circle4.setDaemon(True)
    circle4.start()

    time.sleep(100)
