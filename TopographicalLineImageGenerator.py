from PIL import Image, ImageDraw
import numpy as np
from perlin_numpy import generate_fractal_noise_2d


def get_posterized_image(img: Image, color_levels: int):
    """ image posterization function (reduces the amount of colors in the image to <color_levels>) """

    def get_posterized_color_map(color_levels):
        """ returns a map: pixel brightness -> posterized brightness """

        def to_8bit_format(value):
            """ makes sure the value fits 8bit image format (int 0-255) """
            if value < 0: return 0
            if value > 255: return 255
            return int(value)

        color_width = 256 / color_levels
        return tuple(to_8bit_format(i // color_width * color_width) for i in range(256))

    img = img.convert("L")  # converting to greyscale
    width, height = img.size

    image_pixels = img.load()  # getting image's pixels as an array
    new_img_arr = np.zeros((height, width))  # creating zero-filled array for the new image's pixels

    color_map = get_posterized_color_map(color_levels)  # map greyscale color -> posterized color

    for x in range(width):
        for y in range(height):
            px = image_pixels[x, y]
            new_img_arr[y, x] = color_map[px]

    return Image.fromarray(new_img_arr)


def normalize_for_image_processing(arr):
    """ normalizes noise values to fit image format (int 0-255) """
    arr_min = np.min(arr)
    arr_max = np.max(arr)
    diff_arr = arr_max - arr_min

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            value = arr[i, j]
            temp = ((value - arr_min) * 255) / diff_arr
            arr[i, j] = int(temp)
    return arr


def get_greyscale_img_edge_map(image: Image) -> np.array:
    """ simple edge detection, dont use for non-posterized images """
    width, height = image.size

    # converting to 1 channel greyscale, if it's not already
    if image.mode != "L":
        image.convert("L")

    image_pixels = image.load()

    edge_map = np.empty((width, height))

    for x in range(1, width):
        for y in range(1, height):
            edge_map[x, y] = int(
                image_pixels[x, y] != image_pixels[x - 1, y] or image_pixels[x, y] != image_pixels[x, y - 1])

    return edge_map


def draw_topographic_bg(edge_map, line_width=2, line_color=(255, 255, 255, 255), background_color=(0, 0, 0, 255)):
    width, height = edge_map.shape
    topographic_img = Image.new("RGBA", (width, height), background_color)
    draw = ImageDraw.Draw(topographic_img)

    for x in range(width):
        for y in range(height):
            if edge_map[x, y]:
                draw.circle((x - line_width, y - line_width, x + line_width, y + line_width), fill=line_color,
                            radius=line_width)

    return topographic_img


def create_topographic_line_image(width: int, height: int, background_color: tuple[int, int, int, int] = (0, 0, 0, 255),
                                  line_color: tuple[int, int, int, int] = (128, 128, 128, 255),
                                  line_width: int = 3, noise_octaves: int = 3, noise_persistence: float = .2,
                                  color_levels: int = 6, full_save_path: str = False) -> Image:
    """ function returning topographic image
    width: output image width
    height: output image height
    background_color: color of background (RGBA)
    line_color: color of topographic lines (RGBA)
    line_width: width of topographic lines in pixels (int)
    noise_octaves: number of layers of noise that are combined, higher=more detailed (int)
    noise_persistence: amplitude of each successive noise octave, lower=smoother (float 0-1)
    color_levels: amount of colors in posterized image, higher=more lines (int 1-255)
    full_save_path: path image will be saved to, if not filled image won't be saved as a file (str)
    """

    """ generation perlin noise """

    noise_size = 2 * max(
        1 << (width - 1).bit_length(),
        1 << (height - 1).bit_length()
    )  # getting square size for noise generator (2x for antialiasing)

    print("- generating perlin noise")
    noise = generate_fractal_noise_2d((noise_size, noise_size), (8, 8), noise_octaves, noise_persistence)

    """ normalizing noise to 8bit color format"""
    print("- normalizing noise")
    norm_noise = normalize_for_image_processing(noise)

    """ transforming noise array to image"""
    img = Image.fromarray(norm_noise)
    img = img.crop((0, 0, width * 2, height * 2))  # cropping to original size
    img.show()

    """ posterizing image """
    print("- posterizing")
    img_post = get_posterized_image(img, color_levels)
    img_post.show()

    print("- edge detection")
    edge_map = get_greyscale_img_edge_map(img_post)

    """ drawing lines and background """
    print("- drawing lines and background")
    result_img = draw_topographic_bg(edge_map, line_width, line_color, background_color)
    result_img = result_img.resize((width, height), Image.Resampling.LANCZOS)

    result_img.show()

    if full_save_path:
        try:
            print(f"- saving image to {full_save_path}")
            result_img.save(full_save_path)
        except Exception as e:
            print("Saving to file failed:", e, type(e))

    print("- generation complete")
    return result_img


if __name__ == '__main__':
    # example
    create_topographic_line_image(1920, 1080, line_width=6, background_color=(12, 12, 13, 255),
                                  line_color=(29, 25, 39, 255), full_save_path="topographic_image.png")
