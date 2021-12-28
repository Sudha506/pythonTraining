def func():
    s={"fruits":[{"name":"mango","price":60,"color":"yellow"},{"name":"apple","price":120,"color":"red"},{"name":"grapes","price":55,"color":"green"}]}
    #print(s["fruits"][1]["price"])
    return s["fruits"][1]["name"]
print(func())

def func1():
    g={"stdata":[{"name":"sudha","rnum":506,"language":"telugu"},{"name":"suni","rnum":507,"language":"english"},{"name":"lakki","rnum":508,"language":"telugu"},{"name":"niha","rnum":509,"language":"english"}]}
    print(g["stdata"][3]["rnum"])
func1()