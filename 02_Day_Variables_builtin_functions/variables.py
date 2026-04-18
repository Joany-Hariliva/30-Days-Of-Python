#Jour 2 : 30 jours de programmation Python 
first_name="Joany Hariliva"
name_family="NJATOVOMANANA"
comple_name="NJATOVOMANANA Joany Hariliva"
country="Madagascar"
city="Antananarivo"
age=23
years=2026
is_married=False
is_true=True
is_light_on=True
name,first_name,age,country="NJATOVOMANANA","Joany Hariliva",23,"Madagascar"
#Niveau2
print(type(first_name))
print(type(name_family))
print(type(comple_name))
print(type(country))
print(type(city))
print(type(age))
print(type(years))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

len_first_name=len(first_name))
len_name_family=len(name_family))
print(len_first_name)
print(len_name_family)
if len_first_name>len_name_family:
    print("first name est plus longue que le nom de family")
elif len_first_name<len_name_family:
    print("first name est plus court que le nom de family")
else:
    print("La longeur de de name est first name est equals")

#Declaration de variable 5 et 4
num_one=5
num_two=4
var_total=num_one+num_two
var_diff=num_two-num_one
var_produit=num_two*num_one
var_div=num_one/num_two
var_ram=num_two%num_one
var_exp=num_one**num_two
floor_division=num_one//num_two

#12 RAYON D'UN CERCLE
rayon_cercle=30
aire_du_cercle=3.14*rayon_cercle**2
circum_of_circle=2*3.14*rayon_cercle

rayon_cercle=int(input("Entrer le rayon: "))
aire_du_cercle=3.14*rayon_cercle**2
circum_of_circle=2*3.14*rayon_cercle
print(aire_du_cercle)
print(circum_of_circle)

#Fonction saisie integrer
first_name=str(input("First name: "))
name_family=str(input("Family name: "))
country=str(input("Your contry: "))
age=int(input("Your age: "))
print(f"Tu es {first_name} Ton nom de famille est {name_family} tu habite a {country} et tu as {age}")





