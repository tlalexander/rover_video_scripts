from vito import flowutils
from vito import imvis

# Load optical flow file
flow = flowutils.floread('flow/out_00000_middlebury.flo')
print(flow)
# Colorize it
colorized = flowutils.colorize_flow(flow)
imvis.imshow(colorized)