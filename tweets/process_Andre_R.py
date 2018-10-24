from contextlib import redirect_stdout
from re import compile
import locale 

locale.setlocale(locale.LC_ALL, "pt_Br.UTF-8")

lista = []
conjunto = {}

with open("tweets.in", encoding="utf-8") as f:
    tweets = [line.strip() for line in f.readlines()]
    tweets.sort()

regex = compile(r"RT (@\w+): .*https://.*")

for i in tweets:
	for result in regex.findall(i):
		lista.append(result)
		
conjunto = set(lista)
conjunto = sorted(conjunto, key = locale.strxfrm)
	
with open("tweets.out", "w", encoding="utf-8") as f:
    with redirect_stdout(f):
        print("\n".join(conjunto))
