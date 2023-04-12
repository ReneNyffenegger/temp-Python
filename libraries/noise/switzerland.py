import noise
import numpy
from PIL import Image

gridStr = '''
                                        xx                             
                                       xxxx                            
                                      xxxxx x                          
                                      xxxxxxxx xx                      
                                         xxxxxxxxxxx                   
                         xx  xx   xxx  x xxxxxxxxxxxx                  
                        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx                 
                xxxx   xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx               
                xxxx   xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx             
               xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx             
               xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx             
                 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx              
                xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx               
               xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx               
              xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx              
             xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx              
            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx             
            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx            
           xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx       xx 
         xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx       xx 
        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx   xxxxx
        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  xxxxx
        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx 
        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx 
       xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx 
     xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  xxxx
   xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx   xxx
  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx       
  xxxxxx    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx x xxxxxxxxx       
  xxxx        xxxxxxxxxxxxxxxxxxxxxxxx xxxxxxxxxxxxx  xxxxxxxxxxxx     
   xx        xxxxxxxxxxxxxxxxxxxxxxxx  xxxxxxxxxxxxx   xxxxx   xxx     
   x        xxxxxxxxxxxxxxxxxxxxxxxx   xxxxxxxxxxxxxx  xxxxx   xx      
  xx         xxxxxxxxxxxxxxxxxxxxxxx   xxxxxxxxxxxxx    xxx    xxx     
 xx xx        xxxxxxxxxxxxxxxxxxxx     xxxxxxxxxxxxx            xx     
xxxxx        xxxxxxxxxxxxxxxxxxxxxx    xxxxxxxxxxxx             x      
xxxx         xxxxxxxxxxxxxxxxxxxxxx    xxxxxxxxxxxx                    
             xxxxxxxxxxxxxxxxxxxxxx      xxxxxxxxx                     
              xxxxxxxxxxxxxxxxxxx         x xxxxx                      
              xxxxxxxxxxxxxxxxxxx            xxx                       
                xxxxxxxxxxxxxxxx            xxxxx                      
                 xxxxxxxx  xxxxx             xxx                       
                 xxxxxx     xx                xxx                      
                  x                           xxx                      
                                               xx                      '''


lines = gridStr.splitlines()[1:] # Remove first line

grid = [ [ False if cell==' ' else True  for cell in line ] for line in lines]

# print(grid)

width  = len(grid[0])
height = len(grid   )

img = Image.new('L', (width, height) ) # L = grayscale (rather than RGB)

for x in range(width):
    for y in range(height):
#       print(127 + int(127* noise.snoise2(x,y)))

        if grid[y][x]:
           img.putpixel( (x, y), 127 + int(127*noise.snoise2(x,y)))
        else:
           img.putpixel( (x, y), 0)


img.show()





# print(arr)

# nparr = numpy.array(arr)
# Image.fromarray(nparr, mode='L').show()

#  grid = 
#  
#  import noise
#  import numpy as np
#  
#  # Set the size of the 2D array
#  size = (10, 10)
#  
#  # Create an empty array of the desired size
#  arr = np.zeros(size)
#  
#  # Fill the array with random values generated using Perlin noise
#  for i in range(size[0]):
#      for j in range(size[1]):
#          arr[i][j] = noise.snoise2(i/5, j/5)
#  
#  # Print the array
#  print(arr)
