import pygame
import gl_objects
import math

def rotate2d(pos,rad): x,y = pos; s,c = math.sin(rad), math.cos(rad); return x*c-y*s,y*c+x*s

pygame.init()
w = 400; h = 400; a = w//2; b = h//2
display = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()

pi = math.pi

##quads = [gl_objects.Quad(4,0,0,1,0,0),
##         gl_objects.Quad(4,0,0,-1,0,0),
##         gl_objects.Quad(4,1,0,0,0,pi/2),
##         gl_objects.Quad(4,-1,0,0,0,pi/2),
##         gl_objects.Quad(4,0,1,0,pi/2,0),
##         gl_objects.Quad(4,0,-1,0,pi/2,0)
##         ]

quads = [gl_objects.Quad(1,0,0,0,0,pi/2),
         gl_objects.Quad(1,0,0,0,pi/2,0)]

camera = gl_objects.Camera()

pygame.event.get(); pygame.mouse.get_rel()
pygame.mouse.set_visible(0); pygame.event.set_grab(1)

currentInterval = 0

focus = True

running = True
while(running):
    delta = clock.tick()/1000
    
    currentInterval+=delta
    if currentInterval >= 1:
        currentInterval = 0
        pygame.display.set_caption("3dQuadDrawing | %.00f fps" % (clock.get_fps()))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False; break
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: pygame.quit()

            if event.key == pygame.K_f:
                if focus:
                    pygame.event.set_grab(0)
                    pygame.mouse.set_visible(1)
                else:
                    pygame.event.set_grab(1)
                    pygame.mouse.set_visible(0)
                focus = not focus
        if focus:
            camera.events(event)

    display.fill((255,255,255))

    #for quad in quads:
    for q in range(len(quads)):
        quad = quads[q]

        #print("%f" % (camera.z))
        quad.update_verts()
        
        
##        quad_x = quad.x-camera.x
##        quad_y = quad.y-camera.y
##        quad_z = quad.z-camera.z

        verts = quad.get_verts_transformed(quad.x-camera.x, quad.y-camera.y, quad.z-camera.z)

        for vert in verts:
            vert[0],vert[2] = rotate2d((vert[0],vert[2]), camera.ry)
            vert[1],vert[2] = rotate2d((vert[1],vert[2]), camera.rx)

        vert0 = verts[0]
        vert1 = verts[1]
        vert2 = verts[2]
        vert3 = verts[3]

#       https://youtu.be/g4E9iq0BixA?t=107

        #quad_x-=camera.x; quad_y-=camera.y; quad_z-=camera.z

        focal = 200

        #f = 200/quad_z
        f0 = focal/vert0[2]
        f1 = focal/vert1[2]
        f2 = focal/vert2[2]
        f3 = focal/vert3[2]

        vert0_x = vert0[0] * f0
        vert0_y = vert0[1] * f0
        #vert0_z = f/quad.verts[0][2]

        vert1_x = vert1[0] * f1
        vert1_y = vert1[1] * f1
        #vert1_z = quad.verts[1][2]

        vert2_x = vert2[0] * f2
        vert2_y = vert2[1] * f2
        #vert2_z = quad.verts[2][2]

        vert3_x = vert3[0] * f3
        vert3_y = vert3[1] * f3
        #vert3_z = quad.verts[3][2]

        pygame.draw.polygon(display, (255*(q/len(quads)),0,50), [
            (
            vert0_x+a,(h-vert0_y+b)-h
            ),
            (
            vert1_x+a,(h-vert1_y+b)-h
            ),
            (
            vert2_x+a,(h-vert2_y+b)-h
            ),
            (
            vert3_x+a,(h-vert3_y+b)-h
            ),
            (vert0_x+a,(h-vert0_y+b)-h
            )
            ], 0)

        
##        pygame.draw.aaline(display, (0,0,0), (vert0_x+a,(h-vert0_y+b)-h), (vert1_x+a,(h-vert1_y+b)-h), 1)
##        pygame.draw.aaline(display, (0,0,0), (vert1_x+a,(h-vert1_y+b)-h), (vert2_x+a,(h-vert2_y+b)-h), 1)
##        pygame.draw.aaline(display, (0,0,0), (vert2_x+a,(h-vert2_y+b)-h), (vert3_x+a,(h-vert3_y+b)-h), 1)
##        pygame.draw.aaline(display, (0,0,0), (vert3_x+a,(h-vert3_y+b)-h), (vert0_x+a,(h-vert0_y+b)-h), 1)

    onQuad = 0
    
    if running:
        pygame.display.flip()

        key = pygame.key.get_pressed()
        camera.move(delta, key)

pygame.quit()
