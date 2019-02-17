# Expiration_Date
Our team designs software for the Department of Homeland Security’s Next Generation First Responder program.  When paramedics respond to a medical emergency, they ask the patient about any recent medications she has taken.  Since a patient’s medication influences which procedures or therapies will be administered, correctly recording and communicating the patient’s recent medication is crucial.  Our team is developing optical character recognition (OCR) software that can correctly read vital information from a photo of a medicine bottle, such as the medication’s name, the dose, the lot number and the expiration date.  

Our experiments show that lot numbers and expiration dates are particularly difficult for off-the-shelf OCR engines, such as Tesseract, to read because they are usually written in a dot-matrix font that varies widely from product to product. Additional difficulties include the curved shape of the vial and glare. Our team will custom train Tesseract’s neural network to recognize lot numbers and expiration dates in dot matrix font. Since no publicly available dataset exists, we are generating our own large dataset of dot-matrix fonts. 

We created an initial dot matrix font dataset with classes are 0-9, A-Z, Colon, Dash, Period, Slash.
The images were created by either deleting or perturbing a dot in a character. The number of images in each class, so far, are

0: 520

1: 200

2: 465

3: 610

4: 277

5: 542

6: 454

7: 222

8: 332

9: 299

A: 531

B: 398

C: 266

D: 553

E: 376

F: 299

G: 531

H: 332

I: 222

J: 244

K: 277

L: 222

M: 332

N: 332

O: 310

P: 299

Q: 343

R: 354

S: 310

T: 222

U: 288

V: 244

W: 332

X: 244

Y: 189

Z: 310

Colon: 112

Dash: 90

Period: 57

Slash: 168

