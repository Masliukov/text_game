import pygame
import webbrowser
import sys


def body():
    pygame.init()
    display_width = 1280
    display_height = 720
    clock_fps = pygame.time.Clock()

    screen = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("ПрофТест")
    surface1 = pygame.Surface((700, 300))
    FPS = 30

    background_load = pygame.image.load("1625573764_13-kartinkin-com-p-fon-minimalizm-programmirovanie-krasivie-f-13.png")
    bg_1 = background_load.convert_alpha()
    background = pygame.transform.smoothscale(bg_1, screen.get_size())

    background_load = pygame.image.load("1625573749_17-kartinkin-com-p-fon-minimalizm-programmirovanie-krasivie-f-17.png")
    bg_1 = background_load.convert_alpha()
    background2 = pygame.transform.smoothscale(bg_1, screen.get_size())

    background_load = pygame.image.load("1625573753_4-kartinkin-com-p-fon-minimalizm-programmirovanie-krasivie-f-4.jpg")
    bg_1 = background_load.convert_alpha()
    background3 = pygame.transform.smoothscale(bg_1, screen.get_size())

    icon_back = pygame.image.load("icons8-стрелка-влево-в-круге-64.png")
    icon_mozg = pygame.image.load('icons8-мозги-32.png')
    icon_cofee = pygame.image.load('icons8-логотип-java-coffee-cup-33.png')
    icon_info = pygame.image.load('icons8-информация-32(1).png')
    icon_test = pygame.image.load('icons8-тест-32.png')
    icon_github = pygame.image.load('icons8-квадрат-github-50.png')
    icon_github_m = pygame.image.load('icons8-github-100.png')
    icon_pdf = pygame.image.load('icons8-pdf-100.png')
    icon_eth = pygame.image.load('icons8-ethereum-100.png')
    icon_bit = pygame.image.load('icons8-биткоин-100.png')
    qr_bit = pygame.image.load('bit.png')
    qr_eth = pygame.image.load('eth.png')


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

    def read_q(i, file='questions.txt'):
        with open(file, "r", encoding="UTF8", errors="ignor") as f:
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
                pygame.draw.rect(screen, (230, 190, 35), (x, y, self.width, self.height), 1)

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
                    elif self.name == 'infa':
                        Button.now_s = 'infa'
                    elif self.name == 'link':
                        webbrowser.open('https://github.com/Masliukov/text_game', new=2)
                    elif self.name == 'donat':
                        Button.now_s = 'donat'


            else:
                pass
                #pygame.draw.rect(screen, (230, 190, 35), (x, y, self.width, self.height), 1)
                #pygame.draw.rect(screen, self.inactiv_color, (x+5, y+5, self.width-10, self.height-10))

    class Button_child(Button):
        def draw(self, x, y):
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
                if click[0] == 1:
                    pygame.time.delay(150)
                    print("pressed", Button.count)

                    if self.name == 'exit':
                        if Button.now_s == 'menu':
                            sys.exit()
                        Button.now_s = 'menu'
                    elif self.name == 'link':
                        webbrowser.open('https://github.com/Masliukov/text_game', new=2)
                    elif self.name == 'pdf':
                        webbrowser.open('https://doc.lagout.org/operating%20system%20/linux/Nemet.pdf', new=2)

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

    button_link = Button(398, 25, 'link')
    f = 'infa.txt'
    def infa_project():
        screen.blit(background2, (0, 0))
        button_link.draw(148, 498)
        y = 150
        text = []
        pygame.draw.rect(screen, (185, 255, 210), (100, 100, 500, 500), 1)
        screen.blit(icon_github, (320, 533))
        for i in range(1, count_lines('infa.txt') + 1):
            text.append(f2.render(f'{read_q(i, f)}', True, (185, 255, 210)))

        for i in text:
            screen.blit(i, (150, y))
            y += 50


    text_eth = f1.render('0xdF4Ff18541bF13A64Ec5Ce3e3ea2e5615504B58C', True, (185, 255, 210))
    text_bit = f1.render('1Fc8vKzMnHcgtr6mXRQ572jyBNWTpjRwRk', True, (185, 255, 210))

    def donat():
        screen.blit(background3, (0, 0))
        screen.blit(icon_eth, (100, 140))
        screen.blit(text_eth, (220, 180))
        screen.blit(icon_bit, (100, 270))
        screen.blit(text_bit, (220, 310))
        screen.blit(qr_bit, (250, 470))
        screen.blit(qr_eth, (500, 470))



    button_beg = Button(290, 50, 'beg')
    button_donat = Button(345, 50, 'donat')
    button_infa = Button(170, 50, 'infa')
    button_teoria = Button(250, 50, 'teoria')

    text_beg = f3.render('Проверить знания', True, (185, 255, 210))
    text_donat = f3.render('Купить авторам кофе', True, (234, 255, 242))
    text_infa = f3.render('О проекте', True, (234, 255, 242))
    text_teoria = f3.render('Начать изучать', True, (185, 255, 210))


    button_git = Button_child(100, 100, 'link')
    button_pdf = Button_child(100, 100, 'pdf')
    def menu():
        screen.blit(background2, (0, 0))

        button_teoria.draw(80, 220)
        button_beg.draw(80, 320)
        button_donat.draw(80, 450)
        button_infa.draw(80, 550)

        screen.blit(text_beg, (90, 330))
        screen.blit(text_donat, (90, 460))
        screen.blit(text_infa, (90, 560))
        screen.blit(text_teoria, (90, 230))

        screen.blit(icon_mozg, (30, 226))
        screen.blit(icon_test, (30, 328))
        screen.blit(icon_cofee, (30, 455))
        screen.blit(icon_info, (31, 557))
        screen.blit(icon_github_m, (500, 580))
        screen.blit(icon_pdf, (650, 580))

        button_git.draw(500, 580)
        button_pdf.draw(650, 580)


    button_exit = Button_child(64, 64, 'exit')

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
        elif Button.now_s == 'infa':
            infa_project()
        elif Button.now_s == 'donat':
            donat()

        screen.blit(icon_back, (30, 30))
        button_exit.draw(30, 30)

        pygame.display.update()

if __name__ == '__main__':
    body()