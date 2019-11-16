#include "Arduino.h"
#include "ADXL345.h"
#include "I2Cdev.h"
#include "DCMDriverL298.h"
#include "DCMotor.h"
#include "Servo.h"

// Pin Definitions
#define DCMOTORDRIVERL298_PIN_INT1	2
#define DCMOTORDRIVERL298_PIN_ENB	6
#define DCMOTORDRIVERL298_PIN_INT2	4
#define DCMOTORDRIVERL298_PIN_ENA	5
#define DCMOTORDRIVERL298_PIN_INT3	7
#define DCMOTORDRIVERL298_PIN_INT4	8
#define DCMOTOR_1_PIN_COIL1	9
#define DCMOTOR_2_PIN_COIL1	11
#define GPS_PIN_TX	3
#define GPS_PIN_RX	10
#define SERVO3601_1_PIN_SIG	12
#define SERVO3602_2_PIN_SIG	13
#define SERVO3603_3_PIN_SIG	A3

// Global variables and defines
int16_t adxlAx, adxlAy, adxlAz;

// object initialization
ADXL345 adxl;
DCMDriverL298 dcMotorDriverL298(DCMOTORDRIVERL298_PIN_ENA,DCMOTORDRIVERL298_PIN_INT1,DCMOTORDRIVERL298_PIN_INT2,DCMOTORDRIVERL298_PIN_ENB,DCMOTORDRIVERL298_PIN_INT3,DCMOTORDRIVERL298_PIN_INT4);
DCMotor dcMotor_1(DCMOTOR_1_PIN_COIL1);
DCMotor dcMotor_2(DCMOTOR_2_PIN_COIL1);
Servo servo3601_1;
Servo servo3602_2;
Servo servo3603_3;

// define vars for testing menu
const int timeout = 10000;       //define timeout of 10 sec
char menuOption = 0;
long time0;

// Setup the essentials for your circuit to work. It runs first every time your circuit is powered with electricity.
void setup() 
{
    // Setup Serial which is useful for debugging
    // Use the Serial Monitor to view printed messages
    Serial.begin(9600);
    while (!Serial) ; // wait for serial port to connect. Needed for native USB
    Serial.println("start");
    
    adxl.init();
    menuOption = menu();
    
}

// Main logic of your circuit. It defines the interaction between the components you selected. After setup, it runs over and over again, in an eternal loop.
void loop() 
{
    if(menuOption == '1') {
    // SparkFun ADXL345 - Triple Axis Accelerometer Breakout - Test Code
    // read raw accel measurements from device
    adxl.getAcceleration(&adxlAx, &adxlAy, &adxlAz);
    // display tab-separated accel x/y/z values
    Serial.print(F("ADXL345 accel-\t")); 
    Serial.print(adxlAx); Serial.print(F("\t"));
    Serial.print(adxlAy); Serial.print(F("\t"));  
    Serial.println(adxlAz);
    }
    else if(menuOption == '2') {
    // L298N Motor Driver with Dual Hobby DC motors - Test Code
    //Start both motors. note that rotation direction is determined by the motors connection to the driver.
    //You can change the speed by setting a value between 0-255, and set the direction by changing between 1 and 0.
    dcMotorDriverL298.setMotorA(200,1);
    dcMotorDriverL298.setMotorB(200,0);
    delay(2000);
    //Stop both motors
    dcMotorDriverL298.stopMotors();
    delay(2000);

    }
    else if(menuOption == '3') {
    // Micro DC Motor (Geared) - 90 RPM (6-12V) #1 - Test Code
    // The DC motor will turn on and off for 4000ms (4 sec)
    dcMotor_1.on(200);                        // 1. turns on
    delay(4000);                             // 2. waits 4000 milliseconds (4 sec). change the value in the brackets (4000) for a longer or shorter delay.
    dcMotor_1.off();                       // 3. turns off
    delay(4000);                             // 4. waits 4000 milliseconds (4 sec). change the value in the brackets (4000) for a longer or shorter delay.

    }
    else if(menuOption == '4') {
    // Micro DC Motor (Geared) - 90 RPM (6-12V) #2 - Test Code
    // The DC motor will turn on and off for 4000ms (4 sec)
    dcMotor_2.on(200);                        // 1. turns on
    delay(4000);                             // 2. waits 4000 milliseconds (4 sec). change the value in the brackets (4000) for a longer or shorter delay.
    dcMotor_2.off();                       // 3. turns off
    delay(4000);                             // 4. waits 4000 milliseconds (4 sec). change the value in the brackets (4000) for a longer or shorter delay.

    }
    else if(menuOption == '5')
    {
    // Disclaimer: The Ublox NEO-6M GPS Module is in testing and/or doesn't have code, therefore it may be buggy. Please be kind and report any bugs you may find.
    }
    else if(menuOption == '6') {
    // Servo - Generic Continuous Rotation (Micro Size) #1 - Test Code
    // The servo will rotate CW in full speed, CCW in full speed, and will stop  with an interval of 2000 milliseconds (2 seconds) 
    servo3601_1.attach(SERVO3601_1_PIN_SIG);         // 1. attach the servo to correct pin to control it.
    servo3601_1.write(180);  // 2. turns servo CW in full speed. change the value in the brackets (180) to change the speed. As these numbers move closer to 90, the servo will move slower in that direction.
    delay(2000);                              // 3. waits 2000 milliseconds (2 sec). change the value in the brackets (2000) for a longer or shorter delay in milliseconds.
    servo3601_1.write(0);    // 4. turns servo CCW in full speed. change the value in the brackets (0) to change the speed. As these numbers move closer to 90, the servo will move slower in that direction.
    delay(2000);                              // 5. waits 2000 milliseconds (2 sec). change the value in the brackets (2000) for a longer or shorter delay in milliseconds.
    servo3601_1.write(90);    // 6. sending 90 stops the servo 
    delay(2000);                              // 7. waits 2000 milliseconds (2 sec). change the value in the brackets (2000) for a longer or shorter delay in milliseconds.
    servo3601_1.detach();                    // 8. release the servo to conserve power. When detached the servo will NOT hold it's position under stress.
    }
    else if(menuOption == '7') {
    // Servo - Generic Continuous Rotation (Micro Size) #2 - Test Code
    // The servo will rotate CW in full speed, CCW in full speed, and will stop  with an interval of 2000 milliseconds (2 seconds) 
    servo3602_2.attach(SERVO3602_2_PIN_SIG);         // 1. attach the servo to correct pin to control it.
    servo3602_2.write(180);  // 2. turns servo CW in full speed. change the value in the brackets (180) to change the speed. As these numbers move closer to 90, the servo will move slower in that direction.
    delay(2000);                              // 3. waits 2000 milliseconds (2 sec). change the value in the brackets (2000) for a longer or shorter delay in milliseconds.
    servo3602_2.write(0);    // 4. turns servo CCW in full speed. change the value in the brackets (0) to change the speed. As these numbers move closer to 90, the servo will move slower in that direction.
    delay(2000);                              // 5. waits 2000 milliseconds (2 sec). change the value in the brackets (2000) for a longer or shorter delay in milliseconds.
    servo3602_2.write(90);    // 6. sending 90 stops the servo 
    delay(2000);                              // 7. waits 2000 milliseconds (2 sec). change the value in the brackets (2000) for a longer or shorter delay in milliseconds.
    servo3602_2.detach();                    // 8. release the servo to conserve power. When detached the servo will NOT hold it's position under stress.
    }
    else if(menuOption == '8') {
    // Servo - Generic Continuous Rotation (Micro Size) #3 - Test Code
    // The servo will rotate CW in full speed, CCW in full speed, and will stop  with an interval of 2000 milliseconds (2 seconds) 
    servo3603_3.attach(SERVO3603_3_PIN_SIG);         // 1. attach the servo to correct pin to control it.
    servo3603_3.write(180);  // 2. turns servo CW in full speed. change the value in the brackets (180) to change the speed. As these numbers move closer to 90, the servo will move slower in that direction.
    delay(2000);                              // 3. waits 2000 milliseconds (2 sec). change the value in the brackets (2000) for a longer or shorter delay in milliseconds.
    servo3603_3.write(0);    // 4. turns servo CCW in full speed. change the value in the brackets (0) to change the speed. As these numbers move closer to 90, the servo will move slower in that direction.
    delay(2000);                              // 5. waits 2000 milliseconds (2 sec). change the value in the brackets (2000) for a longer or shorter delay in milliseconds.
    servo3603_3.write(90);    // 6. sending 90 stops the servo 
    delay(2000);                              // 7. waits 2000 milliseconds (2 sec). change the value in the brackets (2000) for a longer or shorter delay in milliseconds.
    servo3603_3.detach();                    // 8. release the servo to conserve power. When detached the servo will NOT hold it's position under stress.
    }
    
    if (millis() - time0 > timeout)
    {
        menuOption = menu();
    }
    
}

// Menu function for selecting the components to be tested
// Follow serial monitor for instrcutions
char menu()
{
    Serial.println(F("\nWhich component would you like to test?"));
    Serial.println(F("(1) SparkFun ADXL345 - Triple Axis Accelerometer Breakout"));
    Serial.println(F("(2) L298N Motor Driver with Dual Hobby DC motors"));
    Serial.println(F("(3) Micro DC Motor (Geared) - 90 RPM (6-12V) #1"));
    Serial.println(F("(4) Micro DC Motor (Geared) - 90 RPM (6-12V) #2"));
    Serial.println(F("(5) Ublox NEO-6M GPS Module"));
    Serial.println(F("(6) Servo - Generic Continuous Rotation (Micro Size) #1"));
    Serial.println(F("(7) Servo - Generic Continuous Rotation (Micro Size) #2"));
    Serial.println(F("(8) Servo - Generic Continuous Rotation (Micro Size) #3"));
    Serial.println(F("(menu) send anything else or press on board reset button\n"));
    while (!Serial.available());

    // Read data from serial monitor if received
    while (Serial.available()) 
    {
        char c = Serial.read();
        if (isAlphaNumeric(c)) 
        {   
            
            if(c == '1') 
    			Serial.println(F("Now Testing SparkFun ADXL345 - Triple Axis Accelerometer Breakout"));
    		else if(c == '2') 
    			Serial.println(F("Now Testing L298N Motor Driver with Dual Hobby DC motors"));
    		else if(c == '3') 
    			Serial.println(F("Now Testing Micro DC Motor (Geared) - 90 RPM (6-12V) #1"));
    		else if(c == '4') 
    			Serial.println(F("Now Testing Micro DC Motor (Geared) - 90 RPM (6-12V) #2"));
    		else if(c == '5') 
    			Serial.println(F("Now Testing Ublox NEO-6M GPS Module - note that this component doesn't have a test code"));
    		else if(c == '6') 
    			Serial.println(F("Now Testing Servo - Generic Continuous Rotation (Micro Size) #1"));
    		else if(c == '7') 
    			Serial.println(F("Now Testing Servo - Generic Continuous Rotation (Micro Size) #2"));
    		else if(c == '8') 
    			Serial.println(F("Now Testing Servo - Generic Continuous Rotation (Micro Size) #3"));
            else
            {
                Serial.println(F("illegal input!"));
                return 0;
            }
            time0 = millis();
            return c;
        }
    }
}