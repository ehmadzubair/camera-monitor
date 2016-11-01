import VideoCapture


class Camera(object):
    def __init__(self):
        self._videoCapture = None
        self._primary_camera = None
        self._secondary_camera = None
        self._primary_camera_image_path = None
        self._secondary_camera_image_path = None

    @property
    def primary_camera(self):
        return self._primary_camera

    @primary_camera.setter
    def primary_camera(self, value):
        self._primary_camera = value

    @property
    def secondary_camera(self):
        return self._secondary_camera

    @secondary_camera.setter
    def secondary_camera(self, value):
        self._secondary_camera = value

    @property
    def primary_camera_image_path(self):
        return self._primary_camera_image_path

    @primary_camera_image_path.setter
    def primary_camera_image_path(self, value):
        self._primary_camera_image_path = value

    @property
    def secondary_camera_image_path(self):
        return self._secondary_camera_image_path

    @secondary_camera_image_path.setter
    def secondary_camera_image_path(self, value):
        self._secondary_camera_image_path = value

    def save_snapshot(self):
        first_snapshot = {"success": True}
        second_snapshot = {"success": True}

        try:
            self._videoCapture = VideoCapture.Device(devnum=int(self.primary_camera))
            self._videoCapture.getImage().save(self.primary_camera_image_path)
            self._videoCapture = None
        except Exception as e:
            print e.message
            first_snapshot["success"] = False
            first_snapshot["error"] = e.message
            self._videoCapture = None

        try:
            self._videoCapture = VideoCapture.Device(devnum=int(self.secondary_camera))
            self._videoCapture.getImage().save(self.secondary_camera_image_path)
            self._videoCapture = None
        except Exception as e:
            print e.message
            second_snapshot["success"] = False
            second_snapshot["error"] = e.message
            self._videoCapture = None

        return first_snapshot, second_snapshot
