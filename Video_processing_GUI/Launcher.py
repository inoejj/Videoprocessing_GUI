import os
import time
import subprocess
import itertools
import sys
from tkinter import *
from tkinter.filedialog import askopenfilename,askdirectory
from tkinter import tix
import platform
import shutil
import datetime
from PIL import Image, ImageTk
import tkinter.ttk as ttk
from batch_process_videos import *
from tools_function import *
import warnings
import webbrowser
warnings.simplefilter(action='ignore', category=FutureWarning)

class processvid_title(Frame):
    def __init__(self,parent=None,widths="",color=None,shortenbox =None,downsambox =None,graybox=None,framebox=None,clahebox=None,**kw):
        self.color = color if color is not None else 'black'
        Frame.__init__(self,master=parent,**kw)
        self.lblName = Label(self, text= 'Video Name',fg=str(self.color),width=widths,font=("Helvetica",10,'bold'))
        self.lblName.grid(row=0,column=0)
        self.lblName2 = Label(self,width =4)
        self.lblName2.grid(row=0, column=1)
        self.lblName3 = Label(self, text='Start Time',width = 13,font=("Helvetica",10,'bold'))
        self.lblName3.grid(row=0, column=2)
        self.lblName4 = Label(self, text='End Time',width = 15,font=("Helvetica",10,'bold'))
        self.lblName4.grid(row=0, column=3)
        self.shorten = IntVar()
        self.lblName5 = Checkbutton(self,text='Select All',variable= self.shorten,command=shortenbox)
        self.lblName5.grid(row=0, column=4)
        self.lblName6 = Label(self, text='Width',width =13,font=("Helvetica",10,'bold'))
        self.lblName6.grid(row=0, column=5)
        self.lblName7 = Label(self, text='Height',width = 15,font=("Helvetica",10,'bold'))
        self.lblName7.grid(row=0, column=6)
        self.downsample = IntVar()
        self.lblName8 = Checkbutton(self,text='Select All',variable = self.downsample,command =downsambox)
        self.lblName8.grid(row=0,column=7,padx=8)
        self.grayscale = IntVar()
        self.lblName9 = Checkbutton(self,text='Select All',variable =self.grayscale,command = graybox)
        self.lblName9.grid(row=0,column=8,padx=7)
        self.frameno = IntVar()
        self.lblName10 = Checkbutton(self,text='Select All',variable = self.frameno,command = framebox)
        self.lblName10.grid(row=0,column=9,padx=6)
        self.clahe = IntVar()
        self.lblName11 = Checkbutton(self,text='Select All',variable =self.clahe,command =clahebox)
        self.lblName11.grid(row=0,column=10,padx=6)

class processvideotable(Frame):
    def __init__(self,parent=None,fileDescription="",widths = "" ,dirname ="",outputdir='',color=None,**kw):
        self.color = color if color is not None else 'black'
        self.croplist = []
        self.filename = os.path.join(dirname,fileDescription)
        self.outputdir = outputdir
        Frame.__init__(self,master=parent,**kw)
        self.lblName = Label(self, text=fileDescription,fg=str(self.color),width= widths)
        self.lblName.grid(row=0,column=0)
        self.btnFind = Button(self, text="Crop",command=self.cropvid)
        self.btnFind.grid(row=0,column=1)
        self.trimstart = Entry(self)
        self.trimstart.grid(row=0,column=2)
        self.trimend = Entry(self)
        self.trimend.grid(row=0, column=3)
        self.shortenvar = IntVar()
        self.downsamplevar = IntVar()
        self.grayscalevar = IntVar()
        self.superimposevar = IntVar()
        self.clahevar = IntVar()
        self.shortenvid = Checkbutton(self,text='Shorten',variable = self.shortenvar)
        self.shortenvid.grid(row=0,column=4)
        self.width = Entry(self)
        self.width.grid(row=0,column=5)
        self.height = Entry(self)
        self.height.grid(row=0,column=6)
        self.downsamplevid = Checkbutton(self,text='Downsample',variable = self.downsamplevar)
        self.downsamplevid.grid(row=0,column=7)
        self.grayscalevid = Checkbutton(self,text='Grayscale',variable= self.grayscalevar)
        self.grayscalevid.grid(row=0,column =8)
        self.superimposevid = Checkbutton(self,text='Add Frame #',variable =self.superimposevar)
        self.superimposevid.grid(row=0,column=9)
        self.clahevid = Checkbutton(self,text='CLAHE',variable = self.clahevar)
        self.clahevid.grid(row=0,column =10)

    def cropvid(self):
        self.croplist = []
        print(self.filename)
        command = cropvid_queue(self.filename,self.outputdir)
        self.croplist.append(command)
        self.btnFind.configure(bg='red')

    def get_crop_list(self):
        return self.croplist

    def getstarttime(self):
         return self.trimstart.get()
    def getendtime(self):
        return self.trimend.get()

    def shorten(self):
        return self.shortenvar.get()

    def downsample(self):
        return self.downsamplevar.get()
    def getwidth(self):
        return self.width.get()
    def getheight(self):
        return self.height.get()
    def grayscale(self):
        return self.grayscalevar.get()
    def addframe(self):
        return self.superimposevar.get()
    def get_clahe(self):
        return self.clahevar.get()

class processvid_menu:

    def __init__(self, videofolder, outputdir):
        self.filesFound = []
        self.row = []
        self.videofolder = videofolder
        self.outputdir = outputdir
        ########### FIND FILES ###########
        for i in os.listdir(videofolder):
            if i.endswith(('.avi','.mp4','.mov','flv')):
                self.filesFound.append(i)

        ### longest string in list
        maxname = max(self.filesFound,key=len)

        # Popup window
        vidprocessmenu = Toplevel()
        vidprocessmenu.minsize(1100, 400)
        vidprocessmenu.wm_title("Batch process video table")
        vidprocessmenu.iconbitmap('video.ico')
        scroll =Scrollable(vidprocessmenu)

        tableframe = LabelFrame(scroll)

        # table title
        self.title = processvid_title(tableframe, str(len(maxname)),shortenbox=self.selectall_shorten,downsambox=self.selectall_downsample,graybox=self.selectall_grayscale,framebox=self.selectall_addframe,clahebox=self.selectall_clahe)
        self.title.grid(row=0,sticky= W)

        #### loop for tables######
        for i in range(len(self.filesFound)):
            self.row.append(processvideotable(tableframe,str(self.filesFound[i]), str(len(maxname)),self.videofolder,self.outputdir))
            self.row[i].grid(row=i+1, sticky=W)

        but = Button(scroll,text='Execute',command =self.execute_processvideo,font=('Times',12,'bold'),fg='navy')
        but.grid(row=2)

        tableframe.grid(row=1)
        scroll.update()

    def selectall_clahe(self):
        for i in range(len(self.filesFound)):
            if self.title.clahe.get() == 1:
                self.row[i].clahevid.select()
            else:
                self.row[i].clahevid.deselect()

    def selectall_addframe(self):
        for i in range(len(self.filesFound)):
            if self.title.frameno.get()==1:
                self.row[i].superimposevid.select()
            else:
                self.row[i].superimposevid.deselect()

    def selectall_grayscale(self):

        for i in range(len(self.filesFound)):
            if self.title.grayscale.get()==1:
                self.row[i].grayscalevid.select()
            else:
                self.row[i].grayscalevid.deselect()


    def selectall_downsample(self):
        for i in range(len(self.filesFound)):
            if self.title.downsample.get()==1:
                self.row[i].downsamplevid.select()
            else:
                self.row[i].downsamplevid.deselect()


    def selectall_shorten(self):
        for i in range(len(self.filesFound)):
            if self.title.shorten.get()==1:
                self.row[i].shortenvid.select()
            else:
                self.row[i].shortenvid.deselect()

    def get_thecroplist(self):
        self.croplistt = []

        for i in range(len(self.filesFound)):
           self.croplistt.append((self.row[i].get_crop_list()))
        print(self.croplistt)
        self.croplistt = list(itertools.chain(*self.croplistt))

        return self.croplistt

    def get_shortenlist(self):
        self.shortenlistt = []
        for i in range(len(self.filesFound)):
            if (self.row[i].shorten()) == 1:
                self.shortenlistt.append(shortenvideos1_queue(self.outputdir,self.filesFound[i],self.row[i].getstarttime(),self.row[i].getendtime()))

        return self.shortenlistt

    def get_downsamplelist(self):
        self.downsamplelistt = []
        for i in range(len(self.filesFound)):
            if (self.row[i].downsample()) == 1:
                self.downsamplelistt.append(downsamplevideo_queue(self.row[i].getwidth(),self.row[i].getheight(),self.filesFound[i],self.outputdir))

        return self.downsamplelistt

    def get_grayscalelist(self):
        self.grayscalelistt = []
        for i in range(len(self.filesFound)):
            if (self.row[i].grayscale()) == 1:
                self.grayscalelistt.append(greyscale_queue(self.outputdir,self.filesFound[i]))

        return self.grayscalelistt

    def get_superimposeframelist(self):
        self.superimposeframelistt = []
        for i in range(len(self.filesFound)):
            if (self.row[i].addframe()) == 1:
                self.superimposeframelistt.append(superimposeframe_queue(self.outputdir, self.filesFound[i]))

        return self.superimposeframelistt

    def execute_processvideo(self):
        # create a temp folder in the output dir
        tmp_folder = os.path.join(self.outputdir,'tmp')
        if os.path.exists(tmp_folder):
            shutil.rmtree(tmp_folder)
        os.mkdir(tmp_folder)

        # remove process txt file if process were killed half way
        try:
            os.remove(self.outputdir + '\\' + 'process_video_define.txt')
        except:
            print('Executing...')

        # compiling the list of commands
        try:
            crop = self.get_thecroplist()
            crop = [i for i in crop if i] ###remove any none in crop
        except:
            crop = []
        try:
            shorten = self.get_shortenlist()
        except:
            shorten = []
        try:
            downsample = self.get_downsamplelist()
        except:
            downsample = []
        try:
            grayscale = self.get_grayscalelist()
        except:
            grayscale = []
        try:
            superimpose = self.get_superimposeframelist()
        except:
            superimpose = []
        ## copy video and move it to output dir
        copyvideos = []
        for i in self.filesFound:
            command = 'copy \"' + str(self.videofolder) + '\\' + str(
                os.path.basename(i)) + '\" \"' + self.outputdir + '\"'
            copyvideos.append(command)

        #compiling all the commands into list
        all_list = copyvideos + crop + shorten + downsample + grayscale + superimpose
        print(len(all_list))
        #creating text file
        filepath = self.outputdir + '\\' + 'process_video_define.txt'

        if os.path.exists(filepath):
            append_write = 'a'  # append if already exists
        else:
            append_write = 'w'  # make a new file if not
        ## writing into the txt file
        highscore = open(filepath, append_write)
        for i in all_list:
            highscore.write(i + '\n')
        highscore.close()
        ## running it using subprocess
        with open(filepath) as fp:
            for cnt, line in enumerate(fp):
                # add probably if ffmpeg then this if not then other subprocess
                subprocess.call(line, shell=True, stdout=subprocess.PIPE)
        ##clahe
        for i in range(len(self.filesFound)):
            if self.row[i].get_clahe() == 1:
                clahe_queue(self.outputdir +'\\'+ os.path.basename(self.filesFound[i]))
            else:
                print('Clahe not applied to',str(self.filesFound[i]))
        ##rename the txt file ran
        file = os.path.dirname(filepath) + '\\' + 'Processes_ran.txt'
        os.rename(filepath, file)
        dir = str(self.outputdir + '\\' + 'process_archive')
        try:
            os.makedirs(dir)
            print("Directory", dir, "created ")
        except FileExistsError:
            print("Directory", dir, "already exists")

        currentDT = datetime.datetime.now()
        currentDT = str(currentDT.month) + '_' + str(currentDT.day) + '_' + str(currentDT.year) + '_' + str(
            currentDT.hour) + 'hour' + '_' + str(currentDT.minute) + 'min' + '_' + str(currentDT.second) + 'sec'
        try:
            shutil.move(file, dir)
        except shutil.Error:
            os.rename(file, file[:-4] + str(currentDT) + '.txt')
            shutil.move(file[:-4] + str(currentDT) + '.txt', dir)

        print('Process video completed.')

class batch_processvideo:

    def __init__(self):
        self.croplist = []
        self.shortenlist = []
        self.downsamplelist =[]
        self.grayscalelist = []
        self.superimposelist = []
        # Popup window
        batchprocess = Toplevel()
        batchprocess.minsize(400, 200)
        batchprocess.wm_title("Batch process video")
        batchprocess.iconbitmap('video.ico')

        #Video Selection Tab
        label_videoselection = LabelFrame(batchprocess,text='Folder selection',font='bold',padx=5,pady=5)
        self.folder1Select = FolderSelect(label_videoselection,'Video directory:',title='Select Folder with videos')

        #output video
        self.outputfolder = FolderSelect(label_videoselection,'Output directory:',title='Select a folder for your output videos')

        #create list of all videos in the videos folder
        button_cL = Button(label_videoselection,text='Confirm',command=self.confirmtable)

        #organize
        label_videoselection.grid(row=0,sticky=W)
        self.folder1Select.grid(row=0,sticky=W)
        self.outputfolder.grid(row=1,sticky=W)
        button_cL.grid(row=2,sticky=W)

    def confirmtable(self):

        if (self.outputfolder.folder_path!='No folder selected')and(self.folder1Select.folder_path!='No folder selected'):
            try:
                processvid_menu(self.folder1Select.folder_path, self.outputfolder.folder_path)
            except:
                print('Please make sure there are videos in the folder selected')
        elif (self.outputfolder.folder_path=='No folder selected'):
            print('Please select an output folder')
        elif (self.folder1Select.folder_path == 'No folder selected'):
            print('Please select a folder with videos')
        else:
            print('Please select folder with videos and the output directory')

class FolderSelect(Frame):
    def __init__(self,parent=None,folderDescription="",color=None,title=None,**kw):
        self.title=title
        self.color = color if color is not None else 'black'
        Frame.__init__(self,master=parent,**kw)
        self.folderPath = StringVar()
        self.lblName = Label(self, text=folderDescription,fg=str(self.color))
        self.lblName.grid(row=0,column=0)
        self.entPath = Label(self, textvariable=self.folderPath,relief=SUNKEN)
        self.entPath.grid(row=0,column=1)
        self.btnFind = Button(self, text="Browse Folder",command=self.setFolderPath)
        self.btnFind.grid(row=0,column=2)
        self.folderPath.set('No folder selected')
    def setFolderPath(self):
        folder_selected = askdirectory(title=str(self.title))
        if folder_selected:
            self.folderPath.set(folder_selected)
        else:
            self.folderPath.set('No folder selected')

    @property
    def folder_path(self):
        return self.folderPath.get()

class FileSelect(Frame):
    def __init__(self,parent=None,fileDescription="",color=None,title=None,**kw):
        self.title=title
        self.color = color if color is not None else 'black'
        Frame.__init__(self,master=parent,**kw)
        self.filePath = StringVar()
        self.lblName = Label(self, text=fileDescription,fg=str(self.color))
        self.lblName.grid(row=0,column=0)
        self.entPath = Label(self, textvariable=self.filePath,relief=SUNKEN)
        self.entPath.grid(row=0,column=1)
        self.btnFind = Button(self, text="Browse File",command=self.setFilePath)
        self.btnFind.grid(row=0,column=2)
        self.filePath.set('No file selected')
    def setFilePath(self):
        file_selected = askopenfilename(title=self.title)
        if file_selected:
            self.filePath.set(file_selected)
        else:
            self.filePath.set('No file selected')
    @property
    def file_path(self):
        return self.filePath.get()

class Entry_Box(Frame):
    def __init__(self,parent=None,fileDescription="",labelwidth='',**kw):
        Frame.__init__(self,master=parent,**kw)
        self.filePath = StringVar()
        self.lblName = Label(self, text=fileDescription,width=labelwidth,anchor=W)
        self.lblName.grid(row=0,column=0)
        self.entPath = Entry(self, textvariable=self.filePath)
        self.entPath.grid(row=0,column=1)

    @property
    def entry_get(self):
        self.entPath.get()
        return self.entPath.get()

    def entry_set(self, val):
        self.filePath.set(val)


class video_downsample:

    def __init__(self):
        # Popup window
        videosdownsample = Toplevel()
        videosdownsample.minsize(200, 200)
        videosdownsample.wm_title("Downsample Video Resolution")

        # Video Path
        self.videopath1selected = FileSelect(videosdownsample, "Video path",title='Select a video file')
        label_choiceq = Label(videosdownsample, text='Choose only one of the following method to downsample videos (Custom/Default)')

        #custom reso
        label_downsamplevidcustom = LabelFrame(videosdownsample,text='Custom resolution',font='bold',padx=5,pady=5)
        # width
        self.label_width = Entry_Box(label_downsamplevidcustom,'Width','10')
        # height
        self.label_height = Entry_Box(label_downsamplevidcustom,'Height','10')
        # confirm custom resolution
        self.button_downsamplevideo1 = Button(label_downsamplevidcustom, text='Downsample to custom resolution',command=self.downsample_customreso)
        #Default reso
        # Checkbox
        label_downsampleviddefault = LabelFrame(videosdownsample,text='Default resolution',font ='bold',padx=5,pady=5)
        self.var1 = IntVar()
        self.checkbox1 = Radiobutton(label_downsampleviddefault, text="1980 x 1080", variable=self.var1,value=1)
        self.checkbox2 = Radiobutton(label_downsampleviddefault, text="1280 x 720", variable=self.var1,value=2)
        self.checkbox3 = Radiobutton(label_downsampleviddefault, text="720 x 480", variable=self.var1, value=3)
        self.checkbox4 = Radiobutton(label_downsampleviddefault, text="640 x 480", variable=self.var1, value=4)
        self.checkbox5 = Radiobutton(label_downsampleviddefault, text="320 x 240", variable=self.var1, value=5)
        # Downsample video
        self.button_downsamplevideo2 = Button(label_downsampleviddefault, text='Downsample to default resolution',command=self.downsample_defaultreso)

        # Organize the window
        self.videopath1selected.grid(row=0,sticky=W)
        label_choiceq.grid(row=1, sticky=W,pady=10)

        label_downsamplevidcustom.grid(row=2,sticky=W,pady=10)
        self.label_width.grid(row=0, column=0,sticky=W)
        self.label_height.grid(row=1, column=0,sticky=W)
        self.button_downsamplevideo1.grid(row=3)

        label_downsampleviddefault.grid(row=3,sticky=W,pady=10)
        self.checkbox1.grid(row=0,stick=W)
        self.checkbox2.grid(row=1,sticky=W)
        self.checkbox3.grid(row=2, sticky=W)
        self.checkbox4.grid(row=3, sticky=W)
        self.checkbox5.grid(row=4, sticky=W)
        self.button_downsamplevideo2.grid(row=5)

    def downsample_customreso(self):
        self.width1 = self.label_width.entry_get
        self.height1 = self.label_height.entry_get

        ds = downsamplevideo(self.width1, self.height1, self.videopath1selected.file_path)

    def downsample_defaultreso(self):

        if self.var1.get()==1:
            self.width2 = str(1980)
            self.height2 = str(1080)
            print('The width selected is ' + str(self.width2) + ', the height is ' + str(self.height2))

        elif self.var1.get()==2:
            self.width2 = str(1280)
            self.height2 = str(720)
            print('The width selected is ' + str(self.width2) + ', the height is ' + str(self.height2))

        elif self.var1.get()==3:
            self.width2 = str(720)
            self.height2 = str(480)
            print('The width selected is ' + str(self.width2) + ', the height is ' + str(self.height2))

        elif self.var1.get()==4:
            self.width2 = str(640)
            self.height2 = str(480)
            print('The width selected is ' + str(self.width2) + ', the height is ' + str(self.height2))

        elif self.var1.get()==5:
            self.width2 = str(320)
            self.height2 = str(240)
            print('The width selected is ' + str(self.width2) + ', the height is ' + str(self.height2))

        ds = downsamplevideo(self.width2, self.height2, self.videopath1selected.file_path)

class Red_light_Convertion:

    def __init__(self):
        # Popup window
        redlightconversion = Toplevel()
        redlightconversion.minsize(200, 200)
        redlightconversion.wm_title("CLAHE")

        #CLAHE
        label_clahe = LabelFrame(redlightconversion,text='Contrast Limited Adaptive Histogram Equalization',font='bold',padx=5,pady=5)
        # Video Path
        self.videopath1selected = FileSelect(label_clahe, "Video path ",title='Select a video file')
        button_clahe = Button(label_clahe,text='Apply CLAHE',command=lambda:clahe(self.videopath1selected.file_path))

        #organize the window
        label_clahe.grid(row=0,sticky=W)
        self.videopath1selected.grid(row=0,sticky=W)
        button_clahe.grid(row=1,pady=5)

class crop_video:

    def __init__(self):
        # Popup window
        cropvideo = Toplevel()
        cropvideo.minsize(200, 200)
        cropvideo.wm_title("Crop Video")

        # Video Path
        label_cropvideo = LabelFrame(cropvideo,text='Crop Video',font='bold',padx=5,pady=5)
        self.videopath1selected = FileSelect(label_cropvideo,"Video path",title='Select a video file')
        # CropVideo
        button_cropvid = Button(label_cropvideo, text='Crop Video', command=lambda:cropvid(self.videopath1selected.file_path))

        #organize
        label_cropvideo.grid(row=0,sticky=W)
        self.videopath1selected.grid(row=0,sticky=W)
        button_cropvid.grid(row=1,sticky=W,pady=10)
# class aboutgui:
#
#     def __init__(self):
#         about = Toplevel()
#         about.minsize(200, 200)
#         about.wm_title("About")
#         about.iconbitmap('about.ico')
#         aboutgui.iconbitmap('about.ico')
#
#         canvas = Canvas(about,width=551,height=268,bg='black')
#         canvas.pack()
#
#         img = PhotoImage(file='about.png')
#         canvas.create_image(0,0,image=img,anchor='nw')
#         canvas.image = img
class shorten_video:

    def __init__(self):
        # Popup window
        shortenvid = Toplevel()
        shortenvid.minsize(200, 200)
        shortenvid.wm_title("Clip video")

        # videopath
        self.videopath1selected = FileSelect(shortenvid, "Video path",title='Select a video file')

        #timeframe for start and end cut
        label_cutvideomethod1 = LabelFrame(shortenvid,text='Method 1',font='bold',padx=5,pady=5)
        label_timeframe = Label(label_cutvideomethod1, text='Please enter the time frame in hh:mm:ss format')
        self.label_starttime = Entry_Box(label_cutvideomethod1,'Start at:','8')
        self.label_endtime = Entry_Box(label_cutvideomethod1, 'End at:',8)
        CreateToolTip(label_cutvideomethod1,
                      'Method 1 will retrieve the specified time input.(eg: input of Start at: 00:00:00, End at: 00:01:00, will create a new video from the chosen video from the very start till it reaches the first minute of the video)')

        #express time frame
        label_cutvideomethod2 = LabelFrame(shortenvid,text='Method 2',font='bold',padx=5,pady=5)
        label_method2 = Label(label_cutvideomethod2,text='Method 2 will retrieve from the end of the video.(eg: an input of 3 seconds will get rid of the first 3 seconds of the video)')
        # self.var_express = IntVar()
        # checkbox_express = Checkbutton(label_cutvideomethod2, text='Check this box to use Method 2', variable=self.var_express)
        self.label_time = Entry_Box(label_cutvideomethod2,'Seconds:','8')
        CreateToolTip(label_cutvideomethod2,'Method 2 will retrieve from the end of the video.(eg: an input of 3 seconds will get rid of the first 3 seconds of the video)')

        #button to cut video
        button_cutvideo1 = Button(label_cutvideomethod1, text='Cut Video', command=lambda:shortenvideos1(self.videopath1selected.file_path,self.label_starttime.entry_get,self.label_endtime.entry_get))
        button_cutvideo2 = Button(label_cutvideomethod2,text='Cut Video',command =lambda:shortenvideos2(self.videopath1selected.file_path,self.label_time.entry_get))
        #organize
        self.videopath1selected.grid(row=0,sticky=W)

        label_cutvideomethod1.grid(row=1,sticky=W,pady=5)
        label_timeframe.grid(row=0,sticky=W)
        self.label_starttime.grid(row=1,sticky=W)
        self.label_endtime.grid(row=2,sticky=W)
        button_cutvideo1.grid(row=3)


        label_cutvideomethod2.grid(row=2,sticky=W,pady=5)
        label_method2.grid(row=0,sticky=W)
        # checkbox_express.grid(row=1,sticky=W)
        self.label_time.grid(row=2,sticky=W)
        button_cutvideo2.grid(row=3)

class change_imageformat:

    def __init__(self):

        # Popup window
        chgimgformat = Toplevel()
        chgimgformat.minsize(200, 200)
        chgimgformat.wm_title("Change image format")

        #select directory
        self.folderpath1selected = FolderSelect(chgimgformat,"Image directory",title='Select folder with images')

        #change image format
        label_filetypein = LabelFrame(chgimgformat,text= 'Original image format',font=("Helvetica",12,'bold'),padx=15,pady=5)
        # Checkbox input
        self.varfiletypein = IntVar()
        checkbox_c1 = Radiobutton(label_filetypein, text=".png", variable=self.varfiletypein, value=1)
        checkbox_c2 = Radiobutton(label_filetypein, text=".jpeg", variable=self.varfiletypein, value=2)
        checkbox_c3 = Radiobutton(label_filetypein, text=".bmp", variable=self.varfiletypein, value=3)

        #ouput image format
        label_filetypeout = LabelFrame(chgimgformat,text='Output image format',font=("Helvetica",12,'bold'),padx=15,pady=5)
        #checkbox output
        self.varfiletypeout = IntVar()
        checkbox_co1 = Radiobutton(label_filetypeout, text=".png", variable=self.varfiletypeout, value=1)
        checkbox_co2 = Radiobutton(label_filetypeout, text=".jpeg", variable=self.varfiletypeout, value=2)
        checkbox_co3 = Radiobutton(label_filetypeout, text=".bmp", variable=self.varfiletypeout, value=3)

        #button
        button_changeimgformat = Button(chgimgformat, text='Convert image file format', command=self.changeimgformatcommand)

        #organized
        self.folderpath1selected.grid(row=0,column=0)
        label_filetypein.grid(row=1,column=0,pady=5)
        checkbox_c1.grid(row=2,column=0)
        checkbox_c2.grid(row=3,column=0)
        checkbox_c3.grid(row=4,column=0)
        label_filetypeout.grid(row=5,column=0,pady=5)
        checkbox_co1.grid(row=6,column=0)
        checkbox_co2.grid(row=7,column=0)
        checkbox_co3.grid(row=8, column=0)
        button_changeimgformat.grid(row=9,pady=5)

    def changeimgformatcommand(self):

        if self.varfiletypein.get()==1:
            filetypein = str('png')
        elif self.varfiletypein.get()==2:
            filetypein = str('jpeg')
        elif self.varfiletypein.get()==3:
            filetypein = str('bmp')

        if self.varfiletypeout.get()==1:
            filetypeout = str('png')
        elif self.varfiletypeout.get()==2:
            filetypeout = str('jpeg')
        elif self.varfiletypeout.get() == 3:
            filetypeout = str('bmp')

        cif=changeimageformat(self.folderpath1selected.folder_path, filetypein, filetypeout)

        print('Images converted to '+ str(cif) + ' format')

class convert_video:

    def __init__(self):
        # Popup window
        convertvid = Toplevel()
        convertvid.minsize(400, 400)
        convertvid.wm_title("Convert video format")

        #multi video
        label_multivideo = LabelFrame(convertvid, text='Convert multiple videos',font=("Helvetica",12,'bold'),padx=5,pady=5)
        vid_dir = FolderSelect(label_multivideo,'Video directory',title='Select folder with videos')
        ori_format = Entry_Box(label_multivideo,'Input format','12')
        final_format = Entry_Box(label_multivideo,'Output format','12')
        button_convertmultivid = Button(label_multivideo,text='Convert multiple videos',command = lambda: batch_convert_videoformat(vid_dir.folder_path,ori_format.entry_get,final_format.entry_get))

        #single video
        label_convert = LabelFrame(convertvid,text='Convert single video',font=("Helvetica",12,'bold'),padx=5,pady=5)
        self.videopath1selected = FileSelect(label_convert, "Video path",title='Select a video file')
        self.vvformat = IntVar()
        checkbox_v1 = Radiobutton(label_convert, text="Convert .avi to .mp4", variable=self.vvformat, value=1)
        checkbox_v2 = Radiobutton(label_convert, text="Convert mp4 into Powerpoint supported format", variable=self.vvformat, value=2)

        #button
        button_convertvid= Button(label_convert, text='Convert video format', command=self.convertavitomp)

        #organize
        label_multivideo.grid(row=0,sticky=W)
        vid_dir.grid(row=0,sticky=W)
        ori_format.grid(row=1,sticky=W)
        final_format.grid(row=2,sticky=W)
        button_convertmultivid.grid(row=3,pady=10)

        label_convert.grid(row=1,sticky=W)
        self.videopath1selected.grid(row=0,sticky=W)
        checkbox_v1.grid(row=1,column=0,sticky=W)
        checkbox_v2.grid(row=2,column=0,sticky=W)
        button_convertvid.grid(row=3,column=0,pady=10)

    def convertavitomp(self):

        if self.vvformat.get()== 1:
            cavi = convertavitomp4(self.videopath1selected.file_path)
            print('Video converted to ' + cavi)
        elif self.vvformat.get()== 2:
            cavi = convertpowerpoint(self.videopath1selected.file_path)
            print('Video converted to ' + cavi)

class extract_specificframes:

    def __init__(self):
        # Popup window
        extractsf = Toplevel()
        extractsf.minsize(200, 200)
        extractsf.wm_title("Extract defined Frames")

        # videopath
        self.videopath1selected = FileSelect(extractsf, "Video path",title='Select a video file')

        #entry boxes for frames to extract
        label_frametitle = LabelFrame(extractsf, text='Frames to be extracted',padx=5,pady=5)
        self.label_startframe1 = Entry_Box(label_frametitle,'Start Frame:','10')

        self.label_endframe1 = Entry_Box(label_frametitle, 'End Frame:','10')


        #button
        button_extractsf = Button(label_frametitle, text='Extract Frames', command=self.extractsfcommand)

        #organize
        self.videopath1selected.grid(row=0,column=0,sticky=W,pady=10)
        label_frametitle.grid(row=1,column=0,sticky=W)
        self.label_startframe1.grid(row=2,column=0,sticky=W)

        self.label_endframe1.grid(row=3,column=0,sticky=W)

        button_extractsf.grid(row=4,pady=5)

    def extractsfcommand(self):

        startframe1 = self.label_startframe1.entry_get
        endframe1 = self.label_endframe1.entry_get

        extractspecificframe(self.videopath1selected.file_path, startframe1, endframe1)
        print('Frames were extracted from '+ str(startframe1)+' to ' + endframe1)

def extract_allframes():

    # Popup window
    extractaf = Toplevel()
    extractaf.minsize(200, 200)
    extractaf.wm_title("Extract all frames")

    # videopath
    videopath = FileSelect(extractaf, "Video path",title='Select a video file')

    #button
    button_extractaf = Button(extractaf, text='Extract All Frames', command= lambda:extract_allframescommand(videopath.file_path))

    #organize
    videopath.grid(row=0,column=0)
    button_extractaf.grid(row=1,column=0)

class changefps:
    def __init__(self):
        fpsmenu = Toplevel()
        fpsmenu.minsize(200, 200)
        fpsmenu.wm_title("Change frame rate of video")

        # videopath
        videopath = FileSelect(fpsmenu, "Video path",title='Select a video file')

        #fps
        label_fps= Entry_Box(fpsmenu,'Output fps','10')

        #button
        button_fps = Button(fpsmenu,text='Convert',command=lambda:changefps_singlevideo(videopath.file_path,label_fps.entry_get))

        #organize
        videopath.grid(row=0,sticky=W)
        label_fps.grid(row=1,sticky=W)
        button_fps.grid(row=2)

class mergeframeffmpeg:

    def __init__(self):
        # Popup window
        mergeffmpeg = Toplevel()
        mergeffmpeg.minsize(250, 250)
        mergeffmpeg.wm_title("Merge images to video")

        # select directory
        self.folderpath1selected = FolderSelect(mergeffmpeg,"Working Directory",title='Select folder with frames')

        # settings
        label_settings = LabelFrame(mergeffmpeg,text='Settings',padx=5,pady=5)
        self.label_imgformat = Entry_Box(label_settings, 'Image format','10')
        label_to = Label(label_settings,text=' to ',width=0)
        self.label_vidformat = Entry_Box(label_settings,'Video format','10')
        self.label_bitrate = Entry_Box(label_settings,'Bitrate','10')
        self.label_fps = Entry_Box(label_settings,'fps','10')

        #button
        button_mergeimg = Button(label_settings, text='Merge Images', command=self.mergeframeffmpegcommand)

        #organize
        label_settings.grid(row=1,pady=10)
        self.folderpath1selected.grid(row=0,column=0,pady=10)
        self.label_imgformat.grid(row=1,column=0,sticky=W)

        label_to.grid(row=1,column=1)
        self.label_vidformat.grid(row=1,column=2,sticky=W)
        self.label_fps.grid(row=2,column=0,sticky=W,pady=5)
        self.label_bitrate.grid(row=3,column=0,sticky=W,pady=5)
        button_mergeimg.grid(row=4,column=1,sticky=E,pady=10)


    def mergeframeffmpegcommand(self):

        imgformat = self.label_imgformat.entry_get
        vidformat = self.label_vidformat.entry_get
        bitrate = self.label_bitrate.entry_get
        fps = self.label_fps.entry_get

        mergemovieffmpeg(self.folderpath1selected.folder_path,fps,vidformat,bitrate,imgformat)
        print('Video created.')

class creategif:

    def __init__(self):
        # Popup window
        create_gif = Toplevel()
        create_gif.minsize(250, 250)
        create_gif.wm_title("Generate Gif from video")
        #Create Gif
        label_creategif = LabelFrame(create_gif,text='Video to Gif',padx=5,pady=5,font='bold')
        # select video to convert to gif
        videoselected = FileSelect(label_creategif, 'Video path',title='Select a video file')
        label_starttime = Entry_Box(label_creategif,'Start time(s)','12')
        label_duration = Entry_Box(label_creategif,'Duration(s)','12')
        label_size = Entry_Box(label_creategif,'Width','12')
        size_description = Label(label_creategif,text='example width: 240,360,480,720,1080',font=("Times", 10, "italic"))
        #convert
        button_creategif = Button(label_creategif,text='Generate Gif',command=lambda :generategif(videoselected.file_path,label_starttime.entry_get,label_duration.entry_get,label_size.entry_get))

        #organize
        label_creategif.grid(row=0,sticky=W)
        videoselected.grid(row=0,sticky=W,pady=5)
        label_starttime.grid(row=1,sticky=W)
        label_duration.grid(row=2,sticky=W)
        label_size.grid(row=3,sticky=W)
        size_description.grid(row=4,sticky=W)
        button_creategif.grid(row=5,sticky=E,pady=10)


class Scrollable(Frame):
    """
       Make a frame scrollable with scrollbar on the right.
       After adding or removing widgets to the scrollable frame,
       call the update() method to refresh the scrollable area.
    """

    def __init__(self, frame, width=16):

        scrollbarX = Scrollbar(frame, width=width, orient='horizontal')
        scrollbarX.pack(side=BOTTOM, fill=X, expand=False)
        scrollbarY = Scrollbar(frame, width=width)
        scrollbarY.pack(side=RIGHT, fill=Y, expand=False)

        self.canvas = Canvas(frame, xscrollcommand=scrollbarX.set, yscrollcommand=scrollbarY.set)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)

        scrollbarX.config(command=self.canvas.xview)
        scrollbarY.config(command=self.canvas.yview)

        self.canvas.bind('<Configure>', self.__fill_canvas)

        # base class initialization
        Frame.__init__(self, frame)

        # assign this obj (the inner frame) to the windows item of the canvas
        self.windows_item = self.canvas.create_window(0,0, window=self, anchor=NW)

        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)

    def on_mousewheel(self, event):
        scrollSpeed = event.delta
        if platform.system() == 'Darwin':
            scrollSpeed = event.delta
        elif platform.system() == 'Windows':
            scrollSpeed = int(event.delta/120)
        self.canvas.yview_scroll(-1*(scrollSpeed), "units")

    def __fill_canvas(self, event):
        "Enlarge the windows item to the canvas width"

        canvas_width = event.width
        self.canvas.itemconfig(self.windows_item, width = canvas_width)

    def update(self):
        "Update the canvas and the scrollregion"

        self.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox(self.windows_item))

class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 57
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)


class App(object):
    def __init__(self):
        self.root = Tk()
        self.root.title('Video processing GUI')
        self.root.minsize(750,750)
        self.root.geometry("750x750")
        self.root.iconbitmap('video.ico')
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        img = PhotoImage(file='video.png')
        background = Label(self.root, image=img, bd=0)
        background.pack(fill='both', expand=True)
        background.image = img

        ### drop down menu###
        menu = Menu(self.root)
        self.root.config(menu=menu)

        # Process video
        pvMenu = Menu(menu)
        menu.add_cascade(label='Process Videos', menu=pvMenu)
        pvMenu.add_command(label='Batch pre-process videos', command=batch_processvideo)

        # fifth menu
        fifthMenu = Menu(menu)
        menu.add_cascade(label='Tools', menu=fifthMenu)
        fifthMenu.add_command(label='Clip videos', command=shorten_video)
        fifthMenu.add_command(label='Crop videos', command=crop_video)
        fifthMenu.add_command(label='Downsample videos', command=video_downsample)
        fifthMenu.add_command(label='Change fps', command=changefps)

        changeformatMenu = Menu(fifthMenu)
        changeformatMenu.add_command(label='Change image file formats', command=change_imageformat)
        changeformatMenu.add_command(label='Change video file formats', command=convert_video)
        fifthMenu.add_cascade(label='Change formats', menu=changeformatMenu)

        fifthMenu.add_command(label='CLAHE enhance video', command=Red_light_Convertion)
        fifthMenu.add_command(label='Superimpose frame numbers on video',
                              command=lambda: superimposeframe(askopenfilename()))
        fifthMenu.add_command(label='Convert to grayscale', command=lambda: greyscale(askopenfilename()))
        fifthMenu.add_command(label='Merge frames to video', command=mergeframeffmpeg)
        fifthMenu.add_command(label='Generate gifs', command=creategif)

        extractframesMenu = Menu(fifthMenu)
        extractframesMenu.add_command(label='Extract defined frames', command=extract_specificframes)
        extractframesMenu.add_command(label='Extract frames', command=extract_allframes)
        fifthMenu.add_cascade(label='Extract frames', menu=extractframesMenu)

        #sixth menu
        sixthMenu = Menu(menu)
        menu.add_cascade(label='Help',menu=sixthMenu)
        #labelling tool
        links = Menu(sixthMenu)
        links.add_command(label='Install FFmpeg',command =lambda: webbrowser.open_new(str(r'https://m.wikihow.com/Install-FFmpeg-on-Windows')))
        sixthMenu.add_cascade(label="Links",menu=links)
        # sixthMenu.add_command(label='About', command= aboutgui)

        #Status bar at the bottom
        self.frame = Frame(background, bd=2, relief=SUNKEN, width=300, height=300)
        self.frame.pack(expand=True)
        self.txt = Text(self.frame, bg='white')
        self.txt.config(state=DISABLED)
        self.txt.pack(expand=True, fill='both')
        sys.stdout = StdRedirector(self.txt)


# writes text out in GUI
class StdRedirector(object):
    def __init__(self, text_widget):
        self.text_space = text_widget

    def write(self, string):
        self.text_space.config(state=NORMAL)
        self.text_space.insert("end", string)
        self.text_space.update()
        self.text_space.see("end")
        self.text_space.config(state=DISABLED)

class SplashScreen:
    def __init__(self, parent):
        self.parent = parent
        self.Splash()
        self.Window()

    def Splash(self):
        self.image = Image.open(r".\video.png")
        self.imgSplash = ImageTk.PhotoImage(self.image)

    def Window(self):
        width, height = self.image.size
        halfwidth = (self.parent.winfo_screenwidth()-width)//2
        halfheight = (self.parent.winfo_screenheight()-height)//2
        self.parent.geometry("%ix%i+%i+%i" %(width, height, halfwidth,halfheight))
        Label(self.parent, image=self.imgSplash).pack()


if __name__ == '__main__':
    root = Tk()
    root.overrideredirect(True)
    app = SplashScreen(root)
    root.after(1000, root.destroy)
    root.mainloop()


app = App()
print('Welcome to Video processing GUI :) ')
app.root.mainloop()
