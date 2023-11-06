import random
import pygame
import time

pygame.init()

screen_size = (400, 420)
screen = pygame.display.set_mode(screen_size)


def rand_arr(num):

    arr = []
    for i in range(num):
        arr.append(random.randint(1, 400))

    return arr


def update_screen(arr, num):
    screen.fill((255, 255, 255))

    count = 0
    width = 400 / num
    for var in arr:
        pygame.draw.rect(screen, (255, 0, 0), (width * count, 420 - var, width, var), 2)   # draws rectangles that fill the whole screen, the height of their number in array
        count += 1

    pygame.display.update()





def main(running):
    num = 20

    arr = rand_arr(num)


    while(running):
        for event in pygame.event.get():                # I will fix logic at some point, now this only checks once, sim runs, and then it doesnt check
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False


        #print(f"arr is: {arr[1]}")

        for i in range(len(arr)-1):

            if arr[i] < arr[i+1]:
                continue
            else:
                arr = sort(arr)



def sort(arr):

    update_screen(arr, len(arr))

    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
            update_screen(arr, len(arr))
            time.sleep(0.3)

    return arr





main(running=True)
