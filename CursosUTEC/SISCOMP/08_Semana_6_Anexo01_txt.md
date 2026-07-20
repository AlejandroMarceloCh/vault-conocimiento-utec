---
curso: SISCOMP
titulo: 08 - Semana 6/Anexo01
slides: 0
fuente: 08 - Semana 6/Anexo01.txt
---


Anexo 1

High - level code

// C++ code
//
void setup()
{
  pinMode(2, OUTPUT); //A
  pinMode(3, OUTPUT); //B
  pinMode(4, OUTPUT); //C
  pinMode(5, OUTPUT); //D
  pinMode(6, OUTPUT); //F
  pinMode(7, OUTPUT); //G
  pinMode(8, OUTPUT); //H
}

void loop()
{
  digitalWrite(2, LOW);  //U
  digitalWrite(3, HIGH);
  digitalWrite(4, HIGH);
  digitalWrite(5, HIGH);
  digitalWrite(6, HIGH);
  digitalWrite(7, HIGH);
  digitalWrite(8, LOW);
  delay(1000); 
  
  digitalWrite(2, LOW);  //t
  digitalWrite(3, LOW);
  digitalWrite(4, LOW);
  digitalWrite(5, HIGH);
  digitalWrite(6, HIGH);
  digitalWrite(7, HIGH);
  digitalWrite(8, HIGH);
  delay(1000);
  
  digitalWrite(2, HIGH); //E
  digitalWrite(3, LOW);
  digitalWrite(4, LOW);
  digitalWrite(5, HIGH);
  digitalWrite(6, HIGH);
  digitalWrite(7, HIGH);
  digitalWrite(8, HIGH);
  delay(1000); 
  
  digitalWrite(2, HIGH);  //C
  digitalWrite(3, LOW);
  digitalWrite(4, LOW);
  digitalWrite(5, HIGH);
  digitalWrite(6, HIGH);
  digitalWrite(7, HIGH);
  digitalWrite(8, LOW);
  delay(1000); 
}
