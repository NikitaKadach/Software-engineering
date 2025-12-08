def removka(text):
    result = ""
    skip = False

    for letter in text:
        if letter == "(":
            skip = True
        elif letter == ")":
            skip = False
        elif not skip:
            result = result + letter
    while "  " in result:
        result = result.replace("  ", " ")
    result = result.strip()

    return result
text1 = "Падал (куда он там падал) прошлогодний (значит очень старый) снег (а почему не дождь) (! (!))."

print("Вход:", text1)
print("Выход:", removka(text1))
print()
