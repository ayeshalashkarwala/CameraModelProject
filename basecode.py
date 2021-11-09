import cv2
import threading

class camThread(threading.Thread):
    def __init__(self, previewName, camID):
        threading.Thread.__init__(self)
        self.previewName = previewName
        self.camID = camID
    def run(self):
        print ("Starting "+ self.previewName)
        camPreview(self.previewName, self.camID)

def camPreview(previewName, camID):
    cv2.namedWindow(previewName)
    cam = cv2.VideoCapture(camID)
    width1 = int(cam.get(3))
    height1 = int(cam.get(4))
    size1 = (width1, height1)
    filename = 'stream' + previewName + '.avi'
    optputFile1 = cv2.VideoWriter(
         filename, cv2.VideoWriter_fourcc(*'MJPG'), 10, size1)
    
    if cam.isOpened():  # try to get the first frame
        rval, frame = cam.read()
    else:
        rval = False

    while rval:
      #  cv2.imshow(previewName, frame)
        rval, frame = cam.read()
        cv2.imshow(previewName, frame)

        #     # saves the frame from camera 1
        optputFile1.write(frame)
        key = cv2.waitKey(20)
        if key == 27:  # exit on ESC
            break
    cam.release()
    optputFile1.release()
    cv2.destroyWindow(previewName)

def main():

    print("Press 1 for pre-recorded videos, 2 for live stream: ")
    option = int(input())

    if option == 1:
        # Record video
        windowName = "Sample Feed from Camera 1"
        cv2.namedWindow(windowName)

        # capture1 = cv2.VideoCapture(0)  # laptop's camera
        # capture2 = cv2.VideoCapture("http://10.130.19.50:8080/video")   # sample code for mobile camera video capture using IP camera

        # define size for recorded video frame for video 1
        # width1 = int(capture1.get(3))
        # height1 = int(capture1.get(4))
        # size1 = (width1, height1)

        # width2 = int(capture2.get(3))
        # height2 = int(capture2.get(4))
        # size2 = (width2, height2)

        # frame of size is being created and stored in .avi file
        # optputFile1 = cv2.VideoWriter(
        #     'Stream1Recording.avi', cv2.VideoWriter_fourcc(*'MJPG'), 10, size1)

        # optputFile2 = cv2.VideoWriter(
        #     'Stream2Recording.avi', cv2.VideoWriter_fourcc(*'MJPG'), 10, size2)

        # check if feed exists or not for camera 1
        # if capture1.isOpened():
        #     ret1, frame1 = capture1.read()
        # else:
        #     ret1 = False


        # if capture2.isOpened():
        #     ret2, frame2 = capture2.read()
        # else:
        #     ret2 = False
            
        # while ret1:
        #     ret1, frame1 = capture1.read()
        #     # sample feed display from camera 1
        #     cv2.imshow(windowName, frame1)

        #     # saves the frame from camera 1
        #     optputFile1.write(frame1)

        #     # escape key (27) to exit
        #     if cv2.waitKey(1) == 27:
        #         break



        # while ret2:
        #     ret2, frame2= capture2.read()
        #     # sample feed display from camera 1
        #     cv2.imshow(windowName, frame2)

        #     # saves the frame from camera 1
        #     optputFile2.write(frame2)

        #     # escape key (27) to exit
        #     if cv2.waitKey(2) == 30:
        #         break
            
            
        # capture1.release()
        # optputFile1.release()
        
        # capture2.release()
        # optputFile2.release()
        
        # cv2.destroyAllWindows()

        thread1 = camThread("Camera1", "http://10.130.16.39:4747/video")
        thread2 = camThread("Camera2", "http://10.130.146.18:4747/video")
        thread3 = camThread("Camera3", "http://10.130.19.50:8080/video")
        thread1.start()
        thread2.start()
        thread3.start()
        
        
    elif option == 2:
        # live stream
        windowName1 = "Live Stream Camera 1"
        cv2.namedWindow(windowName1)
        
        capture1 = cv2.VideoCapture(0) #laptop 
        capture2 = cv2.VideoCapture("http://10.130.19.50:8080/video")  # mobile's camera

        if capture1.isOpened():  # check if feed exists or not for camera 1
            ret1, frame1 = capture1.read()
        else:
            ret1 = False

        while ret1:  # and ret2 and ret3:
            ret1, frame1 = capture1.read()
            cv2.imshow(windowName1, frame1)

            if cv2.waitKey(1) == 27:
                break

        capture1.release()
        cv2.destroyAllWindows()

    else:
        print("Invalid option entered. Exiting...")


main()
