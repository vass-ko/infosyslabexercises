a_list = [10, 12, 14, 14, 16, 28, 28, 30]
def removeDuplicates(list) :
    temp=[]
    i=0
    for item in list:           #prospelasi ths a_list
        for item1 in temp:      #prospelasi ths neas listas
            if item == item1:   #elegxos diplotypias stoixeiou 
                i=1
        if i==0:                #an den yphrxe to stoixeio ths a_list sthn temp, to prosthetw
            temp.append(item)
        i=0
        a_list = temp
    return a_list

""" 
enallaktikos tropos diagrafhs duplicate me xrhsh dictionary 
mylist = list(dict.fromkeys(a_list))
"""

def sortList(list):             #ylopoihsh bubblesort gia sortarisma ths listas
    for i in range(len(list)):
        for j in range(len(list)-1):
            if list[j]>list[j+1]:
                tmp = list[j]
                list[j]=list[j+1]
                list[j+1] = tmp
    return list