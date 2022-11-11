# IoT-Based-Neonatal-Incubator-Health-Monitoring-System



Premature babies, also known as preemies, are those that are born before the mother has reached 37 weeks of gestation.According to the World Health Organization (WHO), 1 million out of 15 million preemies die as a result of their prematurity, making preterm birth the second-highest cause of mortality for children who do not live to complete their fifth year and the top cause of death in the first month following birth.In order to create a similar environment to that of the womb, newborns must be housed in an incubator. The relative humidity and temperature should be strictly  maintained at predetermined levels based on the number of  incubation days.
  - However for various causes, if the temperature of a neonatal  incubator rises rapidly and the doctor is not aware of the condition in the incubator, the premature baby will face numerous difficulties.
  - In the absence of a continuous monitoring system, information about the  baby's health is unavailable, which causes difficulties for the medical staff and causes delay in assessment of the situation and consequently, treatment.

Our idea is a smart infant incubator monitoring system that includes numerous elements being tracked and real-time data with the aid of various sensors integrated to the microcontroller.The baby as well as the incubator environment is being constantly monitored.Medical personnel receive information about the patients' conditions via  Thingspeak cloud, web server , Pushover app and excel sheets, which they may use to process and analyse the baby's current state. Parents will also be benefitted by being able to monitor their baby remotely.


Three key characteristics of our system are : 

* Data storage and processing :  As is discussed  previously, a series of sensor signals are  gathered via the arduino uno, including the SpO2 , heartbeat,ambient temperature, humidity  and body temperature. Significant features can be retrieved to detect and identify potential heart disease in the infant and combat various diseases and emergencies that may occur due to any of the parameters fluctuating more drastically than the safe-limit.
 The identification and accurate diagnoses of a potential disease and danger often require a certain amount of historical data; therefore, a cloud database is established in the form of  Thingspeak Cloud to store the sensor data from the sensor node for each individual user in a graphical manner.
An excel sheet also stores the data during the required time frame.
 
* Data visualisation :
A web-server based data visualisation scheme using python is implemented,more specifically a web-based GUI is created for authorised users to access the data, which is real time.Fig. shows an example of the interface that displays real-time heartbeat,SpO2 ,ambient temperature, humidity and body temperature data. The same data is uploaded to the Thingspeak Cloud and also shown in real time on the webpage , which is backed by the python based tkinter package.
 
* Disease identification and notification - Our solution seeks to provide a user-friendly interface for data access. The hospital mainserver, doctors or nurses, and family members or associated caretakers are the three user groups targeted by the system.
    1. Any minor fluctuation in the heart rate, body temperature etc  is often life threatening for an infant. The system aims at protecting infants from such conditions, and it is important that the patients’ health conditions can be monitored and understood. 
    2. Any suspicious and abnormal sensor reading can be identified and notifications can be sent to identified users, such as the family members and doctors using the pushover application .  Parents can use this information to self-monitor their baby’s  health, and clinicians can use it to diagnose probable ailments. If an aberrant state is discovered, an alert will be sent to a specific stakeholder, such as doctors or family members via the app. 
    3. A full fledged LED alert system is integrated for easy understanding of the scenario and accordingly suitable next steps can be taken.
---------

Below is the brief description of our system :

* SENSORS:

   1. DHT11 for the suitable environment monitoring for the neonate: Increase in the temperature of the incubator as well as oxygen consumption of preterm infants takes place because of relatively low humidity.We need to maintain constant temperature in a relatively small area without harming the baby in the incubator.
      - Less humidity causes problems like hypothermia, dehydration in the infants.
      - If the humidity is low it tends to raise the insensible water losses, which in turn increases heat evaporation and moisture loss. 
      - Relatively higher levels of humidity is also not suitable for infants as it will increase the possibility for germs and bacteria.

    2. LM35 for body temperature: Fever is a typical indicator of infections, the common cold, and pneumonia, and temperature monitoring of the infant's body will aid in the detection of many other internal disorders.
      - When an infant's body temperature is not controlled, hypothermia is a serious risk. Preterm delivery problems, coagulation abnormalities, infection, and other issues have all been linked to neonatal hypothermia.
      - As a result, we took sure to keep an eye on the neonate's temperature in a non-invasive manner


     3.  MAX30100 HeartRate and SpO2  sensor: The heart is one of the most important indicators that may be used to assess a patient's overall health. 
      - The number of heartbeats per minute is represented in our system.Electrocardiographs are routinely used to monitor electrical heart signals (ECG). 
      - Meanwhile, ECG necessitates the continual application of numerous electrodes with a particular gel, causing discomfort, suffering, and skin damage in the fragile preterm child. It's also difficult to manage.
      - In order to overcome this, we used infrared technology to extract the heartbeats
      - Hypoxemia and apnea can be detected early using Respiration and Blood Oxygenation data.
      - Heart Rate helps to detect any kind of cardiovascular disorder in the infant. It also helps to detect arrhythmia(heart can beat too fast, too slowly, or with an irregular rhythm) or irregular heartbeats and ensures the normal working condition of the cardiac system.
      - The arterial SpO2 plays a major role in infant baby’s health.There is a difficult balance between too much and too little supplemental oxygen exposure in premature neonatal care. Because both too much and too little supplemental oxygen can harm preemies, their SpO2 levels must be maintained and regulated between 90 and 93 percent to avoid illnesses.

* MICROCONTROLLER: The microcontroller ARDUINO UNO receives and collects data from each of the sensors.

* COMMUNICATION MODULE: signal transmission is implemented  by using WIFI  module(ESP8826 -01) and the data is pushed to the cloud storage.

* CLOUD: Thingspeak stores data and generates plots that may be seen on a computer or through a mobile application for enhanced data visualisation.

* WEB SERVER USING PYTHON BASED GUI: The webpage will contain information of temperature, number of pulses, and all other parameters which are being taken instantaneously in the real time by the sensors. 

* MOBILE APPLICATION: The pushover app is used to get timely alerts so that any fatalities can be avoided and the treatment is done on a priority.

* LED SYSTEM :  The data is analysed by the LED system, which involves determining the best safe range of the parameters for determining medical emergencies and predicting possible infections/diseases that may pose a hazard to the infant and thereby alarming the staff in such case, with suitable LED indication, whereas the excel sheet records can be referred while the prescription of medicines and for analysis and assessment by the doctor.

----
* arduino.ino : arduino file
* swee1.py : python file for the webserver

