# Sorularımızı buraya yazıyoruz
sorular = [ "1.soru?",
			"2.soru?",
			"3.soru?",
			"4.soru?",
			"5.soru?",
			"6.soru?",
			"7.soru?",
			"8.soru?",
			"9.soru?",
			"10.soru?"]

# Şıklarımızı buraya yazıyoruz
siklar =  [ ["A) 1.şık", "B) 2.şık", "C) 3.şık"],
			["A) 1.şık", "B) 2.şık", "C) 3.şık"],
			["A) 1.şık", "B) 2.şık", "C) 3.şık"],
			["A) 1.şık", "B) 2.şık", "C) 3.şık"],	
			["A) 1.şık", "B) 2.şık", "C) 3.şık"],
			["A) 1.şık", "B) 2.şık", "C) 3.şık"],
			["A) 1.şık", "B) 2.şık", "C) 3.şık"],
			["A) 1.şık", "B) 2.şık", "C) 3.şık"],
			["A) 1.şık", "B) 2.şık", "C) 3.şık"],
			["A) 1.şık", "B) 2.şık", "C) 3.şık"]
			]
# Cevaplarımızı sırasıyla buraya yazıyoruz
cevaplar = ["a","b","c","a","b","c","a","b","c","a"]

# Sınavımızın puanını belirliyor her hatada 10 puan kırıyoruz.
Puan = 100

# Sınavımızın geçme puanını belirliyor
gecmePuani = 50

# Her soru sorduğumuzda tekrar tekrar aynı kodları yazmamak için
# bir fonksiyon oluşturduk

#           soracağımız soruyu ve şıklarını parametre olarak gönderiyoruz.
#           question: string tipinde   secenekler: liste tipinde olmalı
def askQuestion(question, secenekler):
	print("Çıkmak için 0'a basabilirsiniz.\n\n\n")
	print(question)
	for secenek in secenekler:
		print(secenek)
		print("\t")

#    Kullanıcının cevabını almak için kullanıyoruz. Kod tekrarı yapmamak için
#    fonksiyon oluşturduk.
def getAnswer():
	a = input("\n:")
	# kullanıcı "0" girişi yaparsa testten çıkıyor ve fonksiyon 0 çıkışı veriyor.
	if a == "0":
		return 0
	# diğer durumlarda girilen cevabı gönderiyor.
	else: 
		return a

# Programı istediğimiz durumlarda durdurabilmek için bir döngü başlattık.
while True:
	# Programı hangi nedenle durdurduğumuzu öğrenmek için kullanıyoruz
	statusCode = 0
	# Program çalışırken üzerinde çalıştığımız soru numarasını tutuyor.
	questNumber = 0
	# kullanıcının girdiği cevapları tutacağımız liste.
	userAnswers = []

	for soru in sorular:
		# Soruyu ekrana bastırıyoruz
		askQuestion(soru, siklar[questNumber])
		# Cevabı string olarak alıyoruz
		ans = str(getAnswer())
		# Adayın girebileceği tuşlamalar
		answrs = ["a","A","b","B","c","C","0"]
		# Kullanıcı 1'den fazla karakter tuşladıysa veya
		# Yanlış bir karakter tuşladıysa programı 201 hata koduyla durduruyor.
		if len(ans) > 1 or (ans not in answrs):
			statusCode = 201
			break
		# Kullanıcı "0" dan farklı bir cevap girdiyse 
		# cevabını userAnswers listesine kaydediyor
		elif ans != "0":
			userAnswers.append(ans)
		# Kullanıcı "0" girişi yaptıysa programı 101 hata koduyla durduruyor. 
		else:
			statusCode = 101
			break
		# Diğer soruya geçince üzerinde çalıştığımız soru numarasını arttırıyoruz.
		questNumber = questNumber + 1

	# 101 hata kodu alındıysa 
	if statusCode == 101:
		print("Cikis yapildi")
		break

	# 201 hata kodu alındıysa
	elif statusCode == 201:
		print("Yanlis tuslama yapildi")
		break

	# Her soruyu kontrol etmek için toplam soru sayısı kadar bir döngü başlatıyoruz.
	for i in range(10):
		# kullanıcının cevabı doğru değilse puanını 10 azaltıyoruz.
		if userAnswers[i] != cevaplar[i]:
			Puan -= 10

	# Kullanıcının sonucunu ekrana bastırıp programı bitiriyoruz.
	if Puan >= gecmePuani:
		print("Tebrikler geçtiniz.")
	else:
		print("Sınavı geçemediniz.")
	print("Aldığınız Puan: ", Puan)
	break