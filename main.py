from threading import Thread
import time

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class Perceptron():
    def __init__(self, learning_rate, deadline, iterations):
        self.learning_rate = learning_rate
        self.deadline = deadline
        self.iterations = iterations
        self.weights = self.train(learning_rate, deadline, iterations)

    def predict(self, dot, weights, P):
        sum = 0
        for i in range(len(dot)):
            sum += weights[i] * dot[i]
        return 1 if sum > P else 0

    def train(self, learning_rate, deadline, iterations):
        threshold = 4
        data = [(0, 6), (1, 5), (3, 3), (2, 4)]
        n = len(data[0])
        weights = [0.001, -0.004]
        outputs = [0, 0, 0, 1]

        start = time.time()
        for i in range(iterations):
            total_error = 0
            for i in range(len(outputs)):
                prediction = self.predict(data[i], weights, threshold)
                error = outputs[i] - prediction
                total_error += error
                for j in range(n):
                    delta = learning_rate * data[i][j] * error
                    weights[j] += delta
            if total_error == 0 or time.time() - start > deadline:
                break
        return ['w1 = ' + str(weights[0]), 'w2 = ' + str(weights[1])]


class MyButton1(Button):
    def on_press(self, *args):
        Thread(target=self.worker).start()

    def worker(self):

        start = time.time()

        try:
            n = int(App.get_running_app().ti1.text)
        except:
            n = 39746930799
            App.get_running_app().ti1.text = str(n)
        i = 2
        results = []
        while i * i <= n:
            while n % i == 0:
                results.append(i)
                n = n / i
            i = i + 1
        if n > 1:
            results.append(round(n))

        res = 'Results = '
        for i in results:
            res += str(i) + ', '

        res = res[:-2]

        finish = time.time() - start

        App.get_running_app().lb1.text = res
        App.get_running_app().lb1_1.text += str(finish)


class MyButton2(Button):
    def on_press(self, *args):
        Thread(target=self.worker).start()

    def worker(self):
        start = time.time()
        try:
            learning_rate = float(App.get_running_app().ti2.text)
            deadline = float(App.get_running_app().ti3.text)
            iterations = int(App.get_running_app().ti4.text)
        except:
            learning_rate = 0.1
            deadline = 5
            iterations = 500
            App.get_running_app().ti2.text = str(learning_rate)
            App.get_running_app().ti3.text = str(deadline)
            App.get_running_app().ti4.text = str(iterations)
        perceptron = Perceptron(learning_rate, deadline, iterations)

        finish = time.time() - start

        App.get_running_app().lb2.text = perceptron.weights[0] + ', ' + perceptron.weights[1]
        App.get_running_app().lb2_1.text += str(finish)


class MainApp(App):
    # Lab 3.1
    ti1 = TextInput(text="Input here number for factorization")
    lb1 = Label(text="Hello! Its Lab#3.1. Results will be here.")
    lb1_1 = Label(text='Calc time = ')
    bt1 = MyButton1(text="Calculate")
    res = 'empty'
    # Lab 3.2
    lb2 = Label(text="Hello! Its Lab#3.2. Weights will be here.")
    lb2_1 = Label(text='Calc time = ')
    ti2 = TextInput(text="Input here learning rate")
    ti3 = TextInput(text="Input here deadline in seconds")
    ti4 = TextInput(text="Input here number of iterations")
    bt2 = MyButton2(text="Calculate")

    def build(self):
        bl1 = BoxLayout(orientation='vertical')

        bl1_1 = BoxLayout(padding=20, spacing=20)

        bl1_1_1 = BoxLayout(spacing=20, orientation='vertical')
        bl1_1_1.add_widget(self.lb1)
        bl1_1_1.add_widget(self.lb1_1)

        bl1_1.add_widget(bl1_1_1)
        bl1_1.add_widget(self.ti1)
        bl1_1.add_widget(self.bt1)

        bl1_2 = BoxLayout(padding=20, spacing=20)

        bl1_2_1 = BoxLayout(spacing=20, orientation='vertical')
        bl1_2_1.add_widget(self.lb2)
        bl1_2_1.add_widget(self.lb2_1)

        bl1_2.add_widget(bl1_2_1)

        bl1_2_2 = BoxLayout(spacing=20, orientation='vertical')
        bl1_2_2.add_widget(self.ti2)
        bl1_2_2.add_widget(self.ti3)
        bl1_2_2.add_widget(self.ti4)

        bl1_2.add_widget(bl1_2_2)
        bl1_2.add_widget(self.bt2)

        bl1.add_widget(bl1_1)
        bl1.add_widget(bl1_2)

        return bl1


if __name__ == '__main__':
    MainApp().run()
