from csv import reader
from contextlib import redirect_stdout
from collections import namedtuple
from anytree import Node, RenderTree
from anytree.dotexport import RenderTreeGraph

Entrada = namedtuple("Entrada", "cod_geral area_geral cod_especifica area_especifica cod_detalhada area_detalhada codigo rotulo")
inicio = Node("Inicio")

with open("dataset.csv", encoding="utf-8") as csvfile:
	with open("tree.out", "w", encoding="utf-8") as f:
		with redirect_stdout(f):
			cod_geral = ""
			cod_especifica = ""
			cod_detalhada = ""
			csvfile.readline()
			for line in reader(csvfile, delimiter=";"):
				entrada = Entrada(*line)
				
				salva_1 = entrada.cod_geral + " " + entrada.area_geral
				salva_2 = entrada.cod_especifica + " " + entrada.area_especifica
				salva_3 = entrada.cod_detalhada + " " + entrada.area_detalhada
				salva_4 = entrada.codigo + " " + entrada.rotulo
				
				if salva_1 != cod_geral:
					No1 = Node(salva_1, parent = inicio)
					cod_geral = salva_1
				
				if salva_2 != cod_especifica:
					No2 = Node(salva_2, parent = No1)
					cod_especifica = salva_2
				
				if salva_3 != cod_detalhada:
					No3 = Node(salva_3, parent = No2)
					cod_detalhada = salva_3
				
				No4 = Node(salva_4, parent = No3)
				
			for pre, fill, node in RenderTree(inicio):
				 print("{} {}".format(pre, node.name))

RenderTreeGraph(inicio).to_dotfile("tree.dot")