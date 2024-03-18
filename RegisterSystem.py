import tkinter

def listingcourses ():
    coursesfile = open("Courses.txt", "r",encoding="utf8")
    f = coursesfile.readlines()
    new_window0 = Toplevel()
    for i in range(len(f)):
        label_i = Label(new_window0,bg="#CDCDB7",text=f[i],font="verdana 10 bold")
        label_i.pack()
    coursesfile.close()

def listingchosencourses():
    coursesfile = open("Courses.txt","r",encoding="utf8")
    f = coursesfile.readlines()
    new_window1 = Toplevel()
    for i in range(len(f)):
        if f[i][-2] != "0":
            label_i = Label(new_window1, bg="#CDCDB7", text=f[i], font="verdana 10 bold")
            label_i.pack()
    coursesfile.close()

def appendcourse():
    new_window6 = Toplevel()

    label_7 = Label(new_window6, bg="#CDCDB7", text="Enter the course code:", font ="verdana 10 bold")
    label_7.pack()
    entry2 = tkinter.Entry(new_window6, width=30)
    entry2.pack()

    label_8 = Label(new_window6, bg="#CDCDB7", text="Enter the course name:", font ="verdana 10 bold")
    label_8.pack()
    entry3 = tkinter.Entry(new_window6, width=30)
    entry3.pack()

    label_8 = Label(new_window6, bg="#CDCDB7", text="Enter the course instructor:", font="verdana 10 bold")
    label_8.pack()
    entry4 = tkinter.Entry(new_window6, width=30)
    entry4.pack()

    def addcourse():
        cc = str(entry2.get())
        cn = str(entry3.get())
        ins = str(entry4.get())
        coursesfile = open("Courses.txt", "a", encoding="utf8")
        coursesfile.write("{a};{b};{c};0\n".format(a=cc, b=cn, c=ins))
        coursesfile.close()
        label_8 = Label(new_window6, bg="#CDCDB7", text="You have successfully added a new course", font="verdana 10 bold")
        label_8.pack()

    add_button = Button(new_window6, text="Add course", command=addcourse)
    add_button.pack()

def searchbycoursecode():
    new_window3 = Toplevel()

    label_2 = Label(new_window3, bg="#CDCDB7", text="Enter the course code:", font ="verdana 10 bold")
    label_2.pack()
    entry5 = tkinter.Entry(new_window3, width=30)
    entry5.pack()

    def searchcourse():
        code = str(entry5.get())
        coursefile = open("Courses.txt", "r", encoding="utf8")
        f = coursefile
        x = 0
        for i in f:
            if code in i:
                x = 1
                label_3 = Label(new_window3, bg="#CDCDB7", text=i, font="verdana 10 bold")
                label_3.pack()
        if x == 0 :
            label_4 = Label(new_window3, bg="#CDCDB7", text="There is no course with that code,be careful about capslock!", font="verdana 10 bold")
            label_4.pack()
        coursefile.close()

    search_button = Button(new_window3, text="Search course", command=searchcourse)
    search_button.pack()

def searchbycoursename():
    new_window4 = Toplevel()

    label_2 = Label(new_window4, bg="#CDCDB7", text="Enter the course name:", font ="verdana 10 bold")
    label_2.pack()
    entry6 = tkinter.Entry(new_window4, width=30)
    entry6.pack()

    def searchcourse2():
        name = str(entry6.get())
        coursefile = open("Courses.txt", "r", encoding="utf8")
        f = coursefile
        x = 0
        for i in f:
            if name in i:
                x = 1
                label_3 = Label(new_window4, bg="#CDCDB7", text=i, font="verdana 10 bold")
                label_3.pack()
        if x == 0 :
            label_4 = Label(new_window4, bg="#CDCDB7", text="There is no course with that name,be careful about capslock!", font="verdana 10 bold")
            label_4.pack()

    search_button = Button(new_window4, text="Search course", command=searchcourse2)
    search_button.pack()

def registerstudent():
    new_window5 = Toplevel()

    label_2 = Label(new_window5, bg="#CDCDB7", text="Student id:", font ="verdana 10 bold")
    label_2.pack()
    entry7 = tkinter.Entry(new_window5, width=30)
    entry7.pack()

    label_3 = Label(new_window5, bg="#CDCDB7", text="Course code:", font ="verdana 10 bold")
    label_3.pack()
    entry8 = tkinter.Entry(new_window5, width=30)
    entry8.pack()

    def register():
        studentsfile = open("Students.txt", "r", encoding="utf8")
        f = studentsfile.readlines()
        studentsfile.close()
        a = str(entry7.get())
        b = str(entry8.get())
        studentsfileoverwrite = open("Students.txt", "w", encoding="utf8")
        c = 0
        for i in f:
            if a not in i:
                studentsfileoverwrite.write(i)
            else:
                c = 1
                coursesfile = open("Courses.txt", "r", encoding="utf8")
                fi = coursesfile.readlines()
                g = 0
                for d in fi:
                    if b in d:
                        g = 1
                        s = i.replace(i[-1], "")
                        studentsfileappend = open("Students.txt", "a",
                                                  encoding="utf8")
                        studentsfileappend.write("{t};{y}\n".format(t=s, y=b))
                        label_4 = Label(new_window5, bg="#CDCDB7", text="Student added to the course", font="verdana 10 bold")
                        label_4.pack()
                        coursesfileoverwrite = open("Courses.txt", "w",
                                                    encoding="utf8")
                        for h in fi:
                            if b not in h:
                                coursesfileoverwrite.write(h)
                            else:
                                j = int(h[-2])
                                j = j + 1
                                n = str(j)
                                v = h.replace(h[-2], n)
                                coursesfileappend = open("Courses.txt", "a",
                                                         encoding="utf8")
                                coursesfileappend.write("{m}".format(m=v))
                if g == 0:
                    label_5 = Label(new_window5, bg="#CDCDB7", text="There is no course with that code.", font="verdana 10 bold")
                    label_5.pack()
                    studentsfileappend = open("Students.txt", "a",
                                              encoding="utf8")
                    studentsfileappend.write("{t}\n".format(t=i))
        if c == 0:
            label_6 = Label(new_window5, bg="#CDCDB7", text="There is no student with this id.",
                            font="verdana 10 bold")
            label_6.pack()

    register_button = Button(new_window5, text="Register", command=register)
    register_button.pack()

def liststudents():
    new_window5 = Toplevel()
    studentsfile = open("Students.txt","r",encoding="utf8")
    f = studentsfile.readlines()
    for i in range(len(f)):
        label_4 = Label(new_window5, bg="#CDCDB7", text=f[i], font="verdana 10 bold")
        label_4.pack()

def top3crowdedcourses():
    new_window3 = Toplevel()
    coursesfile = open("Courses.txt","r",encoding="utf8")
    f = coursesfile.readlines()
    def number(x):
        return x[-2]
    f.sort(key = number,reverse=True)
    def sort():
        i=0
        while i<3:
            label_2 = Label(new_window3,bg="#CDCDB7",text=f[i],font="verdana 10 bold")
            label_2.pack()
            i = i+1
    sort()

def top3students():
    new_window4 = Toplevel()
    studentsfile = open("Students.txt", "r", encoding="utf8")
    f = studentsfile.readlines()
    def lenght(x):
        return len(x)
    f.sort(key = lenght,reverse=True)
    def sort():
        i=0
        while i<3:
            label_3 = Label(new_window4, bg="#CDCDB7", text=f[i], font="verdana 10 bold")
            label_3.pack()
            i = i+1
    sort()

from tkinter import *
main = Tk()
main.title("Students Register System")

canvas = Canvas(main,height=800,width=1000)
canvas.pack()

back_frame = Frame(main,bg="#8B8B83")
back_frame.place(relx=0,rely=0,relwidth=1,relheight=1)

top_frame = Frame(main,bg="#CDCDB7")
top_frame.place(relx=0.2,rely=0.02,relwidth=0.6,relheight=0.06)
label_1 = Label(top_frame,bg="#CDCDB7",text="Welcome to students register system!",font="verdana 20 bold")
label_1.pack()

left_top_frame = Frame(main,bg="#CDCDB7")
left_top_frame.place(relx=0.02,rely=0.1,relwidth=0.48,relheight=0.4)

left_bot_frame = Frame(main,bg="#CDCDB7")
left_bot_frame.place(relx=0.02,rely=0.55,relwidth=0.48,relheight=0.4)

right_frame = Frame(main,bg="#CDCDB7")
right_frame.place(relx=0.53,rely=0.1,relwidth=0.45,relheight=0.85)

listing_courses = Button(left_top_frame,text="List of all courses",command=listingcourses,height= 5, width=30)
listing_courses.place(x = 140, y = 50)

listing_chosen_courses = Button(left_top_frame,text = "List of chosen courses",command = listingchosencourses,height= 5, width=30)
listing_chosen_courses.place(x = 140, y = 180)

myvar = StringVar()
search_by_course_code = Button(left_bot_frame, text = "Search courses by course code",command = searchbycoursecode,height= 5, width=30)
search_by_course_code.place(x = 140, y = 50)

search_by_course_name = Button(left_bot_frame,text ="Search courses by course name",command = searchbycoursename,height= 5, width=30)
search_by_course_name.place(x = 140, y = 180)

append_course = Button(right_frame,text = "Add a new course", command = appendcourse,height= 5, width=30)
append_course.place(x = 130, y = 30)

register_student = Button(right_frame, text = "Register a student to a course", command = registerstudent,height= 5, width=30)
register_student.place(x = 130, y = 150)

list_students = Button(right_frame, text = "List all the students with their courses", command = liststudents,height= 5, width=30)
list_students.place(x = 130, y = 270)

top_three_crowded_courses = Button(right_frame,text = "Top three crowded courses", command = top3crowdedcourses,height= 15, width=25)
top_three_crowded_courses.place(x = 20, y = 390)

top_three_students = Button(right_frame,text = "Top three students with\n the most course registrations", command = top3students,height= 15, width=25)
top_three_students.place(x = 240, y = 390)

main.mainloop()