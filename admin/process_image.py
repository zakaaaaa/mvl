"""Run in a separate process so rembg's memory is released after each upload.
Usage: process_image.py <src> <out_base> <logo> <remove_bg 0|1>
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import imgproc  # noqa: E402

src, out_base, logo, rb = sys.argv[1:5]
print(imgproc.process_upload(src, out_base, logo, remove_background=(rb == '1')))
