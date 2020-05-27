import pyqrcode

class locationCode:
    def __init__(self, X,Y,Z,rX=0,rY=0,rZ=0,size=13):
        self.X = X
        self.Y = Y
        self.Z = Z
        self.rX = rX
        self.rY = rY
        self.rZ = rZ
        self.sizeQR = size

    def createQR(self):
        print("Creation Started")
        big_code = pyqrcode.create(str(self.X)+";"+str(self.Y)+";"+str(self.Z)+";"+str(self.rX)+";"+str(self.rY)+";"+str(self.rZ)+";"+str(self.sizeQR), error='Q')
        big_code.png('code.png', scale=20, module_color=[0, 0, 0, 128], background=[0xFF, 0xff, 0xff])
        print("The QR-code should be made...")

qr = locationCode(0,0,0)
qr.createQR()