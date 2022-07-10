'''
	Security Cases Control
'''

import pyAesCrypt
import os 
import sys

def decryption(file, password, delete): # Функция Дешифровки
    # задаём размер буфера
    buffer_size = 512 * 1024

    # вызываем метод расшифровки
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )

    # чтобы видеть результат выводим на печать имя зашифрованного файла
    print("[Файл '" + str(os.path.splitext(file)[0]) + "' разшифрован]")

    # удаляем исходный файл
    if delete == "y":
    	os.remove(file)

def encryption(file, password, delete): # Функция Шифровки
    # задаём размер буфера
    buffer_size = 512 * 1024

    # вызываем метод шифрования
    pyAesCrypt.encryptFile(
        str(file),
        str(file) + ".crp",
        password,
        buffer_size
    )

    # чтобы видеть результат выводим на печать имя зашифрованного файла
    print("[Файл '" + str(os.path.splitext(file)[0]) + "' зашифрован]")

    # удаляем исходный файл
    if delete == "y":
    	os.remove(file)

def scan(type_exit, dir, password, delete): # Функция Скана Директорий
    if type_exit == "decrypt":
        # перебираем все поддиректории в указанной директории
        for name in os.listdir(dir):
            path = os.path.join(dir, name)

            # если находим файл, то шифруем его
            if os.path.isfile(path):
                try:
                    decryption(path, password, delete)
                except Exception as ex:
                    print(ex)
            # если находим директорию, то повторяем цикл в поисках файлов
            else:
                scan("decode", path, password, delete)

    elif type_exit == "encrypt":
        # перебираем все поддиректории в указанной директории
        for name in os.listdir(dir):
            path = os.path.join(dir, name)

            # если находим файл, то шифруем его
            if os.path.isfile(path):
                try:
                    encryption(path, password, delete)
                except Exception as ex:
                    print(ex)
            # если находим директорию, то повторяем цикл в поисках файлов
            else:
                scan("encode", path, password, delete)

def main():
	# Logo
	print("-------------")
	print("Security Cases Control")
	print("-------------")

	while True:
		command = input(">> ").split()

		if "exit" in command:
			break

		elif "decrypt" in command: # Запуск разшифровки(decrypt, а потом пишется папка name_dir)
			password = input("Введите пароль для шифрования: ")
			delete = input("Удалять ли оригинал? - [y/n] ")
			path = command[1]

			if os.path.isfile(path):
				try:
					decryption(path, password, delete)
				except Exception as ex:
					print(ex)
			# если находим директорию, то повторяем цикл в поисках файлов
			else:
				scan("decrypt", path, password, delete)
			

		elif "encrypt" in command: # Запуск шифрования(encrypt, а потом пишется папка name_dir)
			password = input("Введите пароль для шифрования: ")
			delete = input("Удалять ли оригинал? - [y/n] ")
			path = command[1]

			if os.path.isfile(path):
				try:
					encryption(path, password, delete)
				except Exception as ex:
					print(ex)
			# если находим директорию, то повторяем цикл в поисках файлов
			else:
				scan("encrypt", path, password, delete)
main()