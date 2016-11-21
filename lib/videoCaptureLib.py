import VideoCapture

from abstractCamera import CameraBase


class Camera(CameraBase):
    def __init__(self):
        super(Camera, self).__init__()

    def save_snapshot(self):
        first_snapshot = {"success": True}
        second_snapshot = {"success": True}

        try:
            cam = VideoCapture.Device(devnum=int(self.primary_camera))
            cam.getImage().save(self.primary_camera_image_path)
            del cam
        except Exception as e:
            first_snapshot["success"] = False

        try:
            cam = VideoCapture.Device(devnum=int(self.secondary_camera))
            cam.getImage().save(self.secondary_camera_image_path)
            del cam
        except Exception as e:
            second_snapshot["success"] = False

        return first_snapshot, second_snapshot
