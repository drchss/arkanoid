import pygame

pygame.init()


back = (200, 255, 255)  # колір фону (background)
mw = pygame.display.set_mode((500, 500))  # Вікно програми (main window)
mw.fill(back)
clock = pygame.time.Clock()


# змінні, що відповідають за координати платформи
racket_x = 200
racket_y = 330

speed_x = 3
speed_y = 3

game_over = False
move_right = False
move_left = False


# клас із попереднього проекту
class Area:
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = back
        if color:
            self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

    def colliderect(self, rect):
        return self.rect.colliderect(rect)


# клас для об'єктів-картинок
class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)

    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))


# створення м'яча та платформи
ball = Picture("ball.jpg", 160, 200, 50, 50)
platform = Picture("platform.png", racket_x, racket_y, 100, 30)



# Створення ворогів
start_x = 5  # координати створення першого монстра
start_y = 5
count = 9  # кількість монстрів у верхньому ряду
monsters = []  # список для зберігання об'єктів-монстрів
for j in range(3):  # цикл по стовпцях
    y = start_y + (
        55 * j
    )  # координата монстра у кожному слід. стовпці буде зміщена на 55 пікселів по y
    x = start_x + (27.5 * j)  # і 27.5 по x
    for i in range(
        count
    ):  # цикл по рядах(рядків) створює в рядку кількість монстрів,що дорівнює count
        d = Picture("enemy.jpg", x, y, 50, 50)  # створюємо монстра
        monsters.append(d)  # додаємо до списку
        x = x + 55  # збільшуємо координату наступного монстра
    count = count - 1  # для наступного ряду зменшуємо кількість монстрів


while not game_over:
    ball.fill()
    platform.fill()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_right = True
            elif event.key == pygame.K_LEFT:
                move_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_LEFT:
                move_left = False
        if move_right:
            platform.rect.x += 3
        if move_left:
            platform.rect.x -= 3
    if ball.colliderect(platform.rect):
        speed_y *=-1
    if ball.rect.y < 0:
        speed_y *=-1
    if ball.rect.x > 450 or ball.rect.x < 0:
        speed_x *=-1
    ball.rect.x +=speed_x
    ball.rect.y +=speed_y
    # малюємо всіх монстрів зі списку
    for m in monsters:
        m.draw()

    platform.draw()
    ball.draw()

    pygame.display.update()

    clock.tick(40)