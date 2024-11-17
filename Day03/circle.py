import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--radius", help="the radius of a given circle", type = int, required = True)
args = parser.parse_args()

radius = args.radius

pi = 3.1415926
area = pi*radius**2
print(area)