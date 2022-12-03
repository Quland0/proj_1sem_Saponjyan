#На трех участках выращиваются следующие сельскохозяйственные культуры: картофель,
#лук, морковь, горох, капуста, редис. Определить, какие из этих культур имеются на каждом
#участке, имеются хотя бы на одном из участков и не имеются ни на одном участке
plot1 = {"картофель","морковь","редис"}
plot2 = {"капуста","морковь","картофель"}
plot3 = {"картофель","лук","редис"}
print('сельскохозяйственная культура есть на каждом участке: ', plot1&plot2&plot3)

list1 = ["картофель", "лук", "морковь", "горох", "капуста", "редис"]

for i in list1:
    if (i in plot1) or (i in plot2) or (i in plot3):
        print(i, 'имеется на участках')

for i in list1:
    if (i not in plot1) and (i not in plot2) and (i not in plot3):
        print(i, 'не имеется на участках')