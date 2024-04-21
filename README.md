# GIS Data Processing in ArcMap

This repository contains scripts and data for processing GIS data in ArcMap.

## Datasets Used

- Land
- Geography Region Points
- Geography Regions Polys
- Geography Region Elevation Points
- Glaciated Areas
- Rivers Lake Centerlines

## Setup

1. Clone the repository.
2. Open ArcMap.
3. Load the datasets into ArcMap.

## Tasks

1. **List and Display Datasets**: Display all datasets in ArcMap.
   
2. **Create Shapefiles**:
   - Create shapefiles for Geography Region Elevation Points and Geography Region Points on Land.
   - Print the number of points in each shapefile.

3. **Update Mountain Data**:
   - Search for mountains with no names in the elevation points.
   - Print their latitude and longitude.
   - Update them with values from the comment field.

4. **Create Shapefiles for Glaciated Areas**:
   - Create shapefiles for each region in Geography Region Elevation Points that are in glaciated areas.

5. **Create Shapefiles for Ocean Regions**:
   - Create shapefiles for geographic region points in the Indian Ocean, North Pacific Ocean, and South Pacific Ocean.
   - Print the names of these regions.

6. **Create Shapefiles for Rivers and Lake Centerlines**:
   - Create shapefiles for Rivers Lake Centerlines based on scalerank.

7. **Print Region Data**:
   - Using Search Cursor, print the name, region, and WIKIDATAID for all geography regions polys.

8. **Create Shapefile for Lake Centerlines**:
   - Create a shapefile for all Lake Centerline in Rivers Lake Centerlines using only ONE condition.

9. **Create Shapefiles for African Regions**:
   - Using Search Cursor, create shapefiles for Geography Region Elevation Points where elevation > 1500 and region is “Africa”.

10. **Update Empty Fields**:
    - Using Update Cursor for multiple fields, update empty string fields in Geography Region Points.

11. **Create Toolbox**:
    - Implement all the requirements above in a toolbox. Ensure logs are printed in ArcGIS.

12. **Print Image Paths**:
    - Print the full path for a collection of images.

13. **Print Exif Tags**:
    - Print Exif Tags for the images.

14. **Print GPS Tags/Info**:
    - Print GPS Tags/Info for each image indicating which is geotagged & which is not.

15. **Print Geotagged Image Coordinates**:
    - Print latitude & longitude for each geotagged image.

## Usage

1. Run the provided scripts in ArcMap to perform the tasks described above.
2. View the output shapefiles and logs in ArcMap.


Feel free to adjust any details to better fit your project's specifics!
