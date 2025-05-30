
# Topographical Line Image Generator

Generator for topographical line images, like: 
<br><img src="https://github.com/FilNez/TopographicalLineImageGenerator/blob/main/output_examples/example1.png" alt="Output example" width="500" height="250">

Program's algorithm:
1. Create Perlin noise
2. Normalize Perlin noise and convert it to image
3. Posterize the image
4. Edge detection
5. Draw background and lines based on the detected edges

More information about perlin noise: [Perlin noise generator by pvigier](https://github.com/pvigier/perlin-numpy)

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required libraries.
```bash
pip install pillow
pip install perlin-numpy
```

Download `.py` project file.
Import it into your python program


## Usage

Import python file
```python
from path/to/file/TopographicalLineImageGenerator import create_topographic_line_image

image = create_topographic_line_image(...)
```

# Function parameters

- width: output image width
- height: output image height
- background_color: color of background (RGBA)
- line_color: color of topographic lines (RGBA)
- line_width: width of topographic lines in pixels (int)
- noise_octaves: number of layers of Perlin noise that are combined, higher = more detailed (int)
- noise_persistence: amplitude of each successive Perlin noise octave, lower = smoother (float 0-1)
- color_levels: amount of colors in posterized image, higher = more lines (int 1-255)
- full_save_path: path image will be saved to, if not filled image won't be saved as a file (str)

## Examples

Example 1
- Default Perlin noise and posterization parameters

<br><img src="https://github.com/FilNez/TopographicalLineImageGenerator/blob/main/output_examples/example1.png?" alt="Output example" width="500" height="250">
```python
create_topographic_line_image(
    width=1024, height=512,
    line_width=3,
    background_color=(123, 123, 133, 255),
    line_color=(29, 25, 39, 255),
    full_save_path="output_examples/example1.png"
)
```


Example 2
- Tranparent background
- less Perlin noise octaves (smoother lines)

<br><img src="https://github.com/FilNez/TopographicalLineImageGenerator/blob/main/output_examples/example2.png?" alt="Output example" width="500" height="250">
```python
create_topographic_line_image(
    width=1024, height=512,
    line_width=3,
    noise_octaves=2,
    background_color=(0, 0, 0, 0),
    line_color=(123, 255, 198, 255),
    full_save_path="output_examples/example2.png"
)
```


Example 3
- Transparent lines
- More  Perlin noiseoctaves (more details)
- Higher Perlin noise persistence (less smooth)

<br><img src="https://github.com/FilNez/TopographicalLineImageGenerator/blob/main/output_examples/example3.png?" alt="Output example" width="500" height="250">
```python
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
