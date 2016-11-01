import ConfigParser
import os
import sys

from lib.cameraManager import Camera
from lib.httpManager import Http

BASE_DIR = os.getcwd()
config_file = os.path.join(BASE_DIR, 'config.ini')
primary_camera_image = os.path.join(BASE_DIR, 'primary_camera_image.jpg')
secondary_camera_image = os.path.join(BASE_DIR, 'secondary_camera_image.jpg')
error_msg = []


class CameraMonitor(object):
    def __init__(self):
        if os.path.isfile(config_file) is False:
            print "Error: config.ini file doesn't exits in current directory({})".format(BASE_DIR)
            sys.exit(0)
        self._parser = ConfigParser.ConfigParser()
        self._parser.read(config_file)
        # Validating the HTTP_HOST
        self._http = Http()
        self._http.http_host = self._parser.get('setting', 'HTTP_HOST')
        self._http.primary_camera_image_path = primary_camera_image
        self._http.secondary_camera_image_path = secondary_camera_image
        self._http.id = int(self._parser.get('setting', 'ROOM_ID'))

        self._camera = Camera()
        self._camera.primary_camera = int(self._parser.get('setting', 'PRIMARY_CAMERA'))
        self._camera.secondary_camera = int(self._parser.get('setting', 'SECONDARY_CAMERA'))
        self._camera.primary_camera_image_path = primary_camera_image
        self._camera.secondary_camera_image_path = secondary_camera_image


    def run(self):
        if self._http.host_alive() is False:
            print "Error: HTTP_HOST({}) is not alive.".format(self._http.http_host)
            sys.exit(0)
        first_camera_res, secondary_camera_res = self._camera.save_snapshot()
        self._http.send_data(first_response=first_camera_res, second_response=secondary_camera_res)
        sys.exit(0)


if __name__ == "__main__":
    CameraMonitor().run()
