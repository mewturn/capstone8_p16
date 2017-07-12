mydata <- read_csv("C:/Users/user/Desktop/SUTD/Capstone/data.csv")

plot(mydata$Wavelength, mydata$Absorbance, type="n", xlab="Wavelength", ylab="Absorbance")
lines(mydata$Wavelength, mydata$Absorbance)
