import pygame
from pygame.locals import *
import random

pygame.init()
size = width,height = 800,600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("贪吃蛇游戏")
clock = pygame.time.Clock()
# 游戏循环标志变量
running = True
#颜色
bg_color = (200,200,200)
head_color = (255,255,255)
snake_color = (0,0,0) # 蛇身体颜色
food_color = (255,0,0)
# 定义格子的行列
ROW = 30
COL = 40
# 网格的宽度和高度
cell_width = width/COL
cell_height = height/ROW
# 实例化蛇头
class Point:
    row = 0
    col = 0
    def __init__(self,row,col):
        self.row = row
        self.col = col

    def copy(self):
        return Point(row = self.row,col = self.col)

head = Point(row = ROW/2,col = COL/2)
# 控制和移动
speed = 1
direct = 'left'
# 得分
point = 0
# 显示文字
font = pygame.font.SysFont("simhei",24)
# 蛇身体
snakes = []
# 生成食物
def create_food():
    while True:
        pos = Point(row = random.randint(0,ROW-1),col = random.randint(0,COL-1))
        # 是否撞到标志布尔值
        is_coll = False
        # 是否跟蛇碰上了
        if head.row == pos.row and head.col == pos.col:
            is_coll = True
        # 蛇的身子是否碰到食物
        for snake in snakes:
            if snake.row == pos.row and snake.col == pos.col:
                is_coll = True
                break
        if not is_coll:
            break
    return pos

food = create_food()
# 绘制网格
'''
def draw_grid():
    # 绘制行
    for r in range(ROW):
        pygame.draw.line(screen,(0,200,100),(0,r * cell_height),
                         (width,r * cell_height))
    # 绘制列
    for c in range(COL):
        pygame.draw.line(screen,(0,200,100),(c * cell_width,0),
                         (c * cell_width,height))
'''
#绘制蛇
def draw_rect(point,color):
    left = point.col * cell_width
    top = point.row * cell_height
    # 绘制
    pygame.draw.rect(screen,color,(left,top,cell_width,cell_height))

while running:
    for snake in snakes:
        if snake.row == head.row and snake.col == head.col:
                running = False
                break
    if head.row > 600 or head.row < 0 or head.col > 800 or head.col < 0:
        running = False
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == K_a:
                if direct == 'up' or direct == 'down':
                    direct = 'left'
            elif event.key == K_RIGHT or event.key == K_d:
                if direct == 'up' or direct == 'down':
                    direct = 'right'
            elif event.key == K_UP or event.key == K_w:
                if direct == 'left' or direct == 'right':
                    direct = 'up'
            elif event.key == K_DOWN or event.key == K_s:
                if direct == 'left' or direct == 'right':
                    direct = 'down'
            elif event.key == K_ESCAPE:
                running = False
    # 吃东西
    eat = (head.row == food.row and head.col == food.col)

    if eat:
        food  = create_food()
        point += 1

    # 处理蛇的身体
    snakes.insert(0,head.copy())

    if not eat:
        snakes.pop()
    # 移动
    if direct == 'left':
        head.col -= speed
    elif direct == 'right':
        head.col += speed
    elif direct == 'up':
        head.row -= speed
    elif direct == 'down':
        head.row += speed
            
    # 背景色填充    
    screen.fill(bg_color)
    # 显示得分
    l_snakes = len(snakes)
    
    score_text = " 得分：" + str(point)
    score = font.render(score_text,True,(0,0,0))
    score_rect = score.get_rect()
    score_rect.centerx = screen.get_rect().centerx
    score_rect.y = 10
    screen.blit(score,score_rect)
    # 绘制蛇头
    draw_rect(head,head_color)
    # 绘制蛇的身体
    for snake in snakes:
        draw_rect(snake,snake_color)

    # 生成食物  
    draw_rect(food,food_color)
    # 绘制网格
    # draw_grid()
    pygame.display.flip() # 刷新屏幕
    # 帧速率
    clock.tick(10)

pygame.quit()
print(score_text)