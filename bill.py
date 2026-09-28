bill = float(input("How much was the bill? "))
tip=[1,1.15,1.2,1.25]
print("how was the service?")
service=input("Enter service quality (bad, okay, good, great): ")
if service == "bad":
    print(tip[0]*bill)
elif service == "okay":
    print(tip[1]*bill)
elif service == "good":
    print(tip[2]*bill)
elif service == "great":
    print(tip[3]*bill)

