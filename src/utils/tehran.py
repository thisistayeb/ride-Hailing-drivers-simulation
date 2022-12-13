"""module generates random geo-points in Tehran."""
from shapely import geometry

from .randpoint import gen_rand_point_shape

tehran_center = [
    [35.70622273732417, 51.44011973787947],
    [35.76988603814731, 51.469862067348124],
    [35.79075427647057, 51.41600433585597],
    [35.768861117489344, 51.410721914430304],
    [35.776780615627786, 51.38947739347925],
    [35.70081413892862, 51.377075186810785],
]


def check_traffic_area(location: tuple[float, float]) -> bool:
    """Indicate if the location is inside Tehran's traffic area."""
    traffic_points = [
        [35.7237995, 51.4409494],
        [35.7244615, 51.4370441],
        [35.7237647, 51.4104366],
        [35.7228937, 51.4093208],
        [35.7209774, 51.4085913],
        [35.7142527, 51.3894081],
        [35.7011152, 51.3912106],
        [35.6909731, 51.392498],
        [35.6754961, 51.394515],
        [35.6674078, 51.3956308],
        [35.6614805, 51.3964033],
        [35.6590397, 51.3981199],
        [35.6580634, 51.4080763],
        [35.6585515, 51.4120674],
        [35.6587259, 51.4159727],
        [35.6595627, 51.4280748],
        [35.659493, 51.4348555],
        [35.6606785, 51.4450264],
        [35.6735786, 51.4461422],
        [35.6964102, 51.4478588],
        [35.7019864, 51.4481592],
        [35.6992332, 51.4388895],
        [35.6992332, 51.4372158],
        [35.7061335, 51.4402628],
        [35.7067259, 51.439662],
        [35.706691, 51.4382029],
        [35.706482, 51.4345551],
        [35.7068304, 51.4338684],
        [35.7118832, 51.4373446],
        [35.7153677, 51.4393616],
        [35.7172493, 51.4406919],
        [35.7178068, 51.439147],
        [35.7237995, 51.4409494],
    ]
    traffic_area = geometry.Polygon(traffic_points)
    point = geometry.Point(location)
    return point.within(traffic_area)


def check_airpollution_area(location: tuple[float, float]) -> bool:
    """Indicate if the location is inside Tehran's air pollution area."""
    airpollution_points = [
        [35.7575179, 51.4850235],
        [35.7593289, 51.4824486],
        [35.7591896, 51.478672],
        [35.7569607, 51.4719772],
        [35.7564035, 51.4656258],
        [35.7555677, 51.4551544],
        [35.7513884, 51.4484596],
        [35.7506918, 51.4403915],
        [35.7497166, 51.437645],
        [35.74902, 51.4280319],
        [35.7497166, 51.4215088],
        [35.7522243, 51.4156723],
        [35.7512491, 51.404171],
        [35.7504132, 51.3868332],
        [35.7421932, 51.3839149],
        [35.7279803, 51.3832283],
        [35.7221272, 51.3796234],
        [35.7178068, 51.3779068],
        [35.7010803, 51.3782501],
        [35.6545066, 51.3820267],
        [35.6453002, 51.3933563],
        [35.6494851, 51.3979912],
        [35.6455792, 51.4324951],
        [35.6451607, 51.4446831],
        [35.6458582, 51.4542961],
        [35.6423707, 51.4637375],
        [35.6531118, 51.4606476],
        [35.6595279, 51.4606476],
        [35.6663618, 51.4647675],
        [35.6698483, 51.4651108],
        [35.6759841, 51.458931],
        [35.6825378, 51.4604759],
        [35.6886726, 51.4570427],
        [35.694807, 51.4565277],
        [35.6985711, 51.4577293],
        [35.7056804, 51.457386],
        [35.7154374, 51.456871],
        [35.7197579, 51.4637375],
        [35.7239389, 51.4707756],
        [35.7293738, 51.4772987],
        [35.7338329, 51.4815903],
        [35.7368985, 51.4831352],
        [35.7472089, 51.4829636],
        [35.7526422, 51.4857101],
        [35.7575179, 51.4850235],
    ]
    airpollution_area = geometry.Polygon(airpollution_points)
    point = geometry.Point(location)
    return point.within(airpollution_area)


def random_req_tehran() -> tuple[float, float]:
    """Generate random geo-points in the favored district."""
    random_location = gen_rand_point_shape(tehran_center)
    return random_location