# Green_Growth_mapper
•	Project Overview
The project is designed to identify areas suitable for afforestation by analyzing satellite images. It involves several key steps: location search, image retrieval, image processing, and afforestation area calculation. The goal is to determine the potential for planting trees in specific areas.

Step 1: Location Search
Objective: To identify the geographical coordinates (latitude and longitude) of a location based on user input.

Details:

User Input: The user enters a location name.
Geocoding Service: The project uses an API (like OpenWeatherMap Geocoding API) to convert the location name into geographical coordinates.
Process: The script sends a request to the geocoding service, receives the coordinates, and extracts the latitude and longitude. This step is crucial as it provides the necessary information to fetch satellite imagery for the given location.
Step 2: Image Retrieval
Objective: To fetch a satellite image of the specified location using the obtained coordinates.

Details:

Coordinates: The latitude and longitude from the previous step are used.
Satellite Imagery Service: The project uses a service like Bing Maps Imagery API to retrieve satellite images.
Process: The script constructs a URL using the coordinates and sends a request to the satellite imagery service. The response is a high-resolution image of the specified location, which is then saved locally for further processing.
Step 3: Image Processing
Objective: To analyze the satellite image and identify different land types such as trees, houses, roads, and fields.

Details:

Image Loading: The saved satellite image is loaded into the program.
Image Filtering: Techniques like mean shift filtering are applied to enhance the image and reduce noise.
Color Space Conversion: The image is converted from BGR (Blue, Green, Red) to HSV (Hue, Saturation, Value) color space to facilitate easier segmentation of different land types.
Thresholding and Masking: Thresholding techniques are used to create binary masks for different land types based on their color ranges in the HSV space. This helps in segmenting areas covered by trees, houses, roads, and fields.
Step 4: Afforestation Area Calculation
Objective: To calculate the area available for afforestation and estimate the number of trees that can be planted.

Details:

Mask Application: The masks created in the previous step are applied to the image to isolate areas of interest.
Pixel Count: The number of non-zero pixels (representing areas suitable for afforestation) is counted.
Area Calculation: The total area is calculated based on the pixel count and the resolution of the satellite image. The project assumes a certain pixel-to-area conversion factor.
Tree Estimation: Using standard spacing guidelines for tree planting, the project estimates the number of trees that can be planted in the available area.
Example Scenario
User Input: The user searches for "Central Park, New York."
Location Search: The project retrieves the coordinates (latitude and longitude) of Central Park.
Image Retrieval: Using these coordinates, the project fetches a high-resolution satellite image of Central Park.
Image Processing: The image is processed to identify areas covered by trees, open fields, and other land types.
Afforestation Calculation: The project calculates the total area of open fields suitable for planting trees and estimates the number of trees that can be planted based on standard spacing guidelines.
Final Outcome
The project provides a detailed report including:

The total area available for afforestation in square meters and acres.
The estimated number of trees that can be planted.
Visual representations of the identified land types and the areas suitable for afforestation.



![Screenshot (45)](https://github.com/Rio567/GreenGrowth-mapper/assets/130983781/46bcee89-ec9c-4d66-be65-53beb240be38)

![Screenshot (44)](https://github.com/Rio567/GreenGrowth-mapper/assets/130983781/e3ac3f51-4b87-4482-bacc-a12ed9934b09)

![pic3](https://github.com/Rio567/Green_Growth-mapper/assets/130983781/250ef394-eca6-4e01-b796-dfade059990c)

![pic2](https://github.com/Rio567/Green_Growth-mapper/assets/130983781/1fe5ef1c-5a93-4949-84d1-b5eb94b1aebd)

![pic1](https://github.com/Rio567/Green_Growth-mapper/assets/130983781/38f2b52f-cbf2-4c2b-b9c8-5555900a72e0)

