import datetime, cv2, time, os, shutil
current_time = datetime.datetime.now()
####### Change for total time #######
endtime = current_time + datetime.timedelta(hours=20)
#####################################
print(current_time,endtime)
cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)
os.mkdir("image")
os.mkdir('image2')
while datetime.datetime.now() < endtime:  
    date_string=time.strftime("%H:%M:%S")
    img = cap.read()[1]
    img2 = cap2.read()[1]
    #gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    cv2.putText(img,date_string,(10,50),cv2.FONT_HERSHEY_COMPLEX,1,255)
    cv2.putText(img2,date_string,(10,50),cv2.FONT_HERSHEY_COMPLEX,1,255)
    cv2.imwrite('image\img_{}.png'.format(int(time.time())), img)
    cv2.imwrite('image2\img_{}.png'.format(int(time.time())), img2)
    #amount of time in seconds between samples
    time.sleep(30)

#make into video
#for x in range(1,3):
#    if x == 1:
#        image_folder = 'image'
#        video_name = 'video1.avi'
#    else:
#        image_folder = 'image2'
#        video_name = 'video2.avi'

#    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
#    frame = cv2.imread(os.path.join(image_folder, images[0]))
#    height, width, layers = frame.shape

#    video = cv2.VideoWriter(video_name, -1, 30, (width,height))

#    for image in images:
#        video.write(cv2.imread(os.path.join(image_folder, image)))
#    video.release()
cv2.destroyAllWindows()
#shutil.rmtree('image')
#shutil.rmtree('image2')
