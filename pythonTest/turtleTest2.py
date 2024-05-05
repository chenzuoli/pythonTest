# 1.导入模块
import time
# 2022-12-10   20221210
from threading import Thread


def run(x: float, y: float, r: float, color: str):
    """
    画圆
    """
    import turtle

    # 2.设置线宽
    turtle.width(10)
    turtle.color(color)
    turtle.goto(x, y)
    turtle.circle(r)


t1 = Thread(target=run(0, 0, 50, 'green'))
t1.setDaemon(True)

t2 = Thread(target=run(120, 0, 50, 'blue'))
t2.setDaemon(True)

t3 = Thread(target=run(240, 0, 50, 'black'))
t3.setDaemon(True)

t4 = Thread(target=run(60, -50, 50, 'red'))
t4.setDaemon(True)

t5 = Thread(target=run(180, -50, 50, 'yellow'))
t5.setDaemon(True)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

time.sleep(100)
