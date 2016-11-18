#!/usr/bin/env sh

echo "Rodando suite de testes para algoritmos de programação dinâmica"
for filename in dynamic/*.py; do
	echo "Rodando $filename..."
	python3 $filename;
	done

echo "Rodando suite de testes para algoritmos de programação gulosa"
for filename in greedy/*.py; do
	echo "Rodando $filename..."
	python3 $filename;
	done

echo "Testes concluídos"
