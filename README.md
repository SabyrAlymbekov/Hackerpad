# **Hackerpad (or Catpad)**

![3D render of hackpad](/assets//hackerpad.png)

## **About**

This is a custom mechanical macropad (Hackerpad), designed entirely from scratch (my first time btw).

## **Inspiration**

I wanted cool looking macropad for Competitive programming, so I made this one. The design is inspired by cyberpunk aesthetics and orpheuspad design. The device features 5 mechanical keys, a rotary encoder for multimedia control, an OLED display, and RGB lighting.

## **Features**

* **5 Mechanical Keys (Cherry MX):** Programmable macros for VS Code and terminal commands.  
* **Rotary Encoder (EC11):** Smooth volume control and scrolling.  
* **OLED Display (0.91"):** Displays active layers, WPM (words per minute), or Bongo Cat animations.  
* **Per-Key RGB:** Light (SK6812 MINI-E).  
* **Sandwich Case Design:** Designed in Fusion 360 for easy 3D printing and glueless assembly.  
* **Silkscreen art** Unique silkscreen art on the PCB.

## **BOM**

| Component | Quantity | Description | Notes |
| :---- | :---- | :---- | :---- |
| Microcontroller | 1 | Seeed Studio XIAO RP2040 | Brain of the device |
| Switches | 5 | Cherry MX | Mechanical switches |
| Keycaps | 5 | DSA profile (blank) | Keycaps |
| Diodes | 6 | 1N4148 (through hole) | For anti-ghosting |
| Encoder | 1 | EC11 rotary encoder | With push button |
| Display | 1 | 0.91" OLED I2C (128x32) | Pinout: GND-VCC-SCL-SDA |
| Pin Header | 1 | 1x4 pin header (2.54mm) | For connecting the display |
| LEDs | 2 | SK6812 MINI-E | Addressable RGB LEDs |
| Screws | 4 | M3 x 10mm | Case screws |
| Inserts | 4 | M3 heatset inserts | Threaded inserts |

## **PCB**

The PCB was designed in **KiCad**.

* **Size:** 97.7mm x 57.15mm.  
* **Layers:** 2 Layers (Top & Bottom).  

### **Layout Screenshots**

| Schematic | Routing | 3D View |
| :---- | :---- | :---- |
| ![Schematic](/assets/scheme.png) | ![PCB](/assets/pcb.png) | ![PCB render](/assets/pcb_rendered.png) |

## **Case Design**

The case was designed in **Autodesk Fusion 360**. It uses a "Sandwich" construction consisting of two parts:

1. **Bottom Case**  
2. **Top Case**

Printable files (.step) can be found in the /cad folder.

## **📂 Repository Structure**

├── cad/                 \# 3D printing files (STL, STEP, F3D)  
├── pcb/                 \# KiCad project (schematic, board, gerbers)  
├── firmware/            \# Source code (main.py)  
├── assets/              \# Renders and photos for README  
└── README.md            \# This file