text = "X-DSPAM-Confidence:    0.8475"
num = text.find('0.8475')
float(text[num:])
print(text[num:])
