import pyqrcode

class locationCode:
    def __init__(self, X,Y,Z,rX=0,rY=0,rZ=0,size=13,name="code"):
        self.X = X
        self.Y = Y
        self.Z = Z
        self.rX = rX
        self.rY = rY
        self.rZ = rZ
        self.sizeQR = size
        self.name = name

    def createQR(self):
        print("Creation Started")
        big_code = pyqrcode.create("QRLOCSYS;"+str(self.X)+";"+str(self.Y)+";"+str(self.Z)+";"+str(self.rX)+";"+str(self.rY)+";"+str(self.rZ)+";"+str(self.sizeQR), error='Q')
        big_code.png(self.name+'.png', scale=20, module_color=[0, 0, 0, 128], background=[0xFF, 0xff, 0xff])
        print("The QR-code should be made...")

qr = locationCode(-5,4.95,0.5,0,0,-90,13,"QR_Code1")
qr.createQR()