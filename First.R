library(jpeg)
data=readJPEG("C:\\ISI\\BStat1\\Stat\\Project\\maxresdefault3.jpg")
bg=readJPEG("C:\\ISI\\BStat1\\Stat\\Project\\bg2.jpg")

data1=data
data1[,,1]=ifelse(data[,,2]>0.5&data[,,1]<0.5&data[,,3]<0.7,bg[,,1],data[,,1])
data1[,,2]=ifelse(data[,,2]>0.5&data[,,1]<0.5&data[,,3]<0.7,bg[,,2],data[,,2])
data1[,,3]=ifelse(data[,,2]>0.5&data[,,1]<0.5&data[,,3]<0.7,bg[,,3],data[,,3])

plot(as.raster(data1))