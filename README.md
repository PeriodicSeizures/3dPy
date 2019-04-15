# 3dPython

As of the very near future, I will probably go ahead and stop uploading publicly because I plan to make this into a real epic serious game or something (in c++ of course).

**Overview**

  *Issues*:
  
    Timesteps need to be functional in physics (Already added, but test)
    
    Movement of player needs to be removed reworked... (put somewhere more effective, should not be in camera)
    put movement into a main update, not in cmera, because:
    
      Camera only renders based on its position...
      
    OR::::::::
    
      Merge RENDERER and CAMERA so that camera will render onto window
      
      Create separate object for player, and dont store as a vague object in objects.json
      
      Move camera from in player (Player will move camera)
      
      Put drawing window stuff ONLY in gl.py (including future camera and window_RENDERER)
      
      
    
    
    

  3d engine baseline written in Python. Can draw triangles and triangles only (all other shapes are *garbage*). 
  
  Physics in works
  
  I say *baseline* because I plan for a possible C++ implementation

    Open the main.py

    w/a/s/d : directional movement

    space/shift : ascend/descend

    mouse : look around

    f : focus/unfocus

    esc / top-right X : exit

![image0](controller.png?raw=true "img0")

![image1](physicsCalculations.png?raw=true "img1")

**To Do:**
  
  Textures? (will be laggy)
  
  ~depth buffer?~
  
  Dynamic physics. (jumping, functional collision)
  
  ~Fix perspective near screen border.~

  Fix spontaneous freezes (I have found out that this is caused by numbers divided by a small number, like x/.00001, which results in a very big number).
  
  Recreate in C++ for Ndless or whatever
  
  Implement LUT for faster maths.
  
  *More colors*
  
  Divide by 0 errors randomly occur again

**Patched issues**

  Verts no longer clip when out of view.
  
  Fixed perspective -- now looks as good as minecraft perspective
  
  ~No more divide by 0 errors.~
  
