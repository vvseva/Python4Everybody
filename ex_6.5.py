print('Exercise 6.5')
text = "X-DSPAM-Confidence:    0.8475";
space = text.find('    ')
print(float(text[space:]))
