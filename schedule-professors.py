n_Course = int(input("tedad doroos ra vared kon: "))

#تعریف متغییر
ar_Course = []
NProfessors = []
Year_Of_Enteries = []
NameOfCources=[]

Cou = ["nam dars","kod ostad dars","sal voroodi dars"]

print(*"-"*30+"\n\n")
for i in range(1,n_Course+1):
    row1 = [] 
    row2 = []
    row3 = []    
    for j in range(3):
        tes=str(i)
        element = str(input(Cou[j]+ " "+ tes + " ra vared kon: "))
        if (j == 0):
            row1.append(element+"(1)")
            row2.append(element+"(2)")
            row3.append(element+"(3)")
        else:
            row1.append(element)
            row2.append(element)    
            row3.append(element)
        print("-"*30+"\n")
    print(*"-"*30+"\n\n")   
    ar_Course.append(row1) 
    ar_Course.append(row2)
    ar_Course.append(row3)    


#پیدا کردن نام اساتید یا سال های ورودی غیر تکراری
def Find_Function(Cource_Multiplied_By_Three,ar_Course,Result,X_Number):

    for i in range(Cource_Multiplied_By_Three):
        element = ar_Course[i][X_Number]
        if(Result.count(element) == 0):
            Result.append(element)
    return Result

#دریافت روزهای حضور اساتید در یک هفته
def Input_Days(NProfessors):
    RangeOfDays = []
    for i in NProfessors:
        element = input("lotfan roozhaye hafteh ostad "+ i +" ra vered konid: ")
        if(element=="all"):
            RangeOfDays.append([1,2,3,4,5]) 
            continue
        else:    
            row = element.split(" ")
            row = list(set(row))
            row = list(map(int, row))
            row.sort()
            RangeOfDays.append(row)
    return RangeOfDays

#دریافت ساعت های حضور اساتید در روز های متفاوت
def Input_Hours(NProfessors,RangeOfDays):
    hour = []
    for i in range(len(NProfessors)):
        hours = []
        for j in RangeOfDays[i]:
            jj = str(j)
            element = input("lotfan saathaye rooze "+ jj +" ostad "+ NProfessors[i] +" ra vered konid: ")
            if(element=="All"):
                for i in RangeOfDays:
                    hours.append(["8","10","14","16"])  
                break   
            elif(element=="all"):
                hours.append(["8","10","14","16"]) 
                continue
            else:  
                row = element.split(" ")
                row = list(set(row))
                row = list(map(int, row))
                row.sort()
                hours.append(row)
        hour.append(hours)
    return hour+hour        

# دروس اساتید یا ورودی های متفاوت را جدا میکند
def Lesson_Separator_Builder(ar_Course, NProfessors,x):
    result = []
    for row in ar_Course:
        if row[x] == NProfessors:
            result.append(row[0])
    return result

#تابع جدا کننده دروس اساتید  و جدا کننده دروس ورودی های متفاوت
def Course_Separator(ar_Course, List, Array_Number,X_Number):
    for i in List:
        Array_Number.append(Lesson_Separator_Builder(ar_Course, i, X_Number))
    return Array_Number

# پیدا کردن نام دروس
def Find_Name_Of_Courses(ar_Course, NameOfCources):
    for i in ar_Course:
            if(NameOfCources.count(NameOfCources)==0):
                NameOfCources.append(i[0])
    return NameOfCources

#ساخت جدول درستی به تعداد اساتید
def CreateTruthTable(n):
    table = []
    for i in range(2**n):
        row = []
        for j in range(n):
            row.append((i // 2**j) % 2)
        table.append(row[::-1])
    return table
#نصف کردن جدول درستی
def CreateHalfTruthTable(lst):
    table = CreateTruthTable(lst)
    n = len(table)
    half_table = table[:n//2]
    return half_table

#تبدیل دامنه از یک هفته به دو هفته        
def Convert_Domain_To_2_Week(arr):
    result = []
    for row in arr:
        row_result = row.copy()
        for i in row:
            row_result.append(i+7)
        result.append(row_result)
    return result


#ساخت دامنه روز ها در دو هفته
def MakingARangeOfDaysInTwoWeeks(domains,NProfessors,ar_Course,doros):
    newdomain = []
    counteri = int(0)
    sw = int(0)

    for i in ar_Course:
        for j in range(len(NProfessors)):
            if (i[1] == NProfessors[j]):
                if doros[j] == 0:
                    if(counteri == 0 or counteri == 1):
                        counteri +=1
                        roww = []
                        for k in range(len(domains[j])//2):
                            roww.append(domains[j][k])
                        newdomain.append(roww)    
                    elif counteri==2:
                        counteri = 0
                        roww = []
                        for k in range((len(domains[j])//2),len(domains[j])):
                            roww.append(domains[j][k])
                        newdomain.append(roww)
                elif doros[j] == 1:
                    
                    if(counteri == 0):
                        counteri +=1
                        roww = []
                        for k in range(len(domains[j])//2):
                            roww.append(domains[j][k])
                        newdomain.append(roww)    
                    elif (counteri == 1 or  counteri==2):
                        if counteri==2:
                            counteri = 0
                        elif counteri==1:
                            counteri +=1 
                        roww = []
                        for k in range((len(domains[j])//2),len(domains[j])):
                            roww.append(domains[j][k])
                        newdomain.append(roww)   
    return newdomain

def cartesian_pro(array1,array2):
    result = []
    for a, b in zip(array1, array2):
        for x in b:
            result.append(f"{a}-{x}")
    return result   
def Build_A_Table_Domain(ar_Course,NProfessors,domains,hour):
    TableDomain = []
    for i in range(len(ar_Course)):
        for j in range(len(NProfessors)):
            row = []
            if ar_Course[i][1] == NProfessors[j]:
                row = cartesian_pro(domains[i],hour[j])
                break
        TableDomain.append(row)
    return TableDomain

def Build_CSP_Tree(nodes, edges):
    matrix = [[0 for _ in range(len(nodes))] for _ in range(len(nodes))]
    node_dict = {node: i for i, node in enumerate(nodes)}
    for connection in edges:
        for i, node in enumerate(connection):
            for j in range(i+1, len(connection)):
                matrix[node_dict[node]][node_dict[connection[j]]] = 1
                matrix[node_dict[connection[j]]][node_dict[node]] = 1
    return matrix

def Or_List(arr1, arr2):
    result = []
    for i in range(len(arr1)):
        sub_result = []
        for j in range(len(arr1[i])):
            sub_result.append(arr1[i][j] or arr2[i][j])
        result.append(sub_result)
    return result

# تعریف تابع برای بررسی قابلیت انتساب رنگ به یک راس
def Is_Consistent(graph, node, color, assignment):
    for i in range(len(graph)):
        if graph[node][i] == 1 and color == assignment[i]:
            return False
    return True
# تعریف تابع برای حذف رنگ‌های غیر مجاز از دامنه‌ها
def Forward_Check(graph, node, TableDomain, assignment):
    for c in TableDomain[node]:
        if not Is_Consistent(graph, node, c, assignment):
            TableDomain[node].remove(c)
    return TableDomain
# تعریف تابع اصلی برای حل مسئله CSP با استفاده از الگوریتم Forward Checking
def CSP_Forward_Checking(graph, TableDomain, n, assignment):
    if n == len(graph):
        return True, assignment

    node = n
    for c in TableDomain[node]:
        if Is_Consistent(graph, node, c, assignment):
            assignment[node] = c
            new_TableDomain = Forward_Check(graph, node, TableDomain.copy(), assignment)
            if [] in new_TableDomain:
                continue
            result, solution = CSP_Forward_Checking(graph, new_TableDomain, n + 1, assignment)
            if result:
                return True, solution
            assignment[node] = None

    return False, []

def Create_Html(ar_Course,solution,NameOfCources,schedulename):
    # تعریف یک جدول خالی به اندازه مورد نیاز
    index = ["#", "شنبه", "یکشنبه", "دوشنبه", "سه شنبه", "چهارشنبه", "پنجشنبه", "جمعه" , "شنبه", "یکشنبه", "دوشنبه", "سه شنبه", "چهارشنبه", "پنجشنبه", "جمعه"]
    columns = ["#", "8:00", "10:00","12:00", "14:00", "16:00", "18:00"]
    schedule = [["" for j in range(len(columns))] for i in range(len(index))]

    schedule[0] = columns

    for i in range(len(index)):
        schedule[i][0] = index[i]


    # پر کردن جدول با درس‌های مربوطه
    for i, subject in enumerate(NameOfCources):
        day, hour = map(int, solution[i].split("-"))
        hour_columns = columns.index(f"{hour}:00")
        code = "-1"
        for i in ar_Course:
            if i[0] == subject:
                code = i[1]
                break
        if (schedule[day][hour_columns]):
            schedule[day][hour_columns] = schedule[day][hour_columns]+"<br /><br />"+subject +" کد استاد: "+ code
        else:
            schedule[day][hour_columns] = subject +" کد استاد: "+ code   

    # نمایش جدول در یک فایل HTML
    #ساخت هدر HTML
    html = "<!doctype html><html><head><title>Untitled Document</title>"
    html += "<link rel='stylesheet' href='https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css' integrity='sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm' crossorigin='anonymous'>"
    html += "</head><body style='direction: rtl;'>"
    html += "<div style='text-align: center;' class='container'><table class='table table-bordered table-striped table-hover'>"


    #پر کردن جدول
    for row in schedule:
        html += "<tr>"
        for col in row:
            if row == schedule[0]:
                html += "<th>{}</th>".format(col)
            elif col == row[0]:
                html += "<th>{}</th>".format(col)    
            else:
                html += "<td>{}</td>".format(col)
        html += "</tr>"
    html += "</table></div>"
    html +="</body></html><br/><br/><hr/>"
    try:
        with open(schedulename, "w", encoding="utf-8") as f:
            f.write(html)
            print("File created successfully!")
    except Exception as e:
        print("Error occurred: ", e)  

def testii(ar_Course,NProfessors,domains,hour,NameOfCources,array1,array2,schedulename):    
    # اجرای تابع اصلی و نمایش نتیجه
    TableDomain = Build_A_Table_Domain(ar_Course,NProfessors,domains,hour)

    graph1 = Build_CSP_Tree(NameOfCources,array1)
    graph2 = Build_CSP_Tree(NameOfCources,array2)
    graph = Or_List(graph1, graph2)

    assignment = [None] * len(graph)
    result, solution = CSP_Forward_Checking(graph, TableDomain, 0, assignment)
    if result:
        Create_Html(ar_Course,solution,NameOfCources,schedulename)
        
    else:
        print("No Solution Found!")


#سه برابر کردن تعداد دروس زیرا یک درس در دو هفته سه بار ارایه میشود
Cource_Multiplied_By_Three = n_Course*3
# پیدا کردن کد اساتید غیر تکراری
NProfessors = Find_Function(Cource_Multiplied_By_Three,ar_Course,NProfessors,1)
#دریافت روزهای حضور اساتید در یک هفته
RangeOfDays = Input_Days(NProfessors)
#دریافت ساعت های حضور اساتید در روز های متفاوت
hour = Input_Hours(NProfessors,RangeOfDays)
# جدا کردن دروس استاید متفاوت
array1 = []
array1 = Course_Separator(ar_Course, NProfessors, array1,1) 
# پیدا کردن سال های ورودی غیر تکراری
Year_Of_Enteries = Find_Function(Cource_Multiplied_By_Three,ar_Course,Year_Of_Enteries,2)
array2 = []
# جدا کردن دروس ورودی های متفاوت
array2 = Course_Separator(ar_Course, Year_Of_Enteries, array2,2) 
# پیدا کردن نام دروس
NameOfCources = Find_Name_Of_Courses(ar_Course, NameOfCources)
#پیدا کردن ماکزیمم مقدار بین تعداد اساتید و تعداد ورودی ها تا با استفاده از آن جدول درستیمان را بسازیم
variables = max (len(NProfessors),len(Year_Of_Enteries))
#ساخت جدول درستی
Result_CHTT = (CreateHalfTruthTable(variables))
#تبدیل دامنه روز ها از یک هفته به دو هفته   
domains = Convert_Domain_To_2_Week(RangeOfDays)
#ساخت حالت های مختلف روز ها در دو هفته با استفاده از جدول درستی
DifferentModes_MARODITW = []
for i in range(len(Result_CHTT)):
    DifferentModes_MARODITW.append(MakingARangeOfDaysInTwoWeeks (domains,NProfessors,ar_Course,Result_CHTT[i]))

for i in range(len(DifferentModes_MARODITW)):
    print(DifferentModes_MARODITW)
    schedulename = "schedule"+str(i+1)+".html"
    testii(ar_Course,NProfessors,DifferentModes_MARODITW[i],hour,NameOfCources,array1,array2,schedulename)