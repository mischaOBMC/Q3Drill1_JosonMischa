from pyscript import document

def Operation(event):
    num1 = float(document.getElementById("num1").value)
    num2 = float(document.getElementById("num2").value)

    result = (num1 + num2) / 2

    document.getElementById("result").innerText = "Average: " + str(result)

    result = round(result, 2)

    if 94 <= result and result <= 100:
        level = "is Bergamo I"
    elif 87 <= result and result < 94:
        level = "is Bergamo II"
    elif result < 87 and result >= 80:
        level = "is Bergamo III"
    elif result < 80 and result >= 75:
        level = "is Perugia I"
    elif result < 75 and result >= 65:
        level = "is Perugia II"
    else:
        level = "cannot be classified"

    document.getElementById("result2").innerHTML = f"Your level {level}"


