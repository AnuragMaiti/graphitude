months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]
colorPalette = ["#55efc4", "#81ecec", "#a29bfe", "#ffeaa7", "#fab1a0", "#ff7675", "#fd79a8",
                "#651fc4", "#91ec1c", "#b29b1e", "#ff1ab7", "#1ab120", "#f17685", "#fd89b8",
                "#762fc4", "#11ec2c", "#c29b2e", "#ff2ac7", "#2ab130", "#f27695", "#fd19c8",
                "#853fc4", "#21ec3c", "#d29b3e", "#ff3ad7", "#3ab140", "#f37615", "#fd29d8",
                "#954fc4", "#31ec4c", "#e29b4e", "#ff4ae7", "#4ab150", "#f47625", "#fd39e8",
                "#a55fc4", "#41ec5c", "#f29b5e", "#ff5af7", "#5ab160", "#f57635", "#fd4918",
                "#b56fc4", "#51ec6c", "#129b6e", "#ff6a17", "#6ab170", "#f67645", "#fd5928",
                "#c57fc4", "#61ec7c", "#229b7e", "#ff7a27", "#7ab180", "#f77655", "#fd6938",
                "#d58fc4", "#a1ec8c", "#329b8e", "#ff8a37", "#8ab190", "#f87665", "#fda948",
                "#e59fc4", "#b1ec9c", "#429b9e", "#ff9a47", "#9ab1c0", "#f97675", "#fdb958",
                "#150fc4", "#c1ec0c", "#529b0e", "#ff0a57", "#0ab1d0", "#f07685", "#fdc968",
                "#25afc4", "#d1ecac", "#629bae", "#ffaa67", "#aab1e0", "#fa7695", "#fdd978"]
colorPrimary, colorSuccess, colorDanger = "#79aec8", colorPalette[0], colorPalette[5]


def get_year_dict():
    year_dict = dict()

    for month in months:
        year_dict[month] = 0

    return year_dict


def generate_color_palette(count):
    palette = []

    i = 0
    while i < len(colorPalette) and len(palette) < count:
        palette.append(colorPalette[i])
        i += 1
        if i == len(colorPalette) and len(palette) < count:
            i = 0

    return palette
