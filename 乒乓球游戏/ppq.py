import pygame
# 初始化所有的pygame模块
pygame.init()
# 窗口宽高
width,height=900,600
# 初始画布
screen=pygame.display.set_mode((width,height))
clock=pygame.time.Clock()
# 读取图片、优化格式
ball=pygame.image.load('q.png').convert_alpha()
ball=pygame.transform.scale(ball,[80,80])
# 定义循环条件
running=True
position=ball.get_rect(x=50,y=100)
speed=[1,1]
plate=pygame.Surface([100,20])
plate.fill([0,255,0])
plate_position=plate.get_rect(x=400,y=500)

# 设置击杀数
count=0
# playing 代表游戏中
# lose 代表输了
status='playing'
# 循环
while running:
    # 循环处理接收到的事件
    # 包括键盘、鼠标、窗口等事件
    # 将画布填充黑色
    screen.fill([0, 0, 0])
    for event in pygame.event.get():
        # 如果收到退出事件
        if event.type==pygame.QUIT:
            # 结束循环
            running=False

    keys=pygame.key.get_pressed()

    # 声明字体对象
    font = pygame.font.SysFont('simhei', 36)
    text = font.render(f'击中：{count}', 1, (255, 255, 255))
    screen.blit(text, text.get_rect(x=10, y=10))

    if status=='playing':
        if keys[pygame.K_LEFT] and plate_position.left > 0:
            # 左方向键被按下
            plate_position.x -= 5
        elif keys[pygame.K_RIGHT] and plate_position.right < width:
            plate_position.x += 5

        if plate_position.colliderect(position):
            # 球拍碰到球时
            speed[1] *= -1
            count += 1
        # position.x+=speed[0]
        # position.y+=speed[1]
        position = position.move(speed)

        if position.right > width or position.left < 0:
            speed[0] *= -1
        if position.bottom > height or position.top < 0:
            speed[1] *= -1
        if position.bottom > height:
            status = 'lose'
    elif status=='lose':
        text = font.render(f'你输了', 1, (255, 255, 255))
        screen.blit(text, text.get_rect(center=screen.get_rect().center))
    # 绘制图片
    screen.blit(ball,position)
    # 绘制球拍
    screen.blit(plate,plate_position)
    # 更新屏幕
    pygame.display.update()
    clock.tick(300)