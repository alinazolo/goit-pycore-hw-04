# Temperature Statistics Project

## Project Description: `temperatures_prj`

This Python project is designed to process temperature data for one month.

The data is stored in a text file called `temperatures.txt`, where each line represents one day. If the temperature for a certain day was not recorded, the corresponding line in the file remains empty.

The program reads data from the file, ignores empty lines, and calculates the main statistical values:

- minimum temperature;
- maximum temperature;
- average temperature;
- median temperature.

### Project Structure

```text
temperatures_prj/
│
├── data.py
├── processing.py
├── main.py
├── temperatures.txt
└── README.md
