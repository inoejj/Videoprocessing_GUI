# How to use tools in GUI

- [Shorten Videos](/docs/Tutorial_tools.md#shorten-videos)
- [Crop Videos](/docs/Tutorial_tools.md#crop-video)
- [Downsample Videos](/docs/Tutorial_tools.md#downsample-video)
- [Change formats](/docs/Tutorial_tools.md#change-formats)
- [CLAHE](/docs/Tutorial_tools.md#clahe)
- [Add Frame Numbers](/docs/Tutorial_tools.md#add-frame-numbers)
- [Grayscale](/docs/Tutorial_tools.md#convert-to-grayscale)
- [Merge Frames to video](/docs/Tutorial_tools.md#merge-images-to-video)
- [Generate Gifs](/docs/Tutorial_tools.md#generate-gifs)
- [Extract Frames](/docs/Tutorial_tools.md#extract-frames)

## Shorten Videos
This is a tool to trim videos using ffmpeg. It contains **Method 1** and **Method 2**

<img src="/images/shortenvideo.PNG" width="544" height="241" />

### Method 1 
Method 1 has the freedom to cut from the beginning of the video and from the end of the video.

Let's say we have a 2 minute long video and we want to get rid of the first 10 seconds and the last 5 seconds of the video.
We would start our video on the 10th second `00:00:10` and end at `00:01:55`.

1. First, click on `Browse File` to select the video to trim.

2. Enter the time frame in `Start at:` entry box, in this case it will be *00:00:10*

3. Enter the time frame in `End at:` entry box, in this case it will be *00:01:55*. The settings should look like the image below.

<img src="/images/shortenvideo1.PNG" width="405" height="115" />

4. Click `Cut Video` to trim video and a new shorten video will be generated, the new video will have a name of *Name of original video* + *_shorten* .

<img src="/images/shortenvideos2.PNG" width="1014" height="114" />


### Method 2
Method 2 cuts of the beginning of the video. In order to use method 2, please check on the check box.

Let's say we have a 2 minute long video and we want to get rid of the first 20 seconds from the start of the video.


1. Enter the amount of time that needs to be trimmed from the start of the video in `Seconds:`, in this case it will be *20*


2. Click `Cut Video` to trim video and a new shorten video will be generated, the new video will have a name of *Name of original video* + *_shorten* .


## Crop Video
This is a tool to crop videos.

<img src="/images/cropvideo.PNG" width="232" height="232" />

1. First, click on `Browse File` to select a video to crop.

2. Then click on `Crop Video` and the following window `Select ROI` will pop up.

<img src="/images/cropvideo2.PNG" width="363" height="546" />

3. Use your mouse to *Left Click* on the video and drag to crop the video. *You can always left click and drag on the video to recrop your video*

<img src="/images/cropvideo3.PNG" width="363" height="546" />

4. Hit `Enter` **twice** and it will crop the video, the new video will have a name of *Name of original video* + *_cropped*.

<img src="/images/cropvideo4.PNG" width="900" height="100" />


## Downsample Video
This is a tool to downsample video into smaller size and reduce the resolution of the video.

<img src="/images/downsamplevid.PNG" width="400" height="300" />

The downsample video tool has **Customize Resolution** and **Default Resolution**

### Customize Resolution
This allows you to downsample video into any height and width.

1. First, click on `Browse File` to select a video to downsample.

2. Then, enter any values in the `Height` and `Width` entry boxes.

<img src="/images/downsamplevid2.PNG" width="400" height="300" />

3. Click on `Downsample Custom Resolution Video` to downsample the video, the new video will have a name of *Name of original video* + *_downsampled*.

<img src="/images/downsamplevid3.PNG" width="900" height="100" />

### Default Resolution 
This allows you to downsample video quickly within two mouse clicks. There will be more options added into the **Default Resolution** in the future.

1. First, click on `Browse File` to select a video to downsample.

2. Click on one of the option `1980 x 1080` or `1280 x 1024`.

3. Click on `Downsample Default Resolution Video` and the video will downsample into the selected resolution.

## Change formats
Change formats includes **Change image format** and **Change video format**

### Change image format
This tool allows the user to select a folder with multiple images and convert the image format.

<img src="/images/changeimageformat.PNG" width="200" height="200" />

1. Click on `Browse Folder` to select a folder that contains multiple images

2. Choose the original image format that is in the folder

3. Choose the desire output image format

4. Click `Convert Image Format` .

### Change video format
This tool allows the user to convert videos into desired format.

<img src="/images/changevideoformat.PNG" width="400" height="400" />

#### Convert multiple videos

1. Click on `Browse Folder` to select the directory that contains all the videos that you wished to convert.

2. Enter the original format (eg: mp4,flv,avi...etc.) in the `Orignal Format` entry box. **Note: do not put in the dots " . " (eg: .mp4 or .flv etc)**

3. Enter the format to be converted into in the `Final Format` entry box 

4. Click `Convert multiple videos`.

#### Convert single video

1. Click on `Browse File` to select a video to convert.

2. Choose one of the following `Convert .avi to .mp4` or `Convert mp4 into Powerpoint supported format`

3. Click `Convert video format`.


## [CLAHE](https://docs.opencv.org/3.4/d5/daf/tutorial_py_histogram_equalization.html)

1. Click on the `Browse File` to select a video.

2. Click `Apply CLAHE`, and the new video will have a name of *CLAHE_* *Name of original video* and it will be in a **.avi** format.

## Add Frame Numbers

1. Click on `Add Frame Numbers`, and a new window will pop up.

2. Select video and click `Open` and frame numbers wil be superimposed to the video.

3. The new video will have a name of *Name of original video* + *_frame_no*.

## Convert to grayscale

1. Click on `Convert to grayscale`, and a new window will pop up.

2. Select video and click `Open` and the video will be converted to grayscale.

3. The new video will have a name of *Name of original video* + *_grayscale*.


## Merge images to video

1. Click on `Browse Folder` to select a folder with frames 

2. Enter the image format of the frames. Eg: if the image name is *Image001.PNG*, enter *PNG* in the `Image Format` entry box.

3. Enter the desire output video format. Eg: if the video should be a *.mp4*, enter *mp4* in the `Video Format` entry box.

4. Enter the desire frames per second in the `fps` entry box.

5. Enter the desire [bitrate](https://help.encoding.com/knowledge-base/article/understanding-bitrates-in-video-files/) for the video in the `Bitrate` entry box.

6. Click `Merge Images`

## Generate Gifs

1. Click on `Browse File` to select a video to convert to a GIF

2. Enter the starting time of the GIF from the video in the `From time(s)` entry box.

3. Enter the duration of the GIF in the `Duration(s)` entry box.

4. Enter the size of the GIF in the `Width` entry box. The output GIF will be scale automatically.

## Extract Frames
Extract frames consist of **Extract Defined Frames**, **Extract Frames**, and **Extract Frames from seq files**

### Extract Specific Frames
Extract specific frames allows the user to extract from certain frames to certain frames in a video.

1. Click `Browse File` to select a video.

2. Enter the starting frame number in the `Start Frame` entry box.

3. Enter the ending frame number in the `End Frame` entry box.

4. Click `Extract Frames` to extract the frames from `Start Frame` to `End Frame`.

5. A folder with the video name will be generated and the all the frames will be in the folder. The image will be in *.png* format

### Extract Frames
Extract frames allows the user to extract every frame from a video.

1. Click `Browse File` to select a video.

2. Click `Extract All Frames` to extract every frames from the video.

3. A folder with the video name will be generated and the all the frames will be in the folder. The image will be in *.png* format

