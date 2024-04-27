import arcpy
import os
arcpy.env.workspace = r'G:\Semster 8\GIS\Project\Data'
arcpy.env.overwriteOutput = True

# Task 1
land = r'G:\Semster 8\GIS\Project\Data\ne_10m_land.shp'
geography_points = r'G:\Semster 8\GIS\Project\Data\ne_10m_geography_regions_points.shp'
geography_polys = r'G:\Semster 8\GIS\Project\Data\ne_10m_geography_regions_polys.shp'
elevation_points = r'G:\Semster 8\GIS\Project\Data\ne_10m_geography_regions_elevation_points.shp'
glaciated_areas = r'G:\Semster 8\GIS\Project\Data\ne_10m_glaciated_areas.shp'
rivers_lake_centerlines = r'ne_10m_rivers_lake_centerlines.shp'
output = r'G:\Semster 8\GIS\Project\Output'

feature_list = arcpy.ListFeatureClasses()
print(feature_list)


# Task 2
# Make feature layers
arcpy.MakeFeatureLayer_management(land, "land_lyr")
arcpy.MakeFeatureLayer_management(geography_points, "geo_points_lyr")
arcpy.MakeFeatureLayer_management(elevation_points, "elevation_points_lyr")

# Select elevation points on land
arcpy.SelectLayerByLocation_management("elevation_points_lyr", "INTERSECT", "land_lyr")

# Create shapefile for elevation points on land
arcpy.FeatureClassToFeatureClass_conversion("elevation_points_lyr", output, "elevation_points_on_land.shp")

# Count number of elevation points on land
elevation_points_count = arcpy.GetCount_management("elevation_points_lyr")
print("Number of elevation points on land:", elevation_points_count)

# Select geography region points on land
arcpy.SelectLayerByLocation_management("geo_points_lyr", "INTERSECT", "land_lyr")

# Create shapefile for geography region points on land
arcpy.FeatureClassToFeatureClass_conversion("geo_points_lyr", output, "geo_points_on_land.shp")

# Count number of geography region points on land
geo_points_count = arcpy.GetCount_management("geo_points_lyr")
print("Number of geography region points on land:", geo_points_count)

# Task 3


# Task 15
#
#     img_contents = os.listdir(imgfolder)
#     for img in img_contents:
#         full_path = os.path.join(imgfolder, img)
#         pillow_img = Image.open(full_path)
#         exif = {ExifTags.TAGS[k]: v for k, v in pillow_img._getexif().items() if k in ExifTags.TAGS}
#         gps_all = {}
#         try:
#             for key in exif['GPSInfo'].keys():
#                 decoded_value = ExifTags.GPSTAGS.get(key)
#                 gps_all[decoded_value] = exif['GPSInfo'][key]
#
#             long_ref = gps_all.get('GPSLongitudeRef')
#             long = gps_all.get('GPSLongitude')
#             lat_ref = gps_all.get('GPSLatitudeRef')
#             lat = gps_all.get('GPSLatitude')
#
#             print long_ref, "    ", long
#             print lat_ref, "    ", lat
#         except:
#             print("This image has no GPS Info in it {}".format(full_path))
#         finally:
#             print ("-----------"*50)