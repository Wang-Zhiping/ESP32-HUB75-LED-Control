
// Example sketch which shows how to display some patterns
// on a 64x32 LED matrix
//

#include <ESP32-HUB75-MatrixPanel-I2S-DMA.h>


#define PANEL_RES_X 32  // Number of pixels wide of each INDIVIDUAL panel module.
#define PANEL_RES_Y 32  // Number of pixels tall of each INDIVIDUAL panel module.
#define PANEL_CHAIN 1   // Total number of panels chained one to another

//MatrixPanel_I2S_DMA dma_display;
MatrixPanel_I2S_DMA *dma_display = nullptr;

uint16_t myBLACK = dma_display->color565(0, 0, 0);
uint16_t myWHITE = dma_display->color565(255, 255, 255);
uint16_t myRED = dma_display->color565(255, 0, 0);
uint16_t myGREEN = dma_display->color565(0, 255, 0);
uint16_t myBLUE = dma_display->color565(0, 0, 255);



void setup() {

  // Module configuration
  HUB75_I2S_CFG mxconfig(
    PANEL_RES_X,  // module width
    PANEL_RES_Y,  // module height
    PANEL_CHAIN   // Chain length
  );

  //mxconfig.gpio.e = 18;
  //mxconfig.clkphase = false;
  //mxconfig.driver = HUB75_I2S_CFG::FM6126A;

  // Display Setup
  dma_display = new MatrixPanel_I2S_DMA(mxconfig);
  dma_display->begin();
  dma_display->setBrightness8(255);  //0-255
  dma_display->clearScreen();

  Serial.begin(9600);
  long int t1 = millis();

  for (int i = 0; i < 20; ++i) {
    dma_display->fillRect(16, 0, dma_display->width() / 2, dma_display->height(), myRED);
    //delay(dd);
    dma_display->clearScreen();

    dma_display->fillRect(0, 16, dma_display->width(), dma_display->height() / 2, myRED);
    //delay(dd);
    dma_display->clearScreen();

    dma_display->fillRect(0, 0, dma_display->width() / 2, dma_display->height(), myRED);
    //delay(dd);
    dma_display->clearScreen();

    dma_display->fillRect(0, 0, dma_display->width(), dma_display->height() / 2, myRED);
    //delay(dd);
    dma_display->clearScreen();
  }

  long int t2 = millis();
  Serial.print("Time taken by the task: ");
  Serial.print(t2 - t1);
  Serial.println(" milliseconds");
}

uint8_t wheelval = 0;


// this function is looped
// 
void loop() {
  Serial.begin(9600);
  int pattern = 0;
  bool keep_pausing = false;
  // in milliseconds
  int delay_t = 10;
  while (true){
      // wait for trigger
      //Serial.println(analogRead(3));

      // if the trigger triggers, then leave while loop and display it
      // but if the trigger is still on (from previous shot), also keep pausing
      while (analogRead(3) < 1000 || keep_pausing == true){
        Serial.print("In the while loop: ");
        Serial.println(analogRead(3));
        //
        if (analogRead(3) < 1000){
            keep_pausing = false;
        }
      }
      //choose the right pattern
      keep_pausing = true;
      if (pattern == 0){
        dma_display->fillRect(16, 0, dma_display->width() / 2, dma_display->height(), myRED);
        pattern = 1;
      } else if (pattern == 1){
        dma_display->fillRect(0, 16, dma_display->width(), dma_display->height() / 2, myRED);
        pattern = 2;
      } else if (pattern == 2){
        dma_display->fillRect(0, 0, dma_display->width() / 2, dma_display->height(), myRED);
        pattern = 3;
      } else if (pattern == 3){
        dma_display->fillRect(0, 0, dma_display->width(), dma_display->height() / 2, myRED);
        pattern = 0;
      }
      // display it for a while
      delay(delay_t);
      // turn if off
      dma_display->clearScreen();
  }
}
