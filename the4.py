from time import time
x = time()
def query(liste,tuples):
	dic = {}
	for i in tuples:

		dic[i[0]] =i[1]
	if type(liste) == str:
		return liste
	if helper(liste,dic) :
		return query(liste[1],tuples)
	else:
		return query(liste[2],tuples)
def returner(dic,key):
	if dic.has_key(key):
		return dic[key]
	else:
		return key
def helper(liste,dic):
	if liste == []:
		return False
	elif len(liste) == 1:
		return True
	elif type(liste[0]) == list:
		liste1 = liste[0]
	else:
		liste1 = liste 
	if liste1[0] == "==":
		return returner(dic,liste1[1]) == returner(dic,liste1[2])		
	elif liste1[0] == "!=":		
		return returner(dic,liste1[1]) != returner(dic,liste1[2])
	elif liste1[0] == ">":
		return returner(dic,liste1[1]) > returner(dic,liste1[2])
	elif liste1[0] == "<":	
		return returner(dic,liste1[1]) < returner(dic,liste1[2])
	elif liste1[0] == "in":	
		return returner(dic,liste1[1]) in liste1[2]
	elif liste1[0] == "and":	
		return helper(liste1[1],dic) and helper(liste1[2],dic)	
	elif liste1[0] == "or":	
		return helper(liste1[1],dic) or helper(liste1[2],dic)
	elif liste1[0] == "not":	
		return  not helper(liste1[1],dic)

	 
decision_tree = [
["in", "TNM", [1, 2, 3]],
[["and", ["not", ["<", "Salb", 3.65]], [">", "LDH", 200]],
[["<", "Age", 71.5], "probably survive", "fiftyfifty"],
"fiftyfifty"],
[["not", ["<", "Salb", 3.85]],
[["<", "Age", 78.5],
[["not", ["<", "DiaBP", 103]],
"survive",
[["or", ["not", ["<", "BMI", 30.5]], [">", "GGT", 150]],
"probably survive",
[["not", ["<", "SysBP", 119]],
"fiftyfifty",
[["not", ["<", "BMI", 25.5]], "probably survive", "probably goner"]]]],
"mortingen st."],
[["<", "Age", 69.5], "fiftyfifty", "probably goner"]]



]


variable_value = [("TNM",4),
("Salb",3.9),
("LDH",210),
("Age",66),
("DiaBP",96),
("BMI",27.8),
("GGT",157),
("SysBP",105)
]
print query(decision_tree,variable_value)

#print query([["and",["and",[1],["or",[],[],["and",[],[1]]],[1],["<","ana",5]],["ana"],["x"],["==","ana","ada"]],"mort","cort"],[("ana",3),("ada",3)])
a = [["and",["<","xan","xam"],["not",["<","fan","fam"]],["not",[">","tan","tam"]]],[["or",["==","xan","tan"],["==","xam","fam"]],"hala","teyze"],[["in","xan",[1,2,3,4]],"anan","baban"]]
f = [("xan",2),("xam",5),("tan",3),("tam",4),("fan",20),("fam",1)]
#print query(a,f)
#print query([["in","toralp",[1,2,3,4]],"yabgu","tanyu"],[("toralp",2)])

#print query([["or",[],[1]],[["==",31,"f"],"a","b"],[["or",[],[]],"c","d"]],[("f",1)])

print time()-x
"""for i in liste1[0:]:
	if helper(liste1[i]) == False:
		return False
	else: continue
for i in liste1[0:]:
	if helper(liste1[i] :
		return True
	else: continue"""




