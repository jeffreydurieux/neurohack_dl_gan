# Thu Aug  8 16:51:48 2019
# Author: Jeffrey Durieux / j.durieux@fsw.leidenuniv.nl


library(oro.nifti)
library(gtools)
library(png)


# change path to subject folder
setwd("~/Desktop/test/")

# sort pngs
files <- dir()
files <- mixedsort(files)


# loop over pngs and store it in an array
data <- array(data = 0, dim = c(176,256,170))
dim(data)
for(i in 1:176){
  data[i,,] <- readPNG(files[i])
}

dim(data)

# path to write nifti file to
# 
setwd("~/Desktop/")
data <- as.nifti(data)
ext <- paste('Subject_', 123000, sep="")
writeNIfTI(nim = data, filename = ext)

