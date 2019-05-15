

import tempfile
from pyfingerprint.pyfingerprint import PyFingerprint


try:
    f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

    if ( f.verifyPassword() == False ):
        raise ValueError('The given fingerprint sensor password is wrong!')

except Exception as e:
    print('The fingerprint sensor could not be initialized!')
    print('Exception message: ' + str(e))
    exit(1)


print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))


try:
    print('Waiting for finger...')

   
    while ( f.readImage() == False ):
        pass

    print('Downloading image (this take a while)...')

    imageDestination =  tempfile.gettempdir() + '/fingerprint.bmp'
    f.downloadImage(imageDestination)

    print('The image was saved to "' + imageDestination + '".')

except Exception as e:
    print('Operation failed!')
    print('Exception message: ' + str(e))
    exit(1)
