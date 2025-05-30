# Shape Square Calculation Library #

## What is this? ##
The test task which should calculate square of circle by its radius and triangle by its sides.

## Quick Guide ##
Set up the library

```
pip install shapesqr
```

Then import ShapeFabric from the library and pass into its constructor a tuple, containing one or three integers or floats.

```
from shapesqr import ShapeFabric


circle = ShapeFabric().get_shape((1.0,))

triangle = ShapeFabric().get_shape((4, 3, 5))
```


----------


### Using ###


Using the library is as simple and convenient as possible:

```
    from shapesqr import ShapeFabric


    circle = ShapeFabric().get_shape((1.0,))
    circle.get_shape_type()  # "circle"
    
    circle.calculate_square()
    status, result = circle.get_calculated_result()  # (1, 3.14...)

    triangle = ShapeFabric().get_shape((3, 4, 5))
    triangle.calculate_square()
    status, result = triangle.get_calculated_result()  # (1, 6)
    triangle.is_right()  # true
```


----------


## Developer ##
My site: [link](https://github.com/DmitriyReztsov) 