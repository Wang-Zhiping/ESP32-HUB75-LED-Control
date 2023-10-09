# Driving LEDs with a ESP32 S3 and HUB 75 LED panel
For background why I bought this setup, see [this reddit discussion](https://www.reddit.com/r/FastLED/comments/16rx3mz/high_refresh_rate_of_led_matrix/)

* Parts: [Adafruit Matrix Portal S3](https://learn.adafruit.com/adafruit-matrixportal-s3) with a HUB75 panel
* Any HUB75 panel (and probably also others) most likely work

## Dependency
Install [this](https://learn.adafruit.com/adafruit-matrixportal-s3/overview) to get it work with your Arduino IDE.

## Library
Install this library in your Arduino IDE.
* https://github.com/mrfaptastic/ESP32-HUB75-MatrixPanel-DMA


The examples from this library don't work out of the box since the pins are differently wired on the Adafruit Matrix Portal S3.
You need to change the content of the file `~/Arduino/libraries/ESP32_HUB75_LED_MATRIX_PANEL_DMA_Display/src/platforms/esp32s3/esp32s3-default-pins.hpp` to

```hpp
 #pragma once
 
 // Avoid and QSPI pins
 
 #define R1_PIN_DEFAULT 42
 #define G1_PIN_DEFAULT 41
 #define B1_PIN_DEFAULT 40
 #define R2_PIN_DEFAULT 38
 #define G2_PIN_DEFAULT 39
 #define B2_PIN_DEFAULT 37
 #define A_PIN_DEFAULT  45
 #define B_PIN_DEFAULT  36
 #define C_PIN_DEFAULT  48
 #define D_PIN_DEFAULT  35
 #define E_PIN_DEFAULT  21 // required for 1/32 scan panels, like 64x64. Any available pin would do, i.e. IO32
 #define LAT_PIN_DEFAULT 47
 #define OE_PIN_DEFAULT  14
 #define CLK_PIN_DEFAULT 2    
```

                             
