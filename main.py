# © Copyright 2022 Тулупов Дмитрий, Маслюков Андрей
# GNU GPLv3

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
    FPS = 30

    background_load = pygame.image.load(
        "1625573764_13-kartinkin-com-p-fon-minimalizm-programmirovanie-krasivie-f-13.png")
    bg_1 = background_load.convert_alpha()
    background = pygame.transform.smoothscale(bg_1, screen.get_size())

    background_load = pygame.image.load(
        "1625573749_17-kartinkin-com-p-fon-minimalizm-programmirovanie-krasivie-f-17.png")
    bg_1 = background_load.convert_alpha()
    background2 = pygame.transform.smoothscale(bg_1, screen.get_size())

    background_load = pygame.image.load("1625573753_4-kartinkin-com-p-fon-minimalizm-programmirovanie-krasivie-f-4.jpg")
    bg_1 = background_load.convert_alpha()
    background3 = pygame.transform.smoothscale(bg_1, screen.get_size())

    background_load = pygame.image.load(
        "1625573761_20-kartinkin-com-p-fon-minimalizm-programmirovanie-krasivie-f-20.png")
    bg_1 = background_load.convert_alpha()
    background4 = pygame.transform.smoothscale(bg_1, screen.get_size())

    background_load = pygame.image.load(
        "1625573769_23-kartinkin-com-p-fon-minimalizm-programmirovanie-krasivie-f-23.jpg")
    bg_1 = background_load.convert_alpha()
    background5 = pygame.transform.smoothscale(bg_1, screen.get_size())

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
    icon_os = pygame.image.load('icons8-открытый-исходный-код-30.png')
    icon_exit = pygame.image.load('icons8-exit-60.png')
    icon_right = pygame.image.load('icons8-стрелка-вправо-в-круге-2-64.png')
    icon_left = pygame.image.load('icons8-стрелка-влево-в-круге-2-64.png')
    icon_copy = pygame.image.load('icons8-copyright-все-права-защищены-30.png')
    icon_fold = pygame.image.load('icons8-папка-32.png')

    f1 = pygame.font.Font(None, 36)
    f2 = pygame.font.Font(None, 30)
    # f25 = pygame.font.Font(None, 37)
    f3 = pygame.font.Font(None, 45)
    f4 = pygame.font.Font(None, 50)

    text_list = f1.render("Осталось вопросов", True, (234, 255, 242))
    text_answer = f1.render("Ваш ответ", True, (234, 255, 242))
    text_check = f1.render("Ответить", True, (98, 254, 169))

    def list_questions_text(i):
        text_ost = f1.render(f"{i}", True, (18, 255, 210))
        screen.blit(text_ost, (450, 100))

    def count_lines(filename, chunk_size=1 << 13):
        with open(filename, encoding="UTF8", errors="ignor") as file:
            return sum(chunk.count('\n')
                       for chunk in iter(lambda: file.read(chunk_size), ''))

    def read_q(i, file='questions.txt'):
        with open(file, "r", encoding="UTF8", errors="ignor") as fl:
            text = fl.readlines()
            try:
                return text[i - 1].strip()
            except:
                print("Error")

    def draw_question(number):
        if len(read_q(number)) > 45:
            text_question = f2.render(read_q(number), True, (185, 255, 210))
        else:
            text_question = f3.render(read_q(number), True, (185, 255, 210))
        screen.blit(text_question, (120, 235))

    def check():
        if "-" == Button.questions_list_answer[Button.count - 1]:
            if str(input_1.text).strip() == str(read_q(Button.count + 1)).strip():
                Button.TF = True
                Button.score += 1
                Button.questions_list_answer[Button.count - 1] = "+"
            else:
                Button.TF = False
        else:
            Button.TF = "+"

    def score(i):
        text_score = f1.render(f"Ваш счет: {i}", True, (234, 255, 242))
        screen.blit(text_score, (150, 50))

    def l_q():
        # Button.questions_list_answer.clear()
        for i in range(count_lines("questions.txt")):
            Button.questions_list_answer.append("-")

    def test_func(i):
        if i == 'Верно' or i == 'Уже ответили':
            result = f1.render(f"{i}", True, (98, 254, 169))
        else:
            result = f1.render(f"{i}", True, (180, 0, 0))
        screen.blit(result, (710, 390))

    def an_is_FT():
        if Button.TF == True:
            test_func("Верно")
        elif Button.TF == False:
            test_func("Не верно")
        elif Button.TF == "+":
            test_func("Уже ответили")

    def draw_FT_answer():
        x = 270
        y = 615
        GREEN = (78, 203, 135)
        RED = (254, 169, 98)
        count = 1
        c = 1
        for i in Button.questions_list_answer:
            if count % 2 == 1:
                if i == "+":
                    pygame.draw.rect(screen, RED, (x, y, 50, 50), 3)
                    pygame.draw.rect(screen, GREEN, (x + 3, y + 3, 44, 44), 0)
                elif i == "-":
                    pygame.draw.rect(screen, RED, (x, y, 50, 50), 3)
                    c = 0
                x += 53
                c += 1
            count += 1

    def blit_t():
        l = int(count_lines("questions.txt") / 2 - Button.score)
        if l == 0:
            pygame.draw.rect(screen, (20, 170, 20), (280, 180, 700, 300), 0)
            text_win = f3.render("Вы успешно прошли тест", True, (180, 10, 90))
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
        list_v = ['teoria_osnova', 'teoria_network', 'raznoe', 'otnas']

        def draw(self, x, y):
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
                pygame.draw.rect(screen, (230, 190, 35), (x, y, self.width, self.height), 1)

                if click[0] == 1:
                    pygame.time.delay(150)

                    if self.name == "answer":
                        Button.TF = None
                        check()
                    elif self.name == 'beg':
                        Button.now_s = 'test'
                    elif self.name == 'infa':
                        Button.now_s = 'infa'
                    elif self.name == 'link':
                        webbrowser.open('https://github.com/Masliukov/text_game', new=2)
                    elif self.name == 'donat':
                        Button.now_s = 'donat'
                    elif self.name == 'teoria':
                        Button.now_s = 'teoria_menu'
                    elif self.name == 'osnova':
                        Button.now_s = 'teoria_osnova'
                    elif self.name == 'network':
                        Button.now_s = 'teoria_network'
                    elif self.name == 'raznoe':
                        Button.now_s = 'raznoe'
                    elif self.name == 'otnas':
                        Button.now_s = 'otnas'
                    elif self.name == 'scripts':
                        webbrowser.open('http://www.kavserver.ru/library/shellscriptsunix.shtml', new=2)
                    elif self.name == 'file_system':
                        webbrowser.open('https://iit.cs.msu.ru/media/media/educational_materials/%D0%A1%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%BD%D0%BE%D0%B5_%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%BD%D0%BE%D0%B5_%D0%BE%D0%B1%D0%B5%D1%81%D0%BF%D0%B5%D1%87%D0%B5%D0%BD%D0%B8%D0%B5_-_%D1%84%D0%B0%D0%B9%D0%BB%D0%BE%D0%B2%D1%8B%D0%B5_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D1%8B_%D0%9E%D0%A1_Unix_zmAwX5u.pdf', new=2)
                    elif self.name == 'kernel_driver':
                        webbrowser.open('http://dmilvdv.narod.ru/Translate/LDD3/Linux_Device_Drivers_3_ru.pdf', new=2)
                    elif self.name == 'tcp_ip':
                        webbrowser.open('https://www.redbooks.ibm.com/pubs/pdfs/redbooks/gg243376.pdf', new=2)
                    elif self.name == 'marsh':
                        webbrowser.open('http://prog.tversu.ru/net/1012%20routing.pdf', new=2)
                    elif self.name == 'dns':
                        webbrowser.open('https://creewick.github.io/study/courses/inet/lectures/4dnsbook.pdf', new=2)
                    elif self.name == 'email':
                        webbrowser.open('http://rdv.rosnou.ru/IT433/it_ad_11.pdf', new=2)
                    elif self.name == 'virt':
                        webbrowser.open('http://sibnigmi.ru/documents/school/Gochakov.pdf', new=2)
                    elif self.name == 'data':
                        webbrowser.open('https://www.marvel.ru/files/1_1407479676.pdf', new=2)
                    elif self.name == 'analiz':
                        webbrowser.open('http://simulation.su/uploads/files/default/2014-serebriakova-parshina.pdf', new=2)
                    elif self.name == 'backup':
                        webbrowser.open('http://aad.tpu.ru/practice/EMC/Module%2010-adapt.pdf', new=2)

    class Button_child(Button):
        def draw(self, x, y):
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
                if click[0] == 1:
                    pygame.time.delay(150)

                    if self.name == "next":
                        Button.TF = None
                        if Button.count + 2 <= int(count_lines("questions.txt")):
                            Button.count += 2
                            input_1.text = ""
                        else:
                            pass
                    elif self.name == "back":
                        Button.TF = None
                        if Button.count - 2 < 0:
                            pass
                        else:
                            Button.count -= 2
                    elif self.name == 'exit':
                        # l_q()
                        if Button.now_s == 'menu':
                            sys.exit()
                        elif Button.now_s in Button.list_v:
                            Button.now_s = 'teoria_menu'
                        else:
                            Button.now_s = 'menu'
                    elif self.name == 'link':
                        webbrowser.open('https://github.com/Masliukov/text_game', new=2)
                    elif self.name == 'pdf':
                        webbrowser.open('https://doc.lagout.org/operating%20system%20/linux/Nemet.pdf', new=2)
            else:
                pass
                # pygame.draw.rect(screen, (230, 190, 35), (x, y, self.width, self.height), 1)

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
                self.color = (185, 255, 210) if self.active else (169, 98, 254)
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

    button_next = Button_child(58, 58, "next")
    button_back = Button_child(58, 58, "back")
    button_cheek = Button(160, 45, "answer")
    input_1 = InputBox(480, 375, 100, 50)

    def test():
        screen.blit(background, (0, 0))

        button_next.draw(1150, 610)
        button_back.draw(80, 610)
        button_cheek.draw(500, 480)

        screen.blit(text_list, (350, 50))
        screen.blit(text_answer, (320, 390))
        screen.blit(text_check, (525, 490))

        input_1.draw(screen)
        score(Button.score)
        an_is_FT()
        draw_FT_answer()
        draw_question(Button.count)
        blit_t()
        list_questions_text(int(count_lines("questions.txt") / 2 - Button.score))

        screen.blit(icon_left, (77, 607))
        screen.blit(icon_right, (1147, 607))

        screen.blit(icon_back, (30, 30))

    button_link = Button(398, 25, 'link')
    f = 'infa.txt'

    def infa_project():
        screen.blit(background2, (0, 0))
        button_link.draw(148, 498)
        y = 150
        text = []
        pygame.draw.rect(screen, (185, 255, 210), (100, 100, 500, 500), 1)
        screen.blit(icon_github, (320, 533))
        screen.blit(icon_os, (480, 143))
        for i in range(1, count_lines('infa.txt') + 1):
            text.append(f2.render(f'{read_q(i, f)}', True, (185, 255, 210)))

        for i in text:
            screen.blit(i, (150, y))
            y += 50

        screen.blit(icon_back, (30, 30))

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

        screen.blit(icon_back, (30, 30))

    button_beg = Button(290, 50, 'beg')
    button_donat = Button(345, 50, 'donat')
    button_infa = Button(170, 50, 'infa')
    button_teoria = Button(250, 50, 'teoria')

    text_beg = f3.render('Проверить знания', True, (185, 255, 210))
    text_donat = f3.render('Купить авторам кофе', True, (234, 255, 242))
    text_infa = f3.render('О проекте', True, (234, 255, 242))
    text_teoria = f3.render('Начать изучать', True, (185, 255, 210))
    text_cping = f2.render('ПрофТест 2022', True, (185, 255, 210))
    text_li = f2.render('GPLv3', True, (185, 255, 210))
    text_name1 = f4.render('Сетевое и системное', True, (234, 255, 242))
    text_name2 = f4.render('администрирование', True, (234, 255, 242))

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
        screen.blit(icon_copy, (10, 680))

        screen.blit(text_cping, (45, 685))
        screen.blit(text_li, (1200, 685))
        screen.blit(text_name1, (300, 50))
        screen.blit(text_name2, (250, 100))

        button_git.draw(500, 580)
        button_pdf.draw(650, 580)

        screen.blit(icon_exit, (30, 30))

    text_base = f3.render('Основы администрирования', True, (185, 255, 210))
    text_network = f3.render('Работа в сетях', True, (185, 255, 210))
    text_raznoe = f3.render('Разное', True, (185, 255, 210))
    text_otnas = f3.render('Дополнительный материал от нас', True, (234, 255, 242))

    text_setata1 = f2.render('Ни искусство, ни мудрость', True, (234, 255, 242))
    text_setata2 = f2.render('не могут быть достигнуты, если им не учиться.', True, (234, 255, 242))
    text_setata_autor = f2.render('Демокрит', True, (234, 255, 242))

    button_teoria_osnova = Button(455, 50, 'osnova')
    button_teoria_network = Button(240, 50, 'network')
    button_teoria_rznoe = Button(130, 50, 'raznoe')
    button_teoria_otnas = Button(525, 50, 'otnas')

    def teoria_menu():
        screen.blit(background4, (0, 0))

        screen.blit(text_base, (100, 180))
        screen.blit(text_network, (100, 280))
        screen.blit(text_raznoe, (100, 380))
        screen.blit(text_otnas, (100, 480))

        button_teoria_osnova.draw(90, 170)
        button_teoria_network.draw(90, 270)
        button_teoria_rznoe.draw(90, 370)
        button_teoria_otnas.draw(90, 470)

        screen.blit(text_setata1, (795, 70))
        screen.blit(text_setata2, (700, 100))
        screen.blit(text_setata_autor, (1070, 140))

        screen.blit(icon_fold, (40, 177))
        screen.blit(icon_fold, (40, 277))
        screen.blit(icon_fold, (40, 377))

        screen.blit(text_li, (1200, 685))
        screen.blit(icon_back, (30, 30))

    button_script_comand = Button(515, 50, 'scripts')
    text_scripts = f3.render('Сценарии и командная оболочка', True, (185, 255, 210))
    button_file_system = Button(310, 50, 'file_system')
    text_file_system = f3.render('Файловые системы', True, (185, 255, 210))
    button_kernel_driver = Button(290, 50, 'kernel_driver')
    text_kernek_driver = f3.render('Ядро и драйверы', True, (185, 255, 210))

    def teoria_osnovnoe():
        screen.blit(background5, (0, 0))

        screen.blit(text_scripts, (150, 200))
        button_script_comand.draw(140, 190)
        screen.blit(text_file_system, (150, 350))
        button_file_system.draw(140, 340)
        screen.blit(text_kernek_driver, (150, 500))
        button_kernel_driver.draw(140, 490)

        screen.blit(icon_back, (30, 30))

    button_tcp_ip = Button(180, 50, 'tcp_ip')
    button_marsh = Button(265, 50, 'marsh')
    button_dns = Button(390, 50, 'dns')
    button_email = Button(305, 50, 'email')
    text_tcp = f3.render('Сети tcp/ip', True, (185, 255, 210))
    text_marsh = f3.render('Маршрутизация', True, (185, 255, 210))
    text_dns = f3.render('Система доменных имен', True, (185, 255, 210))
    text_email = f3.render('Электронная почта', True, (185, 255, 210))

    def teoria_network():
        screen.blit(background5, (0, 0))

        screen.blit(text_tcp, (150, 180))
        screen.blit(text_marsh, (150, 300))
        screen.blit(text_dns, (150, 420))
        screen.blit(text_email, (150, 540))
        button_tcp_ip.draw(140, 170)
        button_marsh.draw(140, 290)
        button_dns.draw(140, 410)
        button_email.draw(140, 530)

        screen.blit(icon_back, (30, 30))

    button_virt = Button(255, 50, 'virt')
    button_data = Button(425, 50, 'data')
    button_analiz = Button(460, 50, 'analiz')
    button_backup = Button(380, 50, 'backup')
    text_virt = f3.render('Виртуализация', True, (185, 255, 210))
    text_data = f3.render('Центры обработки данных', True, (185, 255, 210))
    text_analiz = f3.render('Анализ производительности', True, (185, 255, 210))
    text_backup = f3.render('Резервное копирование', True, (185, 255, 210))


    def teoria_raznoe():
        screen.blit(background5, (0, 0))

        screen.blit(text_virt, (150, 180))
        screen.blit(text_data, (150, 300))
        screen.blit(text_analiz, (150, 420))
        screen.blit(text_backup, (150, 540))
        button_virt.draw(140, 170)
        button_data.draw(140, 290)
        button_analiz.draw(140, 410)
        button_backup.draw(140, 530)


        screen.blit(icon_back, (30, 30))

    def teoria_otnas():
        screen.blit(background5, (0, 0))
        screen.blit(icon_back, (30, 30))

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
        elif Button.now_s == 'teoria_menu':
            teoria_menu()
        elif Button.now_s == 'teoria_osnova':
            teoria_osnovnoe()
        elif Button.now_s == 'teoria_network':
            teoria_network()
        elif Button.now_s == 'raznoe':
            teoria_raznoe()
        elif Button.now_s == 'otnas':
            teoria_otnas()

        button_exit.draw(30, 30)

        pygame.display.update()


if __name__ == '__main__':
    body()
