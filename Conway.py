import pygame, copy, random
width = 9
height = 9
pygame.init()
i=0
k=-11
block_size=22
next_fig = []
for x in range(width):
  column = []
  for y in range(height):
    if(random.randint(0,1)==0):
      column.append(0)
    else:
      column.append(1)
  next_fig.append(column)

screen = pygame.display.set_mode((940,700))
color_red = (255,0,0)
color_green = (155,235,0)
color_blue = (0,0,255)
color_custom = (221,148,221)

while(i<12):
  now_fig = copy.deepcopy(next_fig)
  if(i%4==0):
    j=0
    k+=11
  m=block_size*j
  n=block_size*k


  for x in range(width):
    for y in range(height):
      rect = pygame.Rect(m,n,block_size,block_size)
      if(now_fig[x][y]==0):
        if(i%3==0):
          pygame.draw.rect(screen,color_red,rect,2)
        elif(i%3==1):
          pygame.draw.rect(screen,color_green,rect,2)
        else:
          pygame.draw.rect(screen,color_blue,rect,2)
      else:
        pygame.draw.rect(screen,color_custom,rect)
      m+=block_size
    n+=block_size
    m=block_size*j


  for x in range(width):
    for y in range(height):
      cd_left = (x - 1) % width
      cd_right = (x + 1) % width
      cd_up = (y - 1) % height
      cd_down = (y + 1) % height

      numNeighbors = 0
      if now_fig[cd_left][cd_up] == 1: #top-left
        numNeighbors += 1
      if now_fig[x][cd_up] == 1: #top
        numNeighbors += 1
      if now_fig[cd_right][cd_up] == 1: #top-right
        numNeighbors += 1
      if now_fig[cd_left][y] == 1: #left
        numNeighbors += 1
      if now_fig[cd_right][y] == 1: #right
        numNeighbors += 1
      if now_fig[cd_left][cd_down] == 1: #bottom-left
        numNeighbors += 1
      if now_fig[x][cd_down] == 1: #bottom
        numNeighbors += 1
      if now_fig[cd_right][cd_down] == 1: #bottom-right
        numNeighbors += 1

      if now_fig[x][y] == 1 and (numNeighbors == 2 or numNeighbors == 3):
        next_fig[x][y] = 1
      elif now_fig[x][y] == 0 and numNeighbors == 3:
        next_fig[x][y] = 1
      else:
        next_fig[x][y] = 0
  j+=11
  i+=1


Clock = pygame.time.Clock()
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    pygame.display.update()
pygame.quit()
