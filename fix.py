
"""
f = open("stats.txt", "r")
conts = f.read().split("\n")
f.close()

str = conts[183]
conts.pop(183)
new_str = str.split()
obj = ""
for i in new_str:
    try:
        float(i)
        try:
            int(i)
            obj += i + " " 
        except ValueError:
            obj += i + " " 
            conts.append(obj)
            obj = ""
    except ValueError:
        obj += i + " " 

f = open("tmp.txt", "w")
writestr = "\n".join(conts)
f.write(writestr)
f.close()
"""
"""
f = open("tmp2.txt", "r")
conts = f.read().split("\n")
f.close()

new = []

for i in conts:
    tmp_list = i.split(" ")
    
    while True:
        try:
            int(tmp_list[2])
            break
        except ValueError:
            tmp_list[1] += " " + tmp_list[2]
            tmp_list.pop(2)

    tmp_list[1] = "'" + tmp_list[1] + "'"
    length = len(tmp_list)
    
    tmp_list[length - 1] = "'" + tmp_list[length - 1] + "'"    
    
    if tmp_list[length - 2] in types:
        tmp_list[length - 2] = "'" + tmp_list[length - 2] + "'" 
        i = ", ".join(tmp_list)
        i = "insert into pokemon values(" + i + ", NULL, NULL, NULL);"
    else:
        i = ", ".join(tmp_list)
        i = "insert into pokemon values(" + i + ", NULL, NULL, NULL, NULL);"    
    
    new.append(i)

f = open("tmp.txt", "w")
writestr = "\n".join(new)
f.write(writestr)
f.close()
"""

"""
f = open("moves.txt")
conts = f.read().split("\n")
f.close()

count = 0
results = [0, 1]

while True:
    try:
        tmp = conts[count]
        tmp1 = conts[count + 1]
        tmp_list = tmp.split(" ")
        tmp_list1 = tmp1.split(" ")
        
        try:
            n1 = int(tmp_list[0])
            n2 = int(tmp_list1[0])
            n3 = n2 - n1
           
            if n3 not in results:
                conts[count] += " " + conts[count + 1]
                conts.pop(count + 1)
            
        except ValueError:
            conts[count] += " " + conts[count + 1]
            conts.pop(count + 1)
            
        count += 1
    except IndexError:
        break

f = open("tmp3.txt", "w")
writestr = "\n".join(conts)
f.write(writestr)
f.close()
"""

"""
f = open("types.txt")
conts = f.read().split("\n")
f.close()

num_stats = 7
new = []

for i in conts:
    l = i.split(" ")
    num_items = len(l)
    type_index = num_items - num_stats - 1
    
    # check for second type
    print(l[type_index])
    if l[type_index - 1] in types:
        type1 = l[type_index - 1]
        type2 = l[type_index]
        l.pop(type_index - 1)
        l.pop(type_index - 1)
        l.append(type1)
        l.append(type2)
    else:
        type1 = l[type_index]
        l.pop(type_index)
        l.append(type1)
    
    new.append(" ".join(l))
    
        
f = open("tmp2.txt", "w")
writestr = "\n".join(new)
f.write(writestr)
f.close()
"""
"""
f = open("ability.txt", "r")
conts = f.read()
f.close()

for i in range(371, 638):
    mystr = "[" + str(i) + "]"
    conts = conts.replace(mystr, "")

f = open("tmp4.txt", "w")
f.write(conts)
f.close()
"""

"""
f = open("ability.txt", "r")
conts = f.read().split("\n")
f.close()

new_list = []

for i in conts:
    tmp_list = i.split(" ")
    length = len(tmp_list)
    
    tmp_list.pop(length - 1)
    
    #if tmp_list[length - 5] == "???":
     #   tmp_list[length - 5] = "NULL"
    
    new_list.append(" ".join(tmp_list))

f = open("tmp4.txt", "w")
f.write("\n".join(new_list))
f.close()
"""
"""
f = open("moves.txt", "r")
conts = f.read().split("\n")
f.close()

new_list = []

for i in conts:
    tmp_list = i.split(" ")
    length = len(tmp_list)
    
    if tmp_list[length - 1] == "—":
        tmp_list[length - 1] == "NULL"
    if tmp_list[length - 2] == "—":
        tmp_list[length - 2] == "NULL"
    
    if tmp_list[length - 4] != "NULL":
        tmp_list[length - 4] = "'" + tmp_list[length - 4] + "'"
    tmp_list[length - 5] = "'" + tmp_list[length - 5] + "'"
    tmp_list[length - 6] = "'" + tmp_list[length - 6] + "'"
    
    for j in range(2, length - 6):
        tmp_list[1] += " " + tmp_list[2]
        tmp_list.pop(2)
    
    tmp_list[1] = "'" + tmp_list[1] + "'"
    
    new_list.append("insert into move values(" + ", ".join(tmp_list) + ");")

f = open("tmp3.txt", "w")
f.write("\n".join(new_list))
f.close()
"""

"""
f = open("ability.txt", "r")
conts = f.read().split("\n")
f.close()

count = 1

while True:
    try:
        tmp_list = conts[count].split(" ")
        try:
            int(tmp_list[0])
            count += 1
        except ValueError:
            conts[count - 1] += " " + conts[count]
            conts.pop(count)
    except IndexError:
        break

f = open("tmp4.txt", "w")
f.write("\n".join(conts))
f.close()
"""
"""
f = open("ability.txt", "r")
conts = f.read().split("\n")
f.close()

for i in range(0, len(conts)):
    tmp = conts[i].split(' ')
    tmp[0] += ';'
    conts[i] = ' '.join(tmp)
    tmp = conts[i].split(';')
    tmp[0].strip(';')
    tmp[1].strip(';')
    tmp[1] = tmp[1].lstrip()
    tmp[2] = tmp[2].lstrip()
    print(tmp)
    conts[i] = 'insert into ability values(' + tmp[0] + ', "' + tmp[1] + '", "' + tmp[2] + '");'
    print(conts[i])


f = open("tmp.txt", "w")
f.write("\n".join(conts))
f.close()


f = open("tmp6.txt", "r")
conts = f.read().split("\n")
f.close()

for i in range(0, len(conts)):
    tmp = conts[i].split(' ')
    print(tmp)
    conts[i] = ' '.join(tmp[1:])

f = open("tmp6.txt", "w")
f.write("\n".join(conts))
f.close()
"""

types = ["Fire", "Water", "Ice", "Electric", "Psychic", "Poison", "Ghost", "Bug", "Grass",
         "Dragon", "Steel", "Ground", "Fighting", "Rock", "Fairy", "Dark", "Normal", "Flying"]

"""
f = open("tmp2.txt", "r")
conts = f.read().split("\n")
f.close()

new_conts = []
for i in range(0, len(conts)):
    temp = conts[i].split(' ')
    newdict = {
        "name": "hello",
        "types": "hello",
        "stats": "hello",
    }
    st_index = 0
    
    for j in range(0, len(temp)):
        try:
            int(temp[j])
            st_index = j
            break
        except:
            pass
    
    newdict["name"] = temp[:st_index]
    newdict["stats"] = temp[st_index:st_index + 7]
    newdict["types"] = temp[st_index+7:]
         
      
    new_conts.append(newdict)

text = ""
for i in new_conts:
    text += str(i) + "\n"
print(text)

f = open("tmp8.txt", "w")
f.write(text)
f.close()
"""
"""
def func(ability_conts):
    new_conts = []
    for i in range(0, len(ability_conts)):
        temp = ability_conts[i].split(" ")
        newdict = {
            "name": "hello",
            "types": "hello",
            "abilities": "hello",
        }
        t_index = 0
        d_type = False
        for j in range(0, len(temp)):
            if temp[j] in types:
                t_index = j
                if temp[j + 1] in types:
                    d_type = True
                elif temp[j + 1] == 'Rider':
                    t_index = j + 2
                    d_type = True
                elif temp[j + 1] == 'Forme' or temp[j + 1] == 'Face':
                    t_index = j + 2
                break
                
        newdict["name"] = temp[:t_index]
        if d_type:
            newdict["types"] = temp[t_index:t_index + 2]
            newdict["abilities"] = temp[t_index + 2:]
        else:
            newdict["types"] = temp[t_index:t_index + 1]
            newdict["abilities"] = temp[t_index + 1:]  
        
        new_conts.append(newdict)
    return new_conts

f = open("tmp8.txt", "r")
poke_conts = f.read().strip('\n').split("\n")
f.close()

f = open("tmp4.txt", "r")
ability_conts = f.read().strip('\n').split("\n")
f.close()


new_conts = func(ability_conts)




paste = []

matches = 0
for i in range(0, max(len(new_conts), len(poke_conts))):
    try:
        tmp = eval(poke_conts[i])
        if tmp["name"] == new_conts[i]["name"]:
            tmp["abilities"] = new_conts[i]["abilities"]
            matches += 1
        else:
            print(tmp["name"], new_conts[i]["name"])
        paste.append(str(tmp))
    except IndexError:
        pass


f = open("tmp9.txt", "w")
f.write("\n".join(paste))
f.close()
"""

f = open("tmp9.txt", "r")
conts = f.read().split("\n")
f.close()

count = 0
for i in conts:
    tmp = eval(i)
    if len(tmp["abilities"]) >= 4:
        count += 1
        print(tmp)
        
print(count)