
# Topographical Line Image Generator

Generator for topographical line images, like: 
<br><img src="https://github.com/FilNez/TopographicalLineImageGenerator/blob/main/output_examples/example1.png" alt="Output example" width="500" height="250">


## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required libraries.
```bash
pip install pillow
pip install perlin-numpy
```


Download `.py` project file.
Import it into your python program


## Usage/Examples

Import python file
```python
from path/to/file/TopographicalLineImageGenerator import create_topographic_line_image
```


Example 1
<br><img src="https://github.com/FilNez/TopographicalLineImageGenerator/blob/main/output_examples/example1.png" alt="Output example" width="500" height="250">
```python
# example 1
create_topographic_line_image(
    width=1024, height=512,
    line_width=3,
    background_color=(123, 123, 133, 255),
    line_color=(29, 25, 39, 255),
    full_save_path="output_examples/example1.png"
)
```


Example 2
<br><img src="https://github.com/FilNez/TopographicalLineImageGenerator/blob/main/output_examples/example2.png" alt="Output example" width="500" height="250">
```python
# example 2
create_topographic_line_image(
    width=1024, height=512,
    line_width=2,
    noise_octaves=5,
    background_color=(123, 255, 198, 255),
    line_color=(29, 25, 39, 255),
    full_save_path="output_examples/example2.png"
)
```


Example 3
<br><img src="https://github.com/FilNez/TopographicalLineImageGenerator/blob/main/output_examples/example3.png" alt="Output example" width="500" height="250">
```python
# example 3
create_topographic_line_image(
    width=1024, height=512,
    line_width=3,
    noise_octaves=6,
    noise_persistence=.25,
    color_levels=8,
    background_color=(255, 123, 198, 255),
    line_color=(29, 25, 39, 0),
    full_save_path="output_examples/example3.png"
)
```


## Acknowledgements

 [Perlin noise generator by pvigier](https://github.com/pvigier/perlin-numpy)
