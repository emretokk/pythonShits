print("\n \tHosgeldiniz Bu 20 Kasım 2020'den itibaren \n \tbilmedigimiz bir tarihe kadar gecerli olan \n \tsokaga cikma kisitlamanizi ogrenmeniz icin yapilmistir. \n")
print("Bu cumleyi ve kodu yazarken benim de kafam karisti yanlisimiz olursa affola :(\n\n")

a= input("Haftasonu mu? :")
a.lower()
if a.startswith("e"):
	print("Sadece 10.00-20.00 arasi sokaga cikabilirsin")
	input()
else:
	b= input("20 yas alti veya 65 yas ustu musun? :")
	b.lower()
	if b.startswith("h"):
		print("Tum gun serbest sokaga cikabilirsin iyi gunler.")
		input()
	else:
		c= input("Calisiyor musun? :")
		c.lower()
		if c.startswith("e"):
			print("Sokaga cikabilirsin kolay gelsin iyi gunler")
			input()
		else:
			d= input("20 yas alti misin? :")
			d.lower()
			if d.startswith("e"):
				print("Sadece 13.00-16.00 arasi sokaga cikabilirsin iyi gunler")
				input()
			else:
				print("Sadece 10.00-13.00 arasi sokaga cikabilirsin iyi gunler")
				input()