#!/usr/bin/env python3

# Created by: DJ Watson
# Created on: September 2019
# This program calculates the surface area of triangular prism with user input


def main():
    # input
    length = int(input("height of base: "))
    width = int(input("width of pyramid: "))
    height = int(input("height of pyramid (face): "))
    # process
    area = length*width+(3/2)*(width*height)
    # output
    print("SURFACE AREA: {}cm²".format(area))


if __name__ == "__main__":
    main()
