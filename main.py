import sys
import time

import numpy as np

from gradio_client import Client
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QPixmap

from MainWindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui_main = Ui_MainWindow()
        self.ui_main.setupUi(self)

        self.img_link = ""
        self.q_num = 1
        self.ans_num = 1
        self.history = {'user': "Отвечай на русском языке"}
        self.history_text = ""

        self.main_action()

    def main_action(self):
        self.ui_main.label_2.setHidden(True)
        self.ui_main.label_3.setHidden(True)
        self.ui_main.pushButton_4.clicked.connect(lambda: self.gen())
        self.ui_main.pushButton.clicked.connect(lambda: self.begin_gen_img())
        self.ui_main.pushButton_5.clicked.connect(lambda: self.copy_image_path(self.img_link))
        self.ui_main.pushButton_2.clicked.connect(lambda: self.talking())
        self.ui_main.pushButton_3.clicked.connect(lambda: self.clearhistory())

    def clearhistory(self):
        self.history = {}
        self.history_text = ""
        self.ui_main.plainTextEdit_2.clear()
        self.q_num = 1
        self.ans_num = 1

    def talking(self):
        self.ui_main.label_3.setHidden(False)
        self.ui_main.pushButton_2.setHidden(True)
        query = str(self.ui_main.plainTextEdit_3.toPlainText())
        self.history['user_question#'+str(self.q_num)] = query
        self.q_num += 1
        print(query)
        try:
            client = Client("Qwen/Qwen2-72B-Instruct")
            joke = client.predict(
                query=self.history,
                history=[],
                system="You are a helpful assistant.",
                api_name="/model_chat"
            )
        except Exception:
            client = Client("Qwen/Qwen2-7b-instruct-demo")
            joke = client.predict(
                query=self.history,
                history=[],
                system="You are a helpful assistant.",
                api_name="/model_chat"
            )
        second_element = joke[1]
        nested_list = second_element[0]
        result = nested_list[1].strip('"')
        print(result)
        self.ui_main.plainTextEdit_3.clear()
        self.history['qwen2_answer#'+str(self.ans_num)] = result
        self.ans_num += 1
        self.history_text += "\n\nПользователь:\n" + query + '\n\nAI:\n' + result
        self.ui_main.plainTextEdit_2.clear()
        self.ui_main.plainTextEdit_2.setPlainText(str(self.history_text))
        self.ui_main.label_3.setHidden(True)
        self.ui_main.pushButton_2.setHidden(False)

    def copy_image_path(self, img_link):
        clipboard = QApplication.clipboard()
        clipboard.setImage(img_link)
        print("Путь к изображению скопирован в буфер обмена.")

    def begin_gen_img(self):
        self.ui_main.pushButton.setHidden(True)
        self.ui_main.label_2.setHidden(False)
        time.sleep(2)
        self.image_show()

    def image_show(self):
        self.ui_main.pushButton.setHidden(True)
        self.ui_main.label_2.setHidden(False)

        self.img_link = self.image_gen(str(self.ui_main.plainTextEdit.toPlainText()))
        # self.img_link = r"C:\Users\User\AppData\Local\Temp\gradio\faf241205a0fba85c0acea856741b5a78e2c4ed28353d2d6e752a9c3675a1bb3\image.webp"

        img = QPixmap(self.img_link)
        self.ui_main.label.setPixmap(img.scaled(512, 512))
        self.ui_main.lineEdit_2.setText(self.img_link)

        self.ui_main.pushButton.setHidden(False)
        self.ui_main.label_2.setHidden(True)

    def image_gen(self, prompt):
        query = "У меня есть ТЕКСТ:" + prompt + \
                 "Тебе необходимо КОРОТКО описать картинку, " \
                 "будто это основное изображение для этого ТЕКСТА. " \
                 "Ответ должет быть на АНГЛИЙСКОМ языке и МАКСИМАЛЬНОЙ ДЛИНОЙ 150 СЛОВ. " \
                 "ТОЛЬКО ОПИСАНИЕ КАРТИНКИ, УДАЛИ ВСЁ ОСТАЛЬНОЕ. Не добавляй пояснения. " \
                 "УДАЛИ ПОЯСНЕНИЕ, ОСТАВЬ ИСКЛЮЧИТЕЛЬНО ОПИСАНИЕ КАРТИНКИ"
        try:
            client = Client("Qwen/Qwen2-72B-Instruct")
            joke = client.predict(
                query=query,
                history=[],
                system="You are a middleman who takes input and creates data for the best artists.",
                api_name="/model_chat"
            )
        except Exception:
            client = Client("Qwen/Qwen2-7b-instruct-demo")
            joke = client.predict(
                query=query,
                history=[],
                system="You are a middleman who takes input and creates data for the best artists.",
                api_name="/model_chat"
            )
        second_element = joke[1]
        nested_list = second_element[0]
        text2 = nested_list[1].strip('"')
        print(text2)

        try:
            client = Client("black-forest-labs/FLUX.1-schnell")
            result = client.predict(
                prompt=text2,
                seed=0,
                randomize_seed=True,
                width=1024,
                height=1024,
                num_inference_steps=4,
                api_name="/infer"
            )
            return result[0]

        except Exception as e:
            print(e)
            try:
                client = Client("multimodalart/FLUX.1-merged")
                result = client.predict(
                    prompt=text2,
                    seed=0,
                    randomize_seed=True,
                    width=1024,
                    height=1024,
                    guidance_scale=3.5,
                    num_inference_steps=8,
                    api_name="/infer"
                )
                return result[0]

            except Exception as e:
                print(e)
                client = Client("stabilityai/stable-diffusion-3-medium")
                result = client.predict(
                    prompt=text2,
                    negative_prompt="incorrect human body shape, low quality, text",
                    seed=0,
                    randomize_seed=True,
                    width=1024,
                    height=1024,
                    guidance_scale=5,
                    num_inference_steps=28,
                    api_name="/infer"
                )
                return result[0]

    def make_pairs(self, corp):
        for i in range(len(corp) - 1):
            yield (corp[i], corp[i + 1])

    def gen(self):
        what_to_open = str(self.ui_main.lineEdit.text())
        try:
            text = open(what_to_open, encoding='utf-8').read()
            corpus = text.split()
            pairs = self.make_pairs(corpus)
            word_dict = {}
            for word_1, word_2 in pairs:
                if word_1 in word_dict.keys():
                    word_dict[word_1].append(word_2)
                else:
                    word_dict[word_1] = [word_2]
            first_word = np.random.choice(corpus)

            while first_word.islower() or first_word == '—' or first_word == '-':
                first_word = np.random.choice(corpus)
            chain = [first_word]
            n_words = int(self.ui_main.spinBox.text()) - 1
            for y in range(n_words):
                try:
                    chain.append(np.random.choice(word_dict[chain[-1]]))
                except KeyError:
                    pass
            prt = ' '.join(chain)

            self.ui_main.plainTextEdit_4.clear()
            self.ui_main.plainTextEdit_4.insertPlainText(prt)
        except FileNotFoundError:
            self.ui_main.plainTextEdit_4.clear()
            self.ui_main.plainTextEdit_4.insertPlainText('Файл не найден')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
