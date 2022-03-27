import pygame


def body():
    pygame.init()
    display_width = 1280
    display_height = 720
    clock_fps = pygame.time.Clock()

    screen = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("MasClick")
    surface1 = pygame.Surface((700, 300))

    FPS = 30

    #background_load = pygame.image.load("mikroshema_shemy_chb_126894_1600x1200.jpg")
    #bg_1 = background_load.convert_alpha()
    #background = pygame.transform.smoothscale(bg_1, screen.get_size())

    f1 = pygame.font.Font(None, 36)
    f2 = pygame.font.Font(None, 30)
    text_next = f1.render('Далее', True, (180, 0, 0))
    text_back = f1.render('Назад', True, (180, 0, 0))
    text_list = f1.render("Осталось вопросов", True, (180, 0, 0))
    text_answer = f1.render("Ваш ответ", True, (180, 0, 0))
    text_check = f1.render("Ответить", True, (180, 0, 0))


    def read_q(i):
        with open("questions.txt", "r") as f:
            text = f.readlines()
            return text[i - 1].strip()

    def draw_question(number):
        text_question = f2.render(read_q(number), True, (180, 0, 0))
        surface1.fill((255, 191, 0))
        surface1.blit(text_question, (100, 100))
        screen.blit(surface1, (100, 100))

    def check():
        if str(input_1.text).strip() == str(read_q(Button.count + 1)).strip():
            print("OK")
            Button.score += 1

    def score(i):
        text_score = f2.render(f"Ваш счет: {i}", True, (180, 0, 0))
        screen.blit(text_score, (100, 50))



    class Button:
        def __init__(self, width, height, name="default"):
            self.name = name
            self.width = width
            self.height = height
            self.activ_color = (255, 220, 115)
            self.inactiv_color = (255, 207, 64)

        count = 1
        score = 0
        def draw(self, x, y):
            global count
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            draw_question(self.count)
            if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
                pygame.draw.rect(screen, self.activ_color, (x, y, self.width, self.height))
                if click[0] == 1:
                    pygame.time.delay(150)
                    print("pressed", Button.count)
                    if self.name == "next":
                        if Button.count + 2 <= 20:
                            Button.count += 2
                            input_1.text = ""
                        else:
                            print("что то не так")
                        print(Button.count)

                    elif self.name == "back":
                        if Button.count - 2 < 0:
                            print("что то не так")
                        else:
                            Button.count -= 2
                        print(Button.count)

                    elif self.name == "answer":
                        print("answer", input_1.text)
                        check()


            else:
                pygame.draw.rect(screen, (230, 190, 35), (x, y, self.width, self.height))
                pygame.draw.rect(screen, self.inactiv_color, (x+5, y+5, self.width-10, self.height-10))

    class InputBox:

        def __init__(self, x, y, w, h, text=''):
            self.rect = pygame.Rect(x, y, w, h)
            self.color = (122, 43, 190)
            self.text = text
            self.txt_surface = f1.render(text, True, self.color)
            self.active = False

        def handle_event(self, event):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.active = not self.active
                else:
                    self.active = False
                self.color = (47, 245, 152) if self.active else (34, 65, 200)
            if event.type == pygame.KEYDOWN:
                if self.active:
                    if event.key == pygame.K_RETURN:
                        print(self.text)
                        check()
                        self.text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    else:
                        self.text += event.unicode
                    self.txt_surface = f1.render(self.text, True, self.color)
        def update(self):
            width = max(200, self.txt_surface.get_width() + 10)
            self.rect.w = width

        def draw(self, screen):
            screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
            pygame.draw.rect(screen, self.color, self.rect, 2)

    button_next = Button(150, 60, "next")
    button_back = Button(150, 60, "back")
    button_cheek = Button(200, 60, "answer")
    input_1 = InputBox(850, 320, 100, 50)

    while True:
        clock_fps.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            input_1.handle_event(event)

        input_1.update()

        screen.fill((166, 124, 0))
        #surface1.fill((255, 191, 0))
        #screen.blit(surface1, (100,  100))
        #screen.blit(background, (0, 0))

        button_next.draw(1080, 620)
        button_back.draw(50, 620)
        button_cheek.draw(850, 400)
        screen.blit(text_list, (850, 100))
        screen.blit(text_next, (1100, 630))
        screen.blit(text_back, (70, 630))
        screen.blit(text_answer, (850, 250))
        screen.blit(text_check, (860, 410))
        input_1.draw(screen)
        score(Button.score)

        pygame.display.update()

if __name__ == '__main__':
    body()
