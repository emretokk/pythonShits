import re
# re.match("long string for the lookup", "second string that we searched for")
#          only looks front of the string !!!!!!!!!!
#          returns a match object if success

# re.search()    looks whole string
# re.findall()

#   METACHARACTERS

#  [ ]        aralıktaki tum karakterler

#  .          \n hariç tüm karakterler
#   	 ORNEK
#  		 .[0-9a-z]
#          Herhangi bir karakter ile başlayacak. Bu karakter sayı, harf veya başka bir karakter olabilir.
# 		   Ardından bir sayı veya alfabedeki küçük harflerden herhangi birisi gelecek.
# 		   Bu ölçütleri karşıladıktan sonra, aradığımız karakter dizisi herhangi bir karakter ile devam edebilir.

#  *    Bu metakarakter, kendinden önce gelen bir düzenli ifade kalıbını sıfır veya daha fazla sayıda eşleştirir

#  +    kendisinden önceki bir veya daha fazla sayıda tekrar eden karakterleri ayıklar. 

#  ?    eşleşme sayısının sıfır veya bir olduğu durumları kapsıyor

#  { }  bunun yardımıyla bir eşleşmeden kaç adet istediğimizi belirtebiliyoruz.
#       Küme içinde iki farklı sayı yazarak, 
#       bir karakterin en az ve en çok kaç kez tekrar etmesini istediğimizi belirtebiliriz.

#  ^    Birinci işlevi, bir karakter dizisinin en başındaki veriyi sorgulamaktır.
#       İkinci işlevi ise, “Hariç” anlamına gelmek… 
#       Bu görevini sadece “[]” metakarakterinin içinde kullanıldığı zaman yerine getirir.  

#  $    karakter dizilerinin nasıl biteceğini belirliyor.

#  |    Bu metakarakter, birden fazla düzenli ifade kalıbını birlikte eşleştirmemizi sağlar

#  ()   Bu metakarakter yardımıyla düzenli ifade kalıplarını gruplayacağız.

#  \s   boşluk karakterinin yerini tutar     \S  boşluk olmayan 

#  \d   ondalık sayıların yerini tutar	     \D  ondalık sayı olmayan

#  \w   alfanümerik karakterleri ve “_” karakterini tutar  \W olmayan

#  re.compile() metodu yardımıyla düzenli ifade kalıplarımızı kullanmadan önce 
#				derleyerek daha hızlı çalışmalarını sağlayacağız. 
#				Küçük boyutlu projelerde compile() metodu pek hissedilir bir fark yaratmasa da 
#				özellikle büyük çaplı programlarda bu metodu kullanmak oldukça faydalı olacaktır.
print(dir(re))