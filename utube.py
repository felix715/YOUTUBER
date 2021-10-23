from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

Folder_Name=""
# function for the file location
def openLocation():
    global Folder_Name
    Folder_Name=filedialog.askdirectory()
    if (len(Folder_Name)>1):
        locationError.config(text=Folder_Name,fg="green")
    else:
        locationError.config(text="Please choose folder!",fg="red")
# function for downloading the video
def DownloadVideo():
    choice=ytdChoices.get()
    url=ytdEntry.get()
    if(len(url)>1):
        ytdError.config(text="")
        yt = YouTube(url)

        if(choice==Choices[0]):
            select=yt.streams.filter(progressive=True).first()
        elif(choice==[1]):
            select = yt.streams.filter(progressive=True).last()
        elif (choice == [2]):
            select = yt.streams.filter(only_audio=True).first()
        else:
            ytdError.config(text="Past the Link again kindly",fg="red")

# fucntion for dowloading the
    select.download(Folder_Name)
    ytdError.config(text="Download Completed")



root = Tk()
root.title("Youtube Downloader")
# get window size
# root.geometry("350*400")
# sets all the content into a center
root.columnconfigure(0,weight=1)
# designing the youtube link labels
ytdLabel=Label(root,text="Enter the url of the video: ",font=("jost",15))
ytdLabel.grid()

# the entry box
ytdEntryVar = StringVar()
ytdEntry = Entry(root,width=50,textvariable=ytdEntryVar)
ytdEntry.grid()
# entry message i.e the error message maybe when the user has entered invalid error
ytdError = Label(root,text="Error message",fg = "red",font=("jost",10))
ytdError.grid()


# asking the save file label
saveLabel = Label(root,text="Save the video file",font=("jost",15,"bold"))
saveLabel.grid()

# designing the button when the user wants to save the video,,,it will ask the file location

saveEntry = Button(root,width=10,bg="red",fg="white",text="Choose path",command=openLocation)
saveEntry.grid()

# error message when the user does not select the file loaction
locationError = Label(root,text="the error message of the path",fg="red",font=("jost",10))
locationError.grid()

# ask for download quality
ytdQuality =Label(root,text="select the quality",font=("jost",15))
ytdQuality.grid()

# design the options
Choices = ["720p","144p","Only Audio"]
ytdChoices = ttk.Combobox(root,values=Choices)
ytdChoices.grid()


# designing the download button
downloadbtn =Button(root,text="Download",width=10,bg="red",fg="white",command=DownloadVideo)
downloadbtn.grid()

# developer label
developerLabel = Label(root,text="Dream developers",font=("jost",15))
developerLabel.grid()

root.mainloop()