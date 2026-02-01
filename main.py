from pyscript import document, display

subjects = ["Science", "Math", "English", "Fiipino", "ICT", "PE"]
units = [5, 5, 5, 3, 1, 1]

def calculate_GWA(e):

    Fname = document.getElementById("Fname").value
    Lname = document.getElementById("Lname").value

    Science = float(document.getElementById("Science").value or 0)
    Math = float(document.getElementById("Math").value or 0)
    English = float(document.getElementById("English").value or 0)
    Filipino = float(document.getElementById("Filipino").value or 0)
    ICT = float(document.getElementById("ICT").value or 0)
    PE = float(document.getElementById("PE").value or 0)

    totalUnits = units[0] + units[1] + units [2] + units[3] + units [4] + units [5]
    totalWeight = (Science * units[0]) + (Math * units[1]) + (English * units[2]) + (Filipino * units[3]) + (ICT * units[4]) + (PE * units[5])
    GWA = totalWeight / totalUnits

    document.getElementById("name").innerHTML = (f"Name: {Fname} {Lname}")

    document.getElementById("sci").innerHTML = (f"{subjects[0]}: {Science}")
    document.getElementById("math").innerHTML = (f"{subjects[1]}: {Math}")
    document.getElementById("english").innerHTML = (f"{subjects[2]}: {English}")
    document.getElementById("fil").innerHTML = (f"{subjects[3]}: {Filipino}")
    document.getElementById("ict").innerHTML = (f"{subjects[4]}: {ICT}")
    document.getElementById("pe").innerHTML = (f"{subjects[5]}: {PE}")


    document.getElementById("gwa").innerHTML = (f"Your GWA is {GWA:.2f}")

    if 94 <= GWA <= 100:
        level = "Bergamo I"
    elif 87 <= GWA < 94:
        level = "Bergamo II"
    elif GWA < 87 and GWA >= 80:
        level = "is Bergamo III"
    elif GWA < 80 and GWA >= 75:
        level = "is Perugia I"
    elif GWA < 75 and GWA >= 65:
        level = "is Perugia II"
    else:
        level = "cannot be classified"

    document.getElementById("grade_class").innerHTML = f"Your level {level}"
