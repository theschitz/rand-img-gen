from typing import Sequence
from PIL import Image
from random import randint
import hashlib

class RandomImage():
    mode = 'RGB'
    channels = 3
    width: int
    height: int
    image: Image
    

    def __init__(self, width=100, height=100) -> None:
        self.width = width
        self.height = height
        self.image = Image.new(self.mode, (self.width, self.height))
        seq = self.rand_sequence()
        hash = hashlib.md5(str(seq).encode('utf-8')).hexdigest()
        print(hash)
        self.image.putdata(seq)
        self.image.show()
        

    def rand_rgb(self) -> tuple:
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r, g, b)
    
    def rand_sequence(self):
        seq = []
        for _ in range(self.height):
            for __ in range(self.width):
                seq.append(self.rand_rgb())
        return tuple(seq)

if __name__ == "__main__":
    RandomImage()