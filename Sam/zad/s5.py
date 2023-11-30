class Camera:
    def take_picture(self):
        print('фотографирую')

    def get_resolution(self):
        print('разрешение недоступно')


class Phone:
    def call(self):
        print('зовущий')

    def charge(self):
        print('зарядка')

class CameraPhone(Camera, Phone):
    pass

camera_phone = CameraPhone()
camera_phone.take_picture()
camera_phone.get_resolution()
camera_phone.call()
camera_phone.charge()