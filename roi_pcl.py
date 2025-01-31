# 정의 
def do_passthrough(pcl_data,filter_axis,axis_min,axis_max):
    '''
    Create a PassThrough  object and assigns a filter axis and range.
    :param pcl_data: point could data subscriber
    :param filter_axis: filter axis
    :param axis_min: Minimum  axis to the passthrough filter object
    :param axis_max: Maximum axis to the passthrough filter object
    :return: passthrough on point cloud
    '''
    passthrough = pcl_data.make_passthrough_filter()
    passthrough.set_filter_field_name(filter_axis)
    passthrough.set_filter_limits(axis_min, axis_max)
    return passthrough.filter()


# 호출 
#cloud = input_pcl_xyzrgb
import pcl
cloud = pcl.load("/home/car/Downloads/rosbag_to_pcd/2022-09-25-15-49-54/778.812119100.pcd")


filter_axis = 'x'
axis_min = 1.0
axis_max = 20.0
cloud = filter.do_passthrough(cloud, filter_axis, axis_min, axis_max)

filter_axis = 'y'
axis_min = -7.0
axis_max = 5.5
cloud = filter.do_passthrough(cloud, filter_axis, axis_min, axis_max)

filter_axis = 'z'
axis_min = -1.2
axis_max = 10.0
cloud = filter.do_passthrough(cloud, filter_axis, axis_min, axis_max)

