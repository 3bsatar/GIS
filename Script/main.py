import arcpy

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
