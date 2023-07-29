"""
Программа считывает сколько уникальных слов в тексте.
"""

text = input('Введите текст: ')
text = text.lower()
text = text.replace(".", ' ')
print(text)
text = list(text.split())
text = set(text)
print(len(text))
#Dog JucC IBI OnndsU jncLSuNJ kmiub kpi.uihi byb.nibp iubvyvuuHhh IBI Dog 