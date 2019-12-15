import subprocess
import numpy as np
import os
import cv2
from os import listdir
from os.path import isfile, join
import yaml
from PIL import Image
import glob
import pathlib

def batch_convert_videoformat(directory,format1,format2):
    filesFound = []
    format1 = '.'+format1
    for i in os.listdir(directory):
        if str(format1) in i:
            filesFound.append(i)

    def execute(command):
        subprocess.call(command, shell=True, stdout=subprocess.PIPE)

    ########### DEFINE COMMAND ###########
    for i in filesFound:
        currentFile = i
        outFile = currentFile.replace(format1, '.'+format2)
        outFile = str(outFile)
        output = os.path.basename(outFile)
        print('Converting video...')
        command = (str('ffmpeg -y -i ') +'"' + str(directory)+ '\\' + str(currentFile)+'"' + ' -c:v libx264 -crf 5 -preset medium -c:a libmp3lame -b:a 320k '+'"' + str(directory) + '\\' + outFile+'"')

        execute(command)
        print('Video converted! ',output, ' created.')



def generategif(filename,starttime,duration,size):
    if starttime =='' or duration =='' or size =='':
        print('Please make sure all the boxes are filled before continue')
    elif filename != '' and filename != 'No file selected':
        def execute(command):
            subprocess.call(command, shell=True, stdout = subprocess.PIPE)

        currentFile = filename
        outFile,fileformat = currentFile.split('.')
        outFile = str(outFile) + '.gif'
        output = os.path.basename(outFile)

        command = 'ffmpeg -ss ' + str(starttime) + ' -t ' + str(duration) + ' -i ' +'"'+ str(filename) +'"'+ ' -filter_complex "[0:v] fps=15,scale=w=' + str(size) + ':h=-1,split [a][b];[a] palettegen=stats_mode=single [p];[b][p] paletteuse=new=1" ' +'"'+ str(outFile)+'"'
        file = pathlib.Path(outFile)
        if file.exists():
            print(output,'already exist')
        else:
            print('Generating gif...')
            execute(command)
            print('Gif ', output, ' created.')
        return output

    else:
        print('Please select a video to start')


def downsamplevideo(width,height,filename):
    if width =='' or height == '':
        print('Please enter width and height to continue')
    elif filename != '' and filename !='No file selected':
        def execute(command):
            subprocess.call(command, shell=True, stdout = subprocess.PIPE)

        ########### DEFINE COMMAND ###########

        currentFile = filename
        outFile,fileformat = currentFile.split('.')
        outFile = str(outFile) + '_downsampled.mp4'
        output = os.path.basename(outFile)

        command = (str('ffmpeg -i ')+'"' + str(currentFile)+'"' + ' -vf scale='+str(width)+':'+ str(height) + ' ' +'"'+ outFile +'"'+ ' -hide_banner')
        file = pathlib.Path(outFile)
        if file.exists():
            print(output,'already exist')
        else:
            print('Downsampling video...')
            execute(command)
            print('Video downsampled! ',output, 'created')
        return output

    else:
        print('Please select a video to downsample')

def greyscale(filename):
    if filename:

        def execute(command):
            subprocess.call(command, shell=True, stdout = subprocess.PIPE)

        ########### DEFINE COMMAND ###########

        currentFile = filename
        outFile,fileformat = currentFile.split('.')
        outFile = str(outFile) + '_grayscale.mp4'
        output = os.path.basename(outFile)

        command = (str('ffmpeg -i ') +'"'+ str(currentFile)+'"' + ' -vf format=gray '+'"'+ outFile+'"')

        file = pathlib.Path(outFile)
        if file.exists():
            print(output, 'already exist')
        else:
            print('Converting into grayscale video...(this might take awhile)')
            execute(command)
            print('Video converted into grayscale! ', output, ' is created')
        return output

    else:
        print('No file chosen')

def superimposeframe(filename):
    if filename:
        def execute(command):
            subprocess.call(command, shell=True, stdout = subprocess.PIPE)

        ########### DEFINE COMMAND ###########

        currentFile = filename
        outFile,fileformat = currentFile.split('.')
        outFile = str(outFile) + '_frame_no.mp4'
        output = os.path.basename(outFile)
        command = (str('ffmpeg -i ') +'"'+ str(currentFile)+'"' + ' -vf "drawtext=fontfile=Arial.ttf: text=\'%{frame_num}\': start_number=1: x=(w-tw)/2: y=h-(2*lh): fontcolor=black: fontsize=20: box=1: boxcolor=white: boxborderw=5" -c:a copy '+'"'+ outFile+'"')

        file = pathlib.Path(outFile)
        if file.exists():
            print(output, 'already exist')
        else:
            print('Adding frame numbers...')
            execute(command)
            print('Frame numbers added!')
        return output

    else:
        print('No file chosen')

# def colorized(filename):
#
#     def execute(command):
#         print(command)
#         subprocess.call(command, shell=True, stdout = subprocess.PIPE)
#
#     ########### DEFINE COMMAND ###########
#
#     currentFile = filename
#     outFile = currentFile.replace('.mp4', '')
#     outFile = str(outFile) + '_colorized.mp4'
#     command = (str('python bw2color_video3.py --prototxt colorization_deploy_v2.prototxt --model colorization_release_v2.caffemodel --points pts_in_hull.npy --input ' )+ str(currentFile))
#     execute(command)

def shortenvideos1(filename,starttime,endtime):
    if starttime =='' or endtime =='':
        print('Please enter the time')

    elif filename != '' and filename != 'No file selected':

        def execute(command):
            subprocess.call(command, shell=True, stdout = subprocess.PIPE)

        ########### DEFINE COMMAND ###########

        currentFile = filename
        outFile, fileformat = currentFile.split('.')
        outFile = str(outFile) + '_clipped.mp4'
        output = os.path.basename(outFile)

        command = (str('ffmpeg -i ') +'"'+ str(currentFile) +'"'+ ' -ss ' + starttime + ' -to ' + endtime + ' -async 1 '+'"'+ outFile+'"')

        file = pathlib.Path(outFile)
        if file.exists():
            print(output, 'already exist')
        else:
            print('Clipping video....')
            execute(command)
            print(output,' generated!')
        return output


    else:
        print('Please select a video to trim')


def shortenvideos2(filename,time):

    if time == '':
        print('Please enter time')

    elif filename != '' and filename != 'No file selected':

        def execute(command):
            print(command)
            subprocess.call(command, shell=True, stdout = subprocess.PIPE)

        ########### DEFINE COMMAND ###########

        currentFile = filename
        outFile,fileformat = currentFile.split('.')
        outFile = str(outFile) + '_shorten.mp4'
        output = os.path.basename(outFile)

        command = (str('ffmpeg -ss ') + str(time) + ' -i '+'"' + str(currentFile)+'"'+ ' -c:v libx264 -c:a aac '+'"' + outFile+'"')

        file = pathlib.Path(outFile)
        if file.exists():
            print(output, 'already exist')
        else:
            print('Cutting video....')
            execute(command)
            print(output, ' is generated!')
        return output

    else:
        print('Please select a video to trim')

# def shortenvideosbyframes(filename,fps,startframe):
#
#     timestart = str(int(startframe)/int(fps))
#
#     def execute(command):
#         print(command)
#         subprocess.call(command, shell=True, stdout = subprocess.PIPE)
#
#     ########### DEFINE COMMAND ###########
#
#     currentFile = filename
#     outFile = currentFile.replace('.mp4', '')
#     outFile = str(outFile) + '_shorten.mp4'
#     output = os.path.basename(outFile)
#     print('Cutting video....')
#     command = (str('ffmpeg -ss ') + str(timestart) + ' -i ' + str(currentFile) + ' -c:v libx264 -c:a aac ' + outFile)
#     execute(command)
#     print(output,' is generated!')

def convertavitomp4(filename):
    if filename:

        def execute(command):
            print(command)
            subprocess.call(command, shell=True, stdout = subprocess.PIPE)

        ########### DEFINE COMMAND ###########

        currentFile = filename
        outFile,fileformat = currentFile.split('.')
        outFile = str(outFile) + '_converted.mp4'
        output = os.path.basename(outFile)

        command = (str('ffmpeg -i ')+'"' + str(currentFile)+'"' + ' '+'"' + outFile+'"')

        file = pathlib.Path(outFile)
        if file.exists():
            print(output, 'already exist')
        else:
            print('Converting avi to mp4...')
            execute(command)
            print('Video converted! ',output, ' is generated!')
        return output

    else:
        print('Please select a video to convert')

def convertpowerpoint(filename):

    if filename:

        def execute(command):
            subprocess.call(command, shell=True, stdout = subprocess.PIPE)

        ########### DEFINE COMMAND ###########

        currentFile = filename
        outFile,fileformat = currentFile.split('.')
        outFile = str(outFile) + '_powerpointready.mp4'
        output = os.path.basename(outFile)

        command = (str('ffmpeg -i ') +'"'+ str(currentFile)+'"' + ' -c:v libx264 -preset slow  -profile:v high -level:v 4.0 -pix_fmt yuv420p -crf 22 -codec:a aac '+'"' + outFile+'"')

        file = pathlib.Path(outFile)
        if file.exists():
            print(output, 'already exist')
        else:
            print('Creating video in powerpoint compatible format... ')
            execute(command)
            print('Video converted! ', output, ' generated!')
        return output
    else:
        print('Please select a video to convert')


def extract_allframescommand(filename):
    if filename:

        pathDir = str(filename[:-4])
        if not os.path.exists(pathDir):
            os.makedirs(pathDir)

        picFname = '%d.png'

        saveDirFilenames = os.path.join(pathDir, picFname)
        print(saveDirFilenames)

        fname = str(filename)
        cap = cv2.VideoCapture(fname)
        fps = cap.get(cv2.CAP_PROP_FPS)
        amount_of_frames = cap.get(7)
        print('The number of frames in this video = ',amount_of_frames)
        print('Extracting frames... (Might take awhile)')
        command = str('ffmpeg -i ' +'"'+ str(fname)+'"' + ' ' + '-q:v 1' + ' ' + '-start_number 0' + ' '+'"'+ str(saveDirFilenames)+'"')
        print(command)
        subprocess.call(command, shell=True)
        print('All frames are extracted!')
    else:
        print('Please select a video to convert')

def batch_extract_allframes(dir):
    curdir = os.listdir(dir)
    vid=[]
    for i in curdir:
        if ('.mp4') in i:
            vid.append(i)

    for index,i in enumerate(vid):
        vid[index]=os.path.join(dir,i)

    for i in vid:
        filename= i
        pathDir = str(filename[:-4])
        if not os.path.exists(pathDir):
            os.makedirs(pathDir)

        picFname = '%d.png'

        saveDirFilenames = os.path.join(pathDir, picFname)
        print(saveDirFilenames)

        fname = str(filename)
        cap = cv2.VideoCapture(fname)
        fps = cap.get(cv2.CAP_PROP_FPS)
        amount_of_frames = cap.get(7)
        print('The number of frames in this video = ', amount_of_frames)
        print('Extracting frames... (Might take awhile)')
        command = str(
            'ffmpeg -i '+'"' + str(fname)+'"' + ' ' + '-q:v 1' + ' ' + '-start_number 0' + ' ' +'"'+ str(saveDirFilenames)+'"')
        print(command)
        subprocess.call(command, shell=True)
        print('All frames are extracted!')

def mergemovieffmpeg(directory,framespersec,vidformat,bit,imgformat):

    currDir = directory

    fps = str(framespersec)
    fileformat = str('.'+vidformat)
    bitrate = str(bit)
    imageformat = str(imgformat)

    currentDir = directory
    fileOut = str(directory)+ str(fileformat)
    currentDirPath = directory
    currentFileList = [f for f in listdir(currentDirPath) if isfile(join(currentDirPath, f))]
    imgPath = os.path.join(currentDirPath, currentFileList[0])
    img = cv2.imread(imgPath)
    print(imgPath)
    ffmpegFileName = os.path.join(currentDirPath, '%d.' + str(imageformat))
    imgShape = img.shape
    height = imgShape[0]
    width = imgShape[1]
    command = str('ffmpeg -r ' + str(fps) + str(' -f image2 -s ') + str(height) + 'x' + str(width) + ' -i ' +'"'+ str(ffmpegFileName)+'"' + ' -vcodec libx264 -b ' + str(bitrate) + 'k ' +'"'+ str(fileOut)+'"')
    print(command)
    subprocess.call(command, shell=True)

def mergemovebatch(dir,framespersec,vidformat,bit,imgformat):
    currDir = os.listdir(dir)
    fps = str(framespersec)
    fileformat = str('.' + vidformat)
    bitrate = str(bit)
    imageformat = str(imgformat)

    for i in currDir:
        directory = os.path.join(dir,i)
        fileOut = str(directory) + str(fileformat)
        currentDirPath = directory
        currentFileList = [f for f in listdir(currentDirPath) if isfile(join(currentDirPath, f))]
        imgPath = os.path.join(currentDirPath, currentFileList[0])
        img = cv2.imread(imgPath)
        print(imgPath)
        ffmpegFileName = os.path.join(currentDirPath, '%d.' + str(imageformat))
        imgShape = img.shape
        height = imgShape[0]
        width = imgShape[1]
        command = str('ffmpeg -r ' + str(fps) + str(' -f image2 -s ') + str(height) + 'x' + str(width) + ' -i ' +'"'+ str(
            ffmpegFileName) +'"'+ ' -vcodec libx264 -b ' + str(bitrate) + 'k ' +'"'+ str(fileOut)+'"')
        print(command)
        subprocess.call(command, shell=True)

def changefps_multivideo(dir,fps):

    currdir = os.listdir(dir)
    fpss = str(fps)

    for i in currdir:
        video = os.path.join(dir,i)
        output = os.path.join(dir,fpss + i)
        command = str('ffmpeg -i ') +'"'+ str(video)+'"' + ' -filter:v fps=fps=' + fpss + ' '+'"' + output+'"'
        print(command)
        subprocess.call(command,shell=True)

def changefps_singlevideo(filename,fps):
    video = filename
    outputname = (os.path.basename(video))[:-4]+ '_fps_' + str(fps)+ (os.path.basename(video))[-4:]
    output = os.path.join(os.path.dirname(video),outputname)
    command = str('ffmpeg -i ') +'"'+ str(video)+'"' + ' -filter:v fps=fps=' + str(fps) + ' ' +'"'+ output+'"'
    print(command)
    subprocess.call(command, shell=True)
    print('Fps changed to',str(fps))

# def rename(dir):
#     filename = os.listdir(dir)
#
#     os.chdir(dir)
#
#     for i in filename:
#         os.rename(i,i[2:])


def extractspecificframe(filename,startframe1,endframe1):

    cap = cv2.VideoCapture(filename)
    amount_of_frames = cap.get(7)
    pathDir = str(filename[:-4]+'\\frames')
    if not os.path.exists(pathDir):
        os.makedirs(pathDir)

    frames_OI = list(range(int(startframe1),int(endframe1)+1))
    #frames_OI.extend(range(7000,7200))
    #frames_OI.extend(range(9200,9350))

    for i in frames_OI:
        currentFrame = i
        cap.set(1, currentFrame)
        ret, frame = cap.read()
        fileName = str(currentFrame) + str('.png')
        filePath = os.path.join(pathDir, fileName)
        cv2.imwrite(filePath,frame)

def clahe(filename):
    os.chdir(os.path.dirname(filename))
    print('Applying CLAHE, this might take awhile...')

    currentVideo = os.path.basename(filename)
    fileName, fileEnding = currentVideo.split('.',2)
    saveName = str('CLAHE_') + str(fileName) + str('.avi')
    cap = cv2.VideoCapture(currentVideo)
    imageWidth = int(cap.get(3))
    imageHeight = int(cap.get(4))
    fps = cap.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(saveName, fourcc, fps, (imageWidth, imageHeight), 0)
    try:
        while True:
            ret, image = cap.read()
            if ret == True:
                im = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                claheFilter = cv2.createCLAHE(clipLimit=2, tileGridSize=(16, 16))
                claheCorrecttedFrame = claheFilter.apply(im)
                out.write(claheCorrecttedFrame)
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break
            else:
                print(str('Completed video ') + str(saveName))
                break
    except:
        print('clahe not applied')
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    return saveName

def cropvid(filenames):
    if filenames:

        #extract one frame
        currentDir = str(os.path.dirname(filenames))
        videoName = str(os.path.basename(filenames))
        os.chdir(currentDir)
        cap = cv2.VideoCapture(videoName)
        cap.set(1, 0)
        ret, frame = cap.read()
        fileName = str(0) + str('.bmp')
        filePath = os.path.join(currentDir, fileName)
        cv2.imwrite(filePath, frame)
        #find ROI

        img = cv2.imread(filePath)
        cv2.namedWindow('Select ROI', cv2.WINDOW_NORMAL)
        ROI = cv2.selectROI("Select ROI", img)
        width = abs(ROI[0] - (ROI[2] + ROI[0]))
        height = abs(ROI[2] - (ROI[3] + ROI[2]))
        topLeftX = ROI[0]
        topLeftY = ROI[1]
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        #crop video with ffmpeg
        fileOut, fileType = videoName.split(".", 2)
        fileOutName = str(fileOut) + str('_cropped.mp4')
        command = str('ffmpeg -i ') +'"'+ str(videoName) +'"'+ str(' -vf ') + str('"crop=') + str(width) + ':' + str(
            height) + ':' + str(topLeftX) + ':' + str(topLeftY) + '" ' + str('-c:v libx264 -crf 21 -c:a copy ') +'"'+ str(
            fileOutName)+'"'
        total = width + height + topLeftX + topLeftY

        file = pathlib.Path(fileOutName)
        if file.exists():
            print(os.path.basename(fileOutName), 'already exist')
        else:
            if width==0 and height ==0:
                print('Video not cropped')
            elif total != 0:
                print('Cropping video...')
                print(command)
                subprocess.call(command, shell=True)
                os.remove(filePath)
                print('Cropped video saved!')
                return fileOutName
            elif total ==0:
                print('Video not cropped')

        os.remove(filePath)

    else:
        print('Please select a video to crop')
def changedlc_config(config_path):

    config_path = config_path

    with open(config_path) as f:
        read_yaml = yaml.load(f)

    read_yaml["bodyparts"] = ['Ear_left_1',
                              'Ear_right_1',
                              'Nose_1',
                              'Center_1',
                              'Lateral_left_1',
                              'Lateral_right_1',
                              'Tail_base_1',
                              'Tail_end_1',
                              'Ear_left_2',
                              'Ear_right_2',
                              'Nose_2',
                              'Center_2',
                              'Lateral_left_2',
                              'Lateral_right_2',
                              'Tail_base_2',
                              'Tail_end_2']

    with open(config_path, 'w') as outfile:
        yaml.dump(read_yaml, outfile, default_flow_style=False)


def changeimageformat(directory,filetypein,filetypeout):

    os.chdir(directory)
    filetype1 = filetypein
    filetype2 = filetypeout

    for filename in glob.glob('*.'+str(filetype1)):
        im = Image.open(filename)
        saveName = filename.replace('.'+str(filetype1), '.'+str(filetype2))
        im.save(saveName)
        os.remove(filename)

    return filetype2