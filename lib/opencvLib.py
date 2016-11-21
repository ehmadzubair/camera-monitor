import cv2

from abstractCamera import CameraBase


class Camera(CameraBase):
    def __init__(self):
        super(Camera, self).__init__()

    def save_snapshot(self):
        first_snapshot = {"success": True}
        second_snapshot = {"success": True}

        try:
            cam = cv2.VideoCapture(int(self.primary_camera))
            ret, image = cam.read()
            if ret is True:
                cv2.imwrite(self.primary_camera_image_path, image)
            cam.release()
            del cam
        except Exception as e:
            print e.message
            first_snapshot["success"] = False

        try:
            cam = cv2.VideoCapture(int(self.secondary_camera))
            ret, image = cam.read()
            if ret is True:
                cv2.imwrite(self.secondary_camera_image_path, image)
            cam.release()
            del cam
        except Exception as e:
            print e.message
            second_snapshot["success"] = False
        cv2.destroyAllWindows()
        return first_snapshot, second_snapshot
