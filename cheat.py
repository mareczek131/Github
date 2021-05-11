                            ###README###

#OK, so you are here becouse you dont want to study and your teacher do a test on webside
#Firstly, if you get an error, while you opening code, read him and follow step by step
#Secondly to get code work on you need to create a DATABASE, its simple
#just create a .txt file and paste whole text that you want to copy later
#WARNING code reads only one line of your DATABASE WARNING#
#when you have whole DATABASE only thing that you need to do is put the directory .txt file in field under ###A1###(search it in code) after "find"
#so it should look like this "os.system(f'find /i "{text}" .txt_file_directory')"

#if you followed every step please test it before exam, if something is still wrong please contact with me :D
#If code works propertly, after every ctrl + c code should search text that you copied
#and printed whole line assign to this text in terminal
#WARNING if you dont see anything try to copy text again, also dont copy polskie znaki B) WARNING#
###TIP### YOU CAN DIVIDE IN HALF WEBSIDE AND COMPILER SO YOU CAN SEE ANSWERS ###TIP###

                            ###README###



error_handler = False
error1 = False
error2 = False
try:
    from pynput import keyboard
except:
    error1 = True
    error_handler = True
import os
import time
try:
    import pyperclip
except:
    error2 = True
    error_handler = True
os.system('cls')
text = pyperclip.paste()
k = 6
while True:
    if error_handler == False:
        def on_press(key):
                text = pyperclip.paste()
                if len(format(key)) == k:
                    os.system('cls')
                    ###A1###
                    os.system(f'find /i "{text}" D:/asd/auto/asd.txt')



        def on_release(key):
            if key == keyboard.Key.esc:
                text = pyperclip.paste()
                return False

        with keyboard.Listener(
                on_press=on_press,
                on_release=on_release) as listener:
            listener.join()

        listener = keyboard.Listener(
            on_press=on_press,
            on_release=on_release)
        listener.start()
    else:
        if error1 == True:
            print("ERROR: You need to install pynput library")
            print("GO TO CMD AND ENTER: 'pip install pynput'")
            time.sleep(20)
            os.system('exit')
        if error2 == True:
            print("ERROR: You need to install pyperclip library")
            print("GO TO CMD AND ENTER: 'pip install pyperclip'")
            time.sleep(20)
            os.system('exit')
