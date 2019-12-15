# Tutorial for processing video in batch
Videos are processed via **ffmpeg** in **python**. Click [here](https://m.wikihow.com/Install-FFmpeg-on-Windows) to learn how to install ffmpeg.

## Pipeline

<img src=https://github.com/inoejj/Videoprocessing_GUI/blob/master/images/processvideo_flowdiagram.png width="800" height="310" />

## Step 1: Folder Selection


1. `Process Videos` --> `Batch pre-process videos`.


2. Under **Folder Selection**, `Directory with videos in it`, select a folder with **only** videos by clicking `Browse Folder`

3. Under `Output Directory`, select an output directory where all the processed videos will be saved by clicking `Browse Folder`

4. Click `Confirm` to confirm the directories selected.

>**Note**: Please make sure there is no space in your folder name or video name.



## Step 2: Select parameters

1. A table with the videos in the folder will pop up.

<img src=https://github.com/inoejj/Videoprocessing_GUI/blob/master/images/batchprocessvideo.png width="1102" height="200" />

2. If you wish to crop your videos, click on the `Crop` button. *The button will turn red once you clicked on it*

3. If you wish to trim your videos, check on the `Shorten` box and enter the **Start Time** and  **End Time** in the HH:MM:SS format.

4. If you wish to downsample your video, check on the `Downsample` box and enter the **Width** and **Height**.

5. If you wish to Grayscale your video, check on the `Grayscale` box.

6. If you wish to superimpose frames onto your video, check on the `Add Frame #` box.

7. If you wish to apply [CLAHE](https://docs.opencv.org/master/d5/daf/tutorial_py_histogram_equalization.html), check on the `CLAHE` box.

8. In the first row, there are `Select All` checkboxes to check all the checkboxes in the given column.

> **Note:** The `Select All` checkbox might be off position. We are working on it to fix it.

## Step 3: Execute

1. Once the parameters are confirmed, click `Execute`

2. The final processed videos will be in the `Output Directory` that you have selected.

3. The **tmp** folder contains the step-by-step processsed videos.

4. The **process_archieve** folder contains the **.txt** file of the process that were ran. 
