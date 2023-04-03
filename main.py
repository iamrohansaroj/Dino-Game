import pyautogui
from PIL import Image,ImageGrab
#from numpy import asarray
import time

def hit(key):
    pyautogui.keyDown(key)
    return
    
def isCollide(data):
    for i in range(300, 415):
        for j in range(425, 576):
            if data[i, j] < 100:
                hit("down")
                return 
                
    for i in range(305, 425): 
        for j in range(576, 665):
            if data[i, j] < 100:
                hit("up")
                return 
    return False
    
    
    
if __name__=="__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(2)
    #hit('up')
    
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)
            
        #print(asarray(image))
        
        
        # for i in range(305, 425):
        #     for j in range(576, 665):
        #         data[i, j] = 0
        '''        
        for i in range(255, 305):
            for j in range(425, 576):
                data[i, j] = 171
                
                
        image.show()
        break
        '''