import os
from camera.models import Cameras, Videos, Scanners
import datetime
import cv2
from .cloudos.cloudStorage import uploadToCloud

def getFileAge(file_path):
    return os.path.getmtime(file_path)

def mapping(folder_path):
    try:
        for root,directory,files in os.walk(folder_path):
                if files:
                    for file in files:
                        file_age = getFileAge(os.path.join(root,file))
                        file_age = datetime.datetime.now() - datetime.datetime.fromtimestamp(file_age)

                        if file_age < datetime.timedelta(seconds=15):
                            return TypeError("File is not old enough to upload")
                        else:
                            file_name = file
                            file_path_on_cloud = os.path.join(root,file).replace(folder_path,'./rtsp')
                            file_path_on_local = os.path.join(root,file)

                            video = cv2.VideoCapture(file_path_on_local)
                            frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)
                            fps = video.get(cv2.CAP_PROP_FPS)
                            video_duration = (frame_count/fps)

                            print("Frame count: {}".format(frame_count))
                            print("FPS: {}".format(fps))

                            start_time = file_name.split('.')[0].split('_')[1:]
                            start_time = '_'.join(start_time)
                            start_time = str(start_time)
                            end_time = datetime.datetime.strptime(start_time, '%Y-%m-%d_%H-%M-%S')
                            start_time = datetime.datetime.strptime(start_time, '%Y-%m-%d_%H-%M-%S')
                            
                            end_time = start_time + datetime.timedelta(seconds=video_duration)
                            end_time = str(end_time)

                            camera = Cameras.objects.filter(rtsp_path=file_path_on_local)
                            session_id = None # SessionID is null for testing
                            if camera:
                                machine_id = camera[0].machine_id
                            else:
                                machine_id = None
                            video = Videos.objects.create(
                                start_time=start_time,
                                end_time=end_time,
                                session_id=session_id,
                                video_path_local=file_path_on_local,
                                video_path_cloud=file_path_on_cloud,
                                machine_id=machine_id
                            )
                            video.save()
                            print("Video saved: {}".format(file_path_on_local))

                            uploadToCloud(file_path_on_local,file_path_on_cloud)
                            os.remove(file_path_on_local)
                            print("File deleted: {}".format(file_path_on_local))
    except Exception as e:
        print(e)

