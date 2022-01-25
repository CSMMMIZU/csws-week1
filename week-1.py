from tkinter import TRUE


li=['Andrew','Alif','Harry','Ryan','Wheezy','Kevan']
print(li[0])
print(li[1])
print(li[2])
print(li[3])
print(li[4])
print(li[5])
n=len(li)
print(n)
print(f'{li[0].lower(),"Go back Man"}, "{li[2].upper()}"!"Dont Worry"')
place=['CoxsBazar','Kashmir','Mount Averaste','Narikel Jingira','Nayagra']
place.sort(reverse=TRUE)
print(place)
print(len(place))
place.append('Switzarland')
print(place)
place.remove('Switzarland')
print(place)
place.reverse()
print(place)
place.remove(place[3])
print(place)
