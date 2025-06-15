#libraries


library(readxl)
library(ggplot2)
library(qqplotr)
library(ggfortify)
library(car)
library(MASS)
library(olsrr)
library(car)
library(ggeffects)
library(caret)
library(sjmisc)
library(mixlm)
setwd("C:\\Users\\16094\\Downloads")
appledata = read_xlsx("Spotify_Dataset_Cleaned.xlsx",1)
spotifydata = read_xlsx("Spotify_Dataset_Cleaned.xlsx",2)
data
boxplot(in_spotify_playlists ~ mode, data = spotifydata, main = "Boxplot of in_spotify_playlists by Mode", xlab = "Mode", ylab = "in_spotify_playlists") 
boxplot(in_spotify_playlists ~ key, data = spotifydata, main = "Boxplot of in_spotify_playlists by Key", xlab = "Key", ylab = "in_spotify_playlists") 
boxplot(in_spotify_playlists ~ genre, data = spotifydata, main = "Boxplot of in_spotify_playlists by Genre", xlab = "Mode", ylab = "in_spotify_playlists")
boxplot(in_apple_playlists ~ mode, data = appledata , main = "Boxplot of in_apple_playlists by Mode", xlab = "Mode", ylab = "in_apple_playlists") 
boxplot(in_apple_playlists ~ key, data = appledata , main = "Boxplot of in_apple_playlists by Key", xlab = "Key", ylab = "in_apple_playlists") 
boxplot(in_apple_playlists ~ genre, data = appledata , main = "Boxplot of in_apple_playlists by Genre", xlab = "Genre", ylab = "in_apple_playlists")

#spotify backward model
spotifymodel=lm(in_spotify_playlists~genre + bpm + key + mode + danceability + valence + energy + acousticness + instrumentalness + liveness + speechiness, data=spotifydata)
summary(backward(spotifymodel, alpha = 0.05, full = TRUE, hierarchy = TRUE))
plot(spotifymodel)

#apple backward model
applemodel=lm(in_apple_playlists~genre + bpm + key + mode + danceability + valence + energy + acousticness + instrumentalness + liveness + speechiness, data=appledata)
summary(backward(applemodel, alpha = 0.05, full = TRUE, hierarchy = TRUE))
plot(applemodel)

#APPENDIX - additional work
#predicted vs r-student
rstud <- rstudent(spotifymodel)
predicted <- predict(spotifymodel)

plot(predicted, rstud,
     main = "Predicted vs. R-Student",
     xlab = "Predicted Values",
     ylab = "R-Student")


rstud <- rstudent(applemodel)
predicted <- predict(applemodel)

plot(predicted, rstud,
     main = "Predicted vs. R-Student",
     xlab = "Predicted Values",
     ylab = "R-Student")

rsq = summary(spotifymodel)$r.squared
rsq

aic = AIC(spotifymodel)
aic

RMSE.mdl1=summary(spotifymodel)$sigma
Dependent_Mean=mean(spotifydata$in_spotify_playlists)
X=model.matrix(spotifymodel) # Model Matrix

y = spotifydata$in_spotify_playlists
y_hat = spotifymodel$fitted.values 

plot(spotifydata$in_spotify_playlists, predict(spotifymodel), pch = 20, type = 'p', las = 1,
     xlab="Observed", ylab="Predicted", main = 'Observed vs Predicted')

#probability plots
hii = hatvalues(spotifymodel)                 ## LEVERAGE POINTS 
cd = cooks.distance(spotifymodel)          ## COOKS DISTANCE 
dfts = dffits(spotifymodel)                ## DFFITS
e = residuals(spotifymodel)             ## RESIDUAL
std_e = stdres(spotifymodel)            ## STANDARDIZED RESIDUAL
r = studres(spotifymodel)               ## STUDENTIZED RESIDUAL 
t = rstudent(spotifymodel)             ## COMPUTING R-Student

Residual = residuals(spotifymodel)             ## ei = RESIDUAL
Stand_Res = Residual/sigma(spotifymodel)        ## di = STANDARDIZED RESIDUAL
Student_Res = stdres(spotifymodel)               ## ri = STUDENTIZED RESIDUAL 
R_Student = rstudent(spotifymodel)             ## ti = R-Student
Lev_hii = hatvalues(spotifymodel)                 ## hii = LEVERAGE POINTS 
CookD = cooks.distance(spotifymodel)                ## Di = COOKS DISTANCE 
Dffit = dffits(spotifymodel)                      ## DFFITS

pr = e/(1-hii)                        ## PRESS RESIDUAL
pr

PRS_Stat = sum(pr^2)                 ## PRESS STATISTIC
PRS_Stat

SST = sum((spotifydata$in_spotify_playlists - mean(spotifydata$in_spotify_playlists))^2) ## TOTAL SUM OF SQUARES 
SST

RSq_Prediction = 1 - (PRS_Stat/SST)  ## R-Square - Prediction
RSq_Prediction

table.residuals=data.frame(row(spotifydata)[,1],spotifydata$in_spotify_playlists,y_hat,e,hii,std_e, pr , t, cd, dfts)
colnames(table.residuals)=c("Observations","Y","YHAT","Residual","Leverage","STUD_RES","PRESS","R_STUDENT","COOKD","DFFITS")
View(table.residuals)

rsq = summary(spotifymodel)$r.squared
rsq

aic = AIC(spotifymodel)
aic

RMSE.mdlB=summary(applemodel)$sigma
Dependent_MeanB=mean(appledata$in_apple_playlists)
XB=model.matrix(applemodel) # Model Matrix
"H=X%%(solve(t(X)%%X)%*%t(X))"# Hat Matrix
yB = appledata$in_apple_playlists
y_hatB = applemodel$fitted.values 

plot(appledata$in_apple_playlists, predict(applemodel), pch = 20, type = 'p', las = 1,
     xlab="Observed", ylab="Predicted", main = 'ObservedB vs PredictedB')

#probability plots
hiiB=hatvalues(applemodel)                 ## LEVERAGE POINTS 
cdB=cooks.distance(applemodel)          ## COOKS DISTANCE 
dftsB=dffits(applemodel)                ## DFFITS
eB=residuals(applemodel)             ## RESIDUAL
std_eB=stdres(applemodel)            ## STANDARDIZED RESIDUAL
rB= studres(applemodel)               ## STUDENTIZED RESIDUAL 
tB = rstudent(applemodel)             ## COMPUTING R-Student
plot(y_hatB, tB, pch = 20, type = 'p', las = 1,
     xlab="Predicted", ylab="R-Student",  main = 'PredictedB vs R-StudentB')
ResidualB=residuals(applemodel)             ## ei = RESIDUAL
Stand_ResB= ResidualB/sigma(applemodel)        ## di = STANDARDIZED RESIDUAL
Student_ResB=stdres(applemodel)               ## ri = STUDENTIZED RESIDUAL 
R_StudentB = rstudent(applemodel)             ## ti = R-Student
Lev_hiiB=hatvalues(applemodel)                 ## hii = LEVERAGE POINTS 
CookDB=cooks.distance(applemodel)                ## Di = COOKS DISTANCE 
DffitB=dffits(applemodel)                      ## DFFITS

plot(R_StudentB, ResidualB,
     main = "Residuals vs. R-Student",
     xlab= "R-Student",
     ylab = "Residuals")

prB=eB/(1-hiiB)                        ## PRESS RESIDUAL
prB

PRS_StatB=sum(prB^2)                 ## PRESS STATISTIC
PRS_StatB

SSTB = sum((appledata$in_apple_playlists - mean(appledata$in_apple_playlists))^2) ## TOTAL SUM OF SQUARES 
SSTB

RSq_PredictionB = 1 - (PRS_StatB/SSTB)  ## R-Square - Prediction
RSq_PredictionB

table.residualsB=data.frame(row(appledata)[,1],appledata$in_apple_playlists,y_hatB,eB,hiiB,std_eB, prB , tB, cdB, dftsB)
colnames(table.residualsB)=c("Observations","Y","YHAT","Residual","Leverage","STUD_RES","PRESS","R_STUDENT","COOKD","DFFITS")
View(table.residualsB)