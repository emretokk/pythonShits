import os

# os.getpid()    Get process id
# os.getcwd()    Get working dir
# os.chdir()     Change dir
# os.listdir(PATH)  List dir
# os.startfile("file.txt") Executes the arg
# os.mkdir(path)     mkdir
# os.mkdirs(path)    mkdir -recursive
# os.rename(path, path)   rename a file
# os.remove(path)  deletes the file
# os.rmdir()        deletes the directory
# os.removedirs()   rmdir -recursive
# os.stat(path)        gets the info for the specified file and returns its details as an object
                # st_atime
				# dosyaya en son erişilme tarihi

				# st_ctime
				# dosyanın oluşturulma tarihi (Windows’ta)

						# GNU/Linux’ta bir dosyanın ne zaman oluşturulduğunu öğrenmek mümkün değildir.
						#  Dolayısıyla dosya.st_ctime komutu yalnızca Windows’ta bir dosyanın oluşturulma tarihi verir. 
						#  Bu komutu GNU/Linux’ta verdiğimizde elde edeceğimiz şey dosyanın son değiştirilme tarihidir.


				# st_mtime
				# dosyanın son değiştirilme tarihi

				# st_size
				# dosyanın boyutu
# os.walk(path)  -recursive ls 


for k, v in os.environ.items():
    print(k.ljust(10), v)