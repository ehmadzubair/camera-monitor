import VideoCapture


class Camera(object):
    def __init__(self):
        self._videoCapture = None
        self._primary_camera_image = None
        self._secondary_camera_image = None

    @property
    def primary_camera_image(self):
        return self._primary_camera_image

    @primary_camera_image.setter
    def primary_camera_image(self, value):
        self._primary_camera_image = value

    @property
    def secondary_camera_image(self):
        return self._secondary_camera_image

    @secondary_camera_image.setter
    def secondary_camera_image(self, value):
        self._secondary_camera_image = value

    @property
    def primary_camera_image_path(self):
        return self._primary_camera_image

    @primary_camera_image_path.setter
    def primary_camera_image_path(self, value):
        self._primary_camera_image = value

    @property
    def secondary_camera_image_path(self):
        return self._secondary_camera_image

    @secondary_camera_image_path.setter
    def secondary_camera_image_path(self, value):
        self._secondary_camera_image = value

    def save_snapshot(self):
        first_snapshot = {"success": True}
        second_snapshot = {"success": True}

        try:
            self._videoCapture = VideoCapture.Device(devnum=self.primary_camera_image)
            self._videoCapture.getImage().save(self.primary_camera_image_path)
            self._videoCapture = None
        except Exception as e:
            print e.message
            first_snapshot["success"] = False
            first_snapshot["error"] = e.message
            self._videoCapture = None

        try:
            self._videoCapture = VideoCapture.Device(devnum=self.secondary_camera_image)
            self._videoCapture.getImage().save(self.secondary_camera_image)
            self._videoCapture = None
        except Exception as e:
            print e.message
            second_snapshot["success"] = False
            second_snapshot["error"] = e.message
            self._videoCapture = None

        return first_snapshot, second_snapshot
