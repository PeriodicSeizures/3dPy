#First of all, initialize the depth of each pixel.
i.e,  d(i, j) = infinite (max length)
Initialize the color value for each pixel 
as c(i, j) = background color
for each polygon, do the following steps :

for (each pixel in polygon's projection)
{
    find depth i.e, z of polygon
    at (x, y) corresponding to pixel (i, j)
    
    if (z < d(i, j))
    {
        d(i, j) = z;
        c(i, j) = color;
    }
}
