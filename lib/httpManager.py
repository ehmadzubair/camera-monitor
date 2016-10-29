import os
import re
import time

import requests


class Http(object):
    def __init__(self):
        self._url = None
        self._primary_camera_image = None
        self._secondary_camera_image = None

    @property
    def http_host(self):
        return self._url

    @http_host.setter
    def http_host(self, value):
        regex = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        m = regex.match(value)
        if m is False:
            print "Error: Invalid HTTP_HOST({}) url.".format(value)
            exit(0)

        self._url = value

    @property
    def primary_camera_image_path(self):
        return self._primary_camera_image

    @primary_camera_image_path.setter
    def primary_camera_image_path(self, value):
        self.remove_image(value)
        self._primary_camera_image = value

    @property
    def secondary_camera_image_path(self):
        return self._secondary_camera_image

    @secondary_camera_image_path.setter
    def secondary_camera_image_path(self, value):
        self.remove_image(value)
        self._secondary_camera_image = value

    def host_alive(self):
        try:
            response = requests.head(self.http_host)
            return response.status_code == 200
        except requests.ConnectionError:
            return False

    def remove_image(self, image):
        try:
            os.remove(image)
        except OSError:
            pass

    def send_data(self, first_response, second_response):

        payload_data = {"image_date": str(time.strftime('%Y-%m-%d %H:%M:%S'))}
        payload_file = {}

        if first_response['success'] is True:
            try:
                payload_file["primary_image"] = open(self.primary_camera_image_path, "rb")
            except Exception as e:
                payload_data["error"] += e.message

        if second_response['success'] is True:
            try:
                payload_file["secondary_image"] = open(self.secondary_camera_image_path, "rb")
            except Exception as e:
                payload_data["error"] += e.message

        response = requests.post(self.http_host, data=payload_data, files=payload_file)
        if response.status_code == 200:
            print "All process completed"
