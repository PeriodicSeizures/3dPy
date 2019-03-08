# 3dPython

**Overview**

  This is a 3d concept which includes a *3d engine* WIP

    Open the main.py

    w/a/s/d : directional movement

    space/shift : ascend/descend

    mouse : look around

    f : focus/unfocus

    esc : exit



**ChangeLog:**

  1.4
    
    Game is now entirely triangles (I havnt experimented with shapes with more than 3 sides as of 1.4)
    
    Objects stored in map.json 
    
    Clipping issue partially solved, but is still a wip
    
    

**ToDo:**

  ~implement new way to create / draw quads.~
  
  ~probably stop using python for this (as python is slower)~
  
  implement textures

  fix the entire issue with triangles clipping. 
  
  create some model from the triangles to show what this is capable of
  
  ~implement a depth buffer~
  
  probably wont need a depth buffer due to the capabilities of triangles
  
  physics (gravity, jumping, smooth walking...)
  
  dividing by zero errors
  
  perspective is clunky with objects when looked at a certain way in corner of screen
