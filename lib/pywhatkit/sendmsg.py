import pywhatkit


phone_number = input("number: ")
text = input("text: ")


pywhatkit.sendwhatmsg_instantly(f"+90{phone_number}", text)