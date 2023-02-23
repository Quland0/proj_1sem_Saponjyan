# Из исходного текстового файла (pazzl.html) выбрать все html-коды изображений.
# Посчитать их количество.
import re

pazzle = open('pazzl.html').read()
imgs = re.compile(r"<img.*?>")

print(f"Кол-во изображений: {len(imgs.findall(pazzle))}")