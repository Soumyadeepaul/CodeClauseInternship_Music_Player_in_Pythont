#importing tkinter for gui
import tkinter as tk
#import mixer for music managment
from pygame import mixer
from tkinter import filedialog
import os
#create a window
window=tk.Tk()
#set title
window.title('Play Your Favourites')
#size
window.geometry("920x750")
#background
window.configure(bg='white')
#Disable resizeable
window.resizable(False,False)
#initiate mixer
mixer.init()

#banner at top
Top_Image = tk.PhotoImage(file=r"E:\codeclause\Music_Player\top.png")
tk.Label(window, image=Top_Image, bg="#0f1a2b").pack()

#tab icon
window.iconphoto(False,Top_Image)

#opening folder and adding music to the listitems
def Add_Music():
    path=filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs=os.listdir(path)
        for song in songs:
            if song.endswith('.mp3'):
                Playlist.insert(tk.END,song)
#play the music
def Play_Music():
    global Music_Name
    Music_Name = Playlist.get(tk.ACTIVE)

    #to show which music has been played
    result_label.config(
        text=f"Playing: {Music_Name[0:-4]}",
        fg='red', bg='white',font=('Arial',30))

    mixer.music.load(Music_Name)
    mixer.music.play()

#play the next music
def Next_Music():
    Music_Name = Playlist.get(tk.ACTIVE)
    listbox=Playlist.get(0,tk.END)
    current_pos=listbox.index(Music_Name)
    #if next music is present
    if current_pos+1<len(listbox):
        new_pos=current_pos+1
        Playlist.activate(new_pos)
        Music_name=Playlist.selection_set(tk.ACTIVE)
        Music_Name = Playlist.get(tk.ACTIVE)

        result_label.config(
            text=f"Playing: {Music_Name[0:-4]}",
            fg='red', bg='white',font=('Arial',30))

        mixer.music.load(Music_Name)
        mixer.music.play()

#move to previous music
def Previous_Music():
    Music_Name = Playlist.get(tk.ACTIVE)
    listbox=Playlist.get(0,tk.END)
    current_pos=listbox.index(Music_Name)
    #if previous music present
    if current_pos-1>-1:
        new_pos=current_pos-1
        Playlist.activate(new_pos)
        Music_name=Playlist.selection_set(tk.ACTIVE)
        Music_Name = Playlist.get(tk.ACTIVE)

        if len(Music_Name[0:-4])>20:
            show_name=Music_Name[0:16]+'...'
        else:
            show_name = Music_Name[0:-4]
        result_label.config(
            text=f"Playing: {show_name}",
            fg='red', bg='white',font=('Arial',30))

        mixer.music.load(Music_Name)
        mixer.music.play()
#pause
def pause():
    Music_Name = Playlist.get(tk.ACTIVE)
    if len(Music_Name[0:-4]) > 20:
        show_name = Music_Name[0:16] + '...'
    else:
        show_name = Music_Name[0:-4]
    result_label.config(
        text=f"Paused: {show_name}",
        fg='black', bg='yellow', font=('Arial', 30))
    mixer.music.pause()
#resume
def resume():
    Music_Name = Playlist.get(tk.ACTIVE)
    if len(Music_Name[0:-4]) > 20:
        show_name = Music_Name[0:16] + '...'
    else:
        show_name = Music_Name[0:-4]
    result_label.config(
        text=f"Playing: {show_name}",
        fg='red', bg='white', font=('Arial', 30))
    mixer.music.unpause()


#the music getting played
result_label = tk.Label(window, text="Don't wait...It's waiting...",bg='white',fg='blue', font=('Arial', 30))
result_label.place(x=230,y=240)

#play button
Button_Play=tk.PhotoImage(file=r'E:\codeclause\Music_Player\play.png')
tk.Button(window,image=Button_Play,bg='yellow',bd=0,command=Play_Music).place(x=410,y=340)

#resume button
Button_Resume=tk.PhotoImage(file=r'E:\codeclause\Music_Player\resume.png')
tk.Button(window,image=Button_Resume,bg='yellow',bd=0,command=resume).place(x=357,y=380)

#pause button
Button_Pause = tk.PhotoImage(file=r'E:\codeclause\Music_Player\play1.png')
tk.Button(window, image=Button_Pause, bg='yellow', bd=0, command=pause).place(x=478,y=380)

#previous button
Button_Previous=tk.PhotoImage(file=r'E:\codeclause\Music_Player\previous.png')
tk.Button(window,image=Button_Previous,bg='yellow',bd=0,command=Previous_Music).place(x=300,y=340)

#next button
Button_Next=tk.PhotoImage(file=r'E:\codeclause\Music_Player\next.png')
tk.Button(window,image=Button_Next,bg='yellow',bd=0,command=Next_Music).place(x=530,y=340)


#add music tag
add_music = tk.Label(window, text="ADD MUSIC",bg='white')
add_music.place(x=50,y=470)

#add music button
Button_Add=tk.PhotoImage(file=r'E:\codeclause\Music_Player\add.png')
tk.Button(window,image=Button_Add,bg='yellow',bd=0,command=Add_Music).place(x=10, y=460)

#creating a frame
Frame_Music = tk.Frame(window, bd=2, relief=tk.RIDGE)
Frame_Music.place(x=0, y=500, width=920, height=380)

#scroller
Scroll = tk.Scrollbar(Frame_Music)

#list box
Playlist = tk.Listbox(Frame_Music, width=910, font=("Times new roman", 10), bg="#333333", fg="grey",
                   selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
#scroller configuration
Scroll.config(command=Playlist.yview)
Scroll.pack(side=tk.RIGHT, fill=tk.Y)
Playlist.pack(side=tk.LEFT, fill=tk.BOTH)

#end of window
window.mainloop()



