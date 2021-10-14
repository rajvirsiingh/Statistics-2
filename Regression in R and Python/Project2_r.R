# Project 2: Regression in R.
# Description: R program to calculate regression
# Copyright: Rajvir Singh © 2021-25-09 
# Author: Rajvir Singh
# Version: 1.00	2021-25-09 Baseline computes regression
#          1.01 2021-05-10 Data read and write features added
# Reading data from a csv file
data <-(read.csv("C:/Users/RAJVIR SINGH/Desktop/project/coordinates.csv"))
# separating x & y extracted from csv file
A = data$x
B = data$y

#This function calculates the correlation among two vectors
regression <-function(Xcor,Ycor){
  i=1
  sumAB=sumA2=sumB2=0
  sumA =sum(Xcor)
  sumB= sum(Ycor)
  while(i<11)
  {
    sumA2=sumA2+ (Xcor[i]*Xcor[i])
    sumB2=sumB2+ (Ycor[i]*Ycor[i])
    sumAB=sumAB+ (Xcor[i]*Ycor[i])
    i=i+1
  }
  nEab= sumAB*10
  nEa2= sumA2*10
  EaEb= sumA*sumB
  nEb2 = sumB2*10
  Ea2 = sumA*sumA
  Eb2 = sumB*sumB
  
  B_ab=(nEab-sumA*sumB)/(nEb2-Eb2)
  B_ba=(nEab-sumA*sumB)/(nEa2-Ea2)
  cat("\n Regression X on Y:", B_ab)
  cat("\n Regression Y on X:", B_ba)
  cat("\n\n\n")
}

pc <-function(){
  pie(X) 
}

k=0
ext<-function(){
 invokeRestart("abort")
}
s=0
while(s==0)
{
  print("Choose an option:")
  print("1. Regression Coefficient ")
  print("2. Pie chart ")
  print("3. Bar Graph ")
  print("4. Quit ")
  print("Enter your choice:")
  a <- readline()
  m = strtoi(a, base=0L)
  result = switch(m,
                  "1"= regression(A,B),
                  "2"= pc(),
                  "3"= barplot(A,B, density=c(5,10,20,30,7) , angle=c(0,45,90,11,36) , col="brown"),
                  "4"= ext())
}





