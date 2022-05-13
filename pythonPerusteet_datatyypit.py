

# Variables
a, b, c = 5, 3.2, "Hello"
print(a)
print(b)
print(c, "is type of",type(c))

# Python LIST
d = [1, 2, "jees"]
print(d, "is type of", type(d))
print(d[2], "eli otettiin listasta yksi alkio")

# Python TUPLE, jonka "hienous" on se, että se on nopeampi kuin lista, sillä sitä ei voi muuttaa luonnin jälkeen
e = (1, 2, "tuple")
print(e, "is type of", type(e)) 
print(e[0], "eli myös tuplesta voidaan ottaa yksittäisiä alkoita irti")
#e[0] = 5 # tämä aiheuttaa virheen, sillä tupleen ei voi sijoittaa uusia arvoja luonnin jälkeen.

# Python STRING
f = "Tämä on string variable"
print(f[0:5])  # Eli stringistäkin voi ottaa tietyt alkiot näin
#f[0] = "K"    # Tästä tulee virhe, sillä string muuttujaan ei voi sijoittaa uusia alkoita sen luonnin jälkeen
f = f + "  ja näin stringin perään voi lisätä tekstiä"
print(f)
g = 'Tämäkin on string variable, eli yksittäiset tai kaksittaiset lainausmerkit käy'
h = """ Tämä on sitten multiline
string"""
print(f)
print(g)
print(h)

# Python SET on näppärä joihinkin ongelmiin, ....
i = {"idle","active","semiactive","active"}
print(i, "is type of ", type(i))



# Python DICTIONARY sisältää key-value pareja. Esim nimi - puhelinnumero
j = {"john":5119222,"tom":1415096}
print(j, "is type of", type(j))
print(j.keys())
print(j.values())  # eli kun dict on luokka, niin sillä on myös metodeja.

#Python CONSTANTS
"""
Note: In reality, we don't use constants in Python. Naming them in all capital letters 
      is a convention to separate them from variables, however, it does not actually prevent reassignment.
"""
PI = 3.13
j = PI
print(PI, "is type of", type(PI))
print(j, "is type of", type(j))

#Python explicit type conversion
# Eli int(), float() ja str() funktioilla voidaan muuttaa toiseksi tyypiksi
a = "123"
b = 123
summa = int(a) + b
print(summa)


