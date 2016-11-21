import abc


class CameraBase(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def save_snapshot(self):
        pass

    def __init__(self):
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
