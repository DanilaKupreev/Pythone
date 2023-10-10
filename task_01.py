def is_palindrome(x):
    en='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    ru='АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    number='1234567890'
    a=[]
    
    for simvol in x:
        if simvol in en or simvol in ru or simvol in number:
            a.append(simvol.lower())
    
    if a[0:] == a[::-1]:
        return True

    return False
