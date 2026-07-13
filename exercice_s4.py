dogs = {
        ("Chien", 12), 
        ("chat", 8), 
        ("lapin", 5), 
        ("hamster", 3), 
        ("poisson rouge", 10), 
        ("perroquet", 7), 
        ("tortue", 4), 
        ("furet", 6), 
        ("cochon d'Inde", 9), 
        ("serpent", 2)
        }
for i, (animal, age) in enumerate(dogs, 1):
    print(f"{i}. {animal} - {age} ans")

for i ,animaux in enumerate(dogs):
        print(f"{i+1}. {animaux}")

fruits = ["pomme", "banane", "cerise", "datte", "kiwi"]
for i, fruit in enumerate(fruits, 1):
    print(f"{i}. {fruit}")