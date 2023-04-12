import matplotlib.pyplot as plt
import numpy             as np
import noise


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

height = len(grid   )
width  = len(grid[0])

# values = np.zeros( (width, height) )
values = np.zeros( (height, width) )


# print(f'Size: {width}x{height}')

# img = Image.new('L', (width, height) ) # L = grayscale (rather than RGB)

for x in range(width):
    for y in range(height):
#       print(127 + int(127* noise.snoise2(x,y)))

        if grid[y][x]:
#          noise_val = int(255 * noise.snoise2(x/300, y/300, octaves=4, persistence=0.2, lacunarity=0.8, repeatx=width, repeaty=height))
           noise_val =           noise.snoise2(x/300, y/300, octaves=4, persistence=0.2, lacunarity=0.8, repeatx=width, repeaty=height)
           values[y, x] = noise_val



plt.figure(figsize=(width, height))
plt.imshow(values, cmap = 'gist_stern')

plt.axis('off')
plt.show()

# plt.imshow(grid
# img.show()
