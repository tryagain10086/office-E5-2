import pygame

# 定义游戏的宽度和高度
WIDTH = 800
HEIGHT = 600

# 定义游戏的背景颜色
BACKGROUND_COLOR = (255, 255, 255)

# 定义游戏的角色
class Mario(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        # 加载角色的图片
        self.image = pygame.image.load("assets/mario.png")

        # 设置角色的初始位置
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 100

        # 设置角色的移动速度
        self.velocity_x = 0
        self.velocity_y = 0

    def update(self):
        # 更新角色的水平移动
        self.rect.x += self.velocity_x

        # 检测角色是否超出屏幕边界
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        elif self.rect.left < 0:
            self.rect.left = 0

        # 更新角色的垂直移动
        self.rect.y += self.velocity_y

        # 检测角色是否落地
        if self.velocity_y > 0:
            if self.rect.bottom > HEIGHT:
                self.velocity_y = 0
                self.rect.bottom = HEIGHT

    def jump(self):
        # 角色跳跃
        self.velocity_y -= 20

# 定义游戏的场景
class Scene(pygame.sprite.Group):

    def __init__(self):
        super().__init__()

        # 添加背景
        self.background = pygame.image.load("assets/background.png")
        self.background_rect = self.background.get_rect()

        # 添加角色
        self.mario = Mario()
        self.add(self.mario)

        # 添加障碍物
        self.blocks = pygame.sprite.Group()
        for i in range(0, WIDTH, 100):
            block = pygame.sprite.Sprite()
            block.image = pygame.image.load("assets/block.png")
            block.rect = block.image.get_rect()
            block.rect.x = i
            block.rect.bottom = HEIGHT - 100
            self.blocks.add(block)

    def update(self):
        # 更新场景的背景
        self.screen.blit(self.background, self.background_rect)

        # 更新角色和障碍物
        self.mario.update()
        self.blocks.update()

        # 检测角色是否与障碍物相撞
        for block in self.blocks:
            if self.mario.rect.colliderect(block.rect):
                self.mario.kill()

# 定义游戏的循环
def main():
    # 初始化Pygame
    pygame.init()

    # 创建游戏窗口
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # 创建游戏场景
    scene = Scene()

    # 开始游戏循环
    running = True
    while running:
        # 处理游戏事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    scene.mario.jump()

        # 更新游戏场景
        scene.update()

        # 显示游戏场景
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
