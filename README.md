# 3dPython

**Overview**
  This is a 3d concept written in Python with the Pygame module

  Open the main.py

  w/a/s/d : directional movement
  space/shift : ascend/descend
  mouse : look around
  f : focus/unfocus
  esc : exit



**ChangeLog:**

  added v1.4, only triangles work now
  
  semi-patched the mirroring/clipped verts issue (verts which would clip don't get drawn)
  
  objects stored in a file "map.json"



**ToDo:**

  ~implement new way to create / draw quads.~
  
  probably stop using python for this (as python is slower)

  fix the entire issue with triangles clipping. 
  
  create some model from the triangles to show what this is capable of
  
  implement a depth buffer
  
  physics (gravity, jumping, smooth walking...)
  
  dividing by zero errors
  
  perspective is clunky with objects when looked at a certain way in corner of screen
