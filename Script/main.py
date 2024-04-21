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

