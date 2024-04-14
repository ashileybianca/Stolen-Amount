
for %%f in (casoG50.txt casoG100.txt casoG200.txt casoG500.txt casoG750.txt casoG1000.txt casoG1500.txt casoG2000.txt) do (
    python stolen_amount.py .\casos_teste\%%f
)