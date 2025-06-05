#include <ESP32-HUB75-MatrixPanel-I2S-DMA.h>
#include <Adafruit_GFX.h>

#define PANEL_RES_X 32
#define PANEL_RES_Y 32
#define PANEL_CHAIN 1

#define R1_PIN 42
#define G1_PIN 41
#define B1_PIN 40
#define R2_PIN 38
#define G2_PIN 39
#define B2_PIN 37
#define A_PIN 45
#define B_PIN 36
#define C_PIN 48
#define D_PIN 35
#define E_PIN 21
#define LAT_PIN 47
#define OE_PIN 14
#define CLK_PIN 2

MatrixPanel_I2S_DMA* display = nullptr;

void setup() {
  Serial.begin(115200);

  HUB75_I2S_CFG::i2s_pins pins = {
    R1_PIN, G1_PIN, B1_PIN,
    R2_PIN, G2_PIN, B2_PIN,
    A_PIN, B_PIN, C_PIN, D_PIN, E_PIN,
    LAT_PIN, OE_PIN, CLK_PIN
  };
  HUB75_I2S_CFG cfg(PANEL_RES_X, PANEL_RES_Y, PANEL_CHAIN, pins);
  display = new MatrixPanel_I2S_DMA(cfg);
  display->begin();
  display->setBrightness8(128); 
  display->clearScreen();
}

void loop() {
  if (Serial.available()) {
    String cmd = Serial.readStringUntil('\n');
    cmd.trim();

    if (cmd.startsWith("PIXEL")) {
      int x, y, r, g, b;
      int matched = sscanf(cmd.c_str(), "PIXEL %d %d %d %d %d", &x, &y, &r, &g, &b);
      if (matched == 5 && x >= 0 && x < PANEL_RES_X && y >= 0 && y < PANEL_RES_Y) {
        uint16_t color = display->color565(r, g, b);
        display->drawPixel(x, y, color);
      }
    }
    else if (cmd.startsWith("CLEAR")) {
      display->clearScreen();
    }
    else if (cmd.startsWith("BRIGHTNESS")) {
      int val;
      if (sscanf(cmd.c_str(), "BRIGHTNESS %d", &val) == 1) {
        val = constrain(val, 0, 255);
        display->setBrightness8(val);
      }
    }
  }
}
