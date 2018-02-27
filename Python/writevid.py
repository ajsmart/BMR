import cv2, os


#make into video
image_folder = 'data\image2'
video_name = 'test2.avi'

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, -1, 30, (width,height))#cv2.VideoWriter_fourcc('H','F','Y','U'), 30, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))
video.release()
cv2.destroyAllWindows()
