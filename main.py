import pygame


def body():
    pygame.init()
    display_width = 1280
    display_height = 720
    clock_fps = pygame.time.Clock()

    screen = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("ПрофТест")
    surface1 = pygame.Surface((700, 300))
    FPS = 30

    background_load = pygame.image.load("vetka_minimalizm_chb_125024_1600x1200.jpg")
    bg_1 = background_load.convert_alpha()
    background = pygame.transform.smoothscale(bg_1, screen.get_size())

    background_load = pygame.image.load("kabeli_provoda_podsvetka_130357_1920x1080.jpg")
    bg_1 = background_load.convert_alpha()
    background2 = pygame.transform.smoothscale(bg_1, screen.get_size())

    f1 = pygame.font.Font(None, 36)
    f2 = pygame.font.Font(None, 30)
    f3 = pygame.font.Font(None, 45)
    text_next = f1.render('Далее', True, (180, 0, 0))
    text_back = f1.render('Назад', True, (180, 0, 0))
    text_list = f1.render("Осталось вопросов", True, (180, 0, 0))
    text_answer = f1.render("Ваш ответ", True, (180, 0, 0))
    text_check = f1.render("Ответить", True, (180, 0, 0))

    def list_questions_text(i):
        text_ost = f1.render(f"{i}", True, (180, 0, 0))
        screen.blit(text_ost, (950, 160))

    def count_lines(filename, chunk_size=1 << 13):
        with open(filename, encoding="UTF8", errors="ignor") as file:
            return sum(chunk.count('\n')
                       for chunk in iter(lambda: file.read(chunk_size), ''))

    def read_q(i):
        with open("questions.txt", "r", encoding="UTF8", errors="ignor") as f:
            text = f.readlines()
            try:
                return text[i - 1].strip()
            except:
                print("Error")

    def read_q_i(i):
        with open("infa.txt", "r", encoding="UTF8", errors="ignor") as f:
            text = f.readlines()
            try:
                return text[i - 1].strip()
            except:
                print("Error")

    def draw_question(number):
        text_question = f2.render(read_q(number), True, (180, 0, 0))
        surface1.fill((255, 191, 0))
        surface1.blit(text_question, (100, 100))
        screen.blit(surface1, (100, 100))

    def check():
        if "-" == Button.questions_list_answer[Button.count - 1]:
            if str(input_1.text).strip() == str(read_q(Button.count + 1)).strip():
                print("OK")
                Button.TF = True
                Button.score += 1
                Button.questions_list_answer[Button.count - 1] = "+"
            else:
                Button.TF = False
        else:
            Button.TF = "+"
            print("Вы уже ответили на этот вопрос")

    def score(i):
        text_score = f2.render(f"Ваш счет: {i}", True, (180, 0, 0))
        screen.blit(text_score, (100, 50))

    def l_q():

        for i in range(count_lines("questions.txt")):
            Button.questions_list_answer.append("-")
        print(Button.questions_list_answer)

    def test_func(i):
        result = f1.render(f"{i}", True, (180, 0, 0))
        screen.blit(result, (1090, 330))

    def an_is_FT():
        if Button.TF == True:
            test_func("Ok")
        elif Button.TF == False:
            test_func("Error")
        elif Button.TF == "+":
            test_func("Уже ответили")

    def draw_FT_answer():
        x = 350
        y = 30
        GREEN = (50, 180, 30)
        RED = (180, 40, 15)
        count = 1
        for i in Button.questions_list_answer:
            if count % 2 == 1:
                if i == "+":
                    pygame.draw.rect(screen, RED, (x, y, 50, 50), 3)
                    pygame.draw.rect(screen, GREEN, (x+3, y+3, 44, 44), 0)
                elif i == "-":
                    pygame.draw.rect(screen, RED, (x, y, 50, 50), 3)
                x += 50
            count += 1

    def blit_t():
        l = int(count_lines("questions.txt") / 2 - Button.score)
        if l == 0:
            pygame.draw.rect(screen, (20, 170, 20), (280, 180, 700, 300), 0)
            text_win = f1.render("Вы успешно прошли тест", True, (180, 10, 90))
            screen.blit(text_win, (450, 300))

    class Button:
        def __init__(self, width, height, name="default"):
            self.name = name
            self.width = width
            self.height = height
            self.activ_color = (255, 220, 115)
            self.inactiv_color = (255, 207, 64)

        TF = None
        count = 1
        score = 0
        questions_list_answer = []
        now_s = 'menu'

        def draw(self, x, y):
            global count, question_n
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            #draw_question(self.count)
            #list_questions_text(int(count_lines("questions.txt") / 2 - Button.score))
            if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
                pygame.draw.rect(screen, self.activ_color, (x, y, self.width, self.height))
                if click[0] == 1:
                    pygame.time.delay(150)
                    print("pressed", Button.count)
                    if self.name == "next":
                        Button.TF = None
                        if Button.count + 2 <= int(count_lines("questions.txt")):
                            Button.count += 2
                            input_1.text = ""
                        else:
                            print("что то не так")
                        print(Button.count)

                    elif self.name == "back":
                        Button.TF = None
                        if Button.count - 2 < 0:
                            print("что то не так")
                        else:
                            Button.count -= 2
                        print(Button.count)

                    elif self.name == "answer":
                        Button.TF = None
                        print("answer", input_1.text)
                        check()
                    elif self.name == 'beg':
                        Button.now_s = 'test'


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

    def test():
        # screen.fill((166, 124, 0))
        # surface1.fill((255, 191, 0))
        # screen.blit(surface1, (100,  100))
        screen.blit(background, (0, 0))

        button_next.draw(1080, 620)
        button_back.draw(50, 620)
        button_cheek.draw(850, 400)
        screen.blit(text_list, (850, 100))
        screen.blit(text_next, (1110, 635))
        screen.blit(text_back, (85, 635))
        screen.blit(text_answer, (850, 250))
        screen.blit(text_check, (895, 415))
        input_1.draw(screen)
        score(Button.score)
        an_is_FT()
        draw_FT_answer()
        blit_t()
        draw_question(Button.count)
        list_questions_text(int(count_lines("questions.txt") / 2 - Button.score))

    button_beg = Button(250, 50, 'beg')
    button_donat = Button(180, 50, 'donat')


    def menu():
        screen.blit(background2, (0, 0))

        text_beg = f3.render('Начать тест', True, (180, 0, 0))
        text_donat = f3.render('Донат', True, (180, 0, 0))

        button_beg.draw(900, 350)
        button_donat.draw(970, 450)

        screen.blit(text_beg, (935, 360))
        screen.blit(text_donat, (1005, 460))

        pygame.draw.rect(screen, (102, 178, 178), (100, 100, 600, 500))
        pygame.draw.rect(screen, (120, 145, 190), (105, 105, 590, 490))

        y = 150
        text = []
        print(count_lines('infa.txt'))
        for i in range(1, count_lines('infa.txt') + 1):
            text.append(f2.render(f'{read_q_i(i)}', True, (180, 0, 0)))

        for i in text:
            screen.blit(i, (150, y))
            y += 50





    l_q()
    while True:
        clock_fps.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            input_1.handle_event(event)

        input_1.update()

        if Button.now_s == 'menu':
            menu()
        elif Button.now_s == 'test':
            test()

        pygame.display.update()

if __name__ == '__main__':
    body()