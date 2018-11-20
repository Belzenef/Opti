rm(list = ls())

library(ggplot2)
library(doBy)

#**********************************************************************
data1<-read.table("fonctionf/paramsf.txt", h=T, dec=".")

# 1D
Equilibre<-as.factor((data1$Solution>(-2.9) & data1$Solution<(-2.7))+(data1$Solution >(3.4) & data1$Solution<(3.6))*2)
data1<-cbind(data1,Equilibre)
data1$Equilibre<-as.factor(data1$Equilibre)
data1$k1<-as.factor(data1$k1)
data1$k2<-as.factor(data1$k2)
data1$Depart<-as.factor(data1$Depart)
#data1$nbIter[data1$nbIter>=50000]<-25000
Overt<-as.factor(data1$nbIter>=10000)
data1<-cbind(data1,Overt)
summary(data1)

p <- ggplot(data1, aes(x = Depart, y =nbIter, color = Equilibre)) + 
  geom_jitter(size=2) + 
  ggtitle(" ") + theme_bw() +
  facet_wrap(~ k1+k2)+ 
  theme(axis.title=element_text(size=11,face="bold"))
p 
#ggsave("evolequif.png",p)
test<-data1[801:1000,]
summary(test)
summary(test[test$Depart==2,])
summaryBy(nbIter~k1+k2+Depart, data=data1, FUN=c(mean))

#**********************************************************************
data1<-read.table("fonctiong/paramsg4.txt", h=T, dec=".")

# 2D
Equilibre<-as.factor(
  ((data1$X >(-2.9) & data1$X<(-2.7)) & (data1$Y<(-2.7) & data1$Y>(-2.9)))*1+
  ((data1$X >(3.4) & data1$X<(3.6)) & (data1$Y<(-2.7) & data1$Y>(-2.9)))*2+
  ((data1$X<(-2.7) & data1$X>(-2.9)) & (data1$Y<(3.6) & data1$Y>(3.4)))*3+
  ((data1$X<(3.6) & data1$X>(3.4)) & (data1$Y<(3.6) & data1$Y>(3.4)))*4)
data1<-cbind(data1,Equilibre)
data1$Equilibre<-as.factor(data1$Equilibre)
data1$k1<-as.factor(data1$k1)
data1$k2<-as.factor(data1$k2)
data1$Depart<-as.factor(data1$Depart)
#data1$nbIter[data1$nbIter>=100000]<-10**(4.5)
Overt<-as.factor(data1$nbIter>=20000)
data1<-cbind(data1,Overt)
summary(data1)
p <- ggplot(data1, aes(x = Depart, y =nbIter, color = Equilibre)) + 
  geom_jitter(size=2) + 
  ggtitle(" ") + theme_bw() +
  facet_wrap(~ k1+k2)+ 
  theme(axis.title=element_text(size=11,face="bold"))
p
test<-data1[data1$k1==10 & data1$k2==0.1,]
summary(test)
summary(test[test$Depart==-4,c("k1","k2","Depart","nbIter","Equilibre","Overt")])
summary(test[test$Depart==4,c("k1","k2","Depart","nbIter","Equilibre","Overt")])
#ggsave("evolequig4.png",p)
#**********************************************************************
# Amélioration
data1<-read.table("paramsgV2.txt", h=T, dec=".")
data1<-data1[(data1$Depart!=0),]
# 2D
Equilibre<-as.factor(
  ((data1$X >(-2.9) & data1$X<(-2.7)) & (data1$Y<(-2.7) & data1$Y>(-2.9)))*1+
    ((data1$X >(3.4) & data1$X<(3.6)) & (data1$Y<(-2.7) & data1$Y>(-2.9)))*2+
    ((data1$X<(-2.7) & data1$X>(-2.9)) & (data1$Y<(3.6) & data1$Y>(3.4)))*3+
    ((data1$X<(3.6) & data1$X>(3.4)) & (data1$Y<(3.6) & data1$Y>(3.4)))*4)
data1<-cbind(data1,Equilibre)
data1$Equilibre<-as.factor(data1$Equilibre)
data1$version<-as.factor(data1$version)
data1$k1<-as.factor(data1$k1)
data1$k2<-as.factor(data1$k2)
data1$Depart<-as.factor(data1$Depart)
data1$nbIter[data1$nbIter>=100000]<-20000
summary(data1)
p <- ggplot(data1, aes(x = Depart, y =nbIter, color = Equilibre)) + 
  geom_jitter(size=2) + 
  ggtitle(" ") + theme_bw() +
  facet_wrap(~ k1+k2+version)+ 
  theme(axis.title=element_text(size=11,face="bold"))
p
test<-data1[data1$k1==10 & data1$k2==0.1 & data1$Depart==2
            & data1$version==1,
            c("version","k1","k2","Depart","nbIter","Equilibre")]
summary(test)
#ggsave("evolequig4.png",p)

#**********************************************************************
# Voyageur
data1<-read.table("Voyageur.txt", h=T, dec=".", sep="\t")
data1$k<-as.factor(data1$k)
summary(data1)
p <- ggplot(data1, aes(x = Fonction, y =log10(Dist), color = Fonction)) + 
  geom_jitter(size=2) + 
  ggtitle(" ") + theme_bw() +
  scale_color_discrete(labels=c("1/t^3","1/t","1/log(t)"))+
  facet_wrap(~k)+
  theme(axis.title=element_text(size=11,face="bold"))
p
#ggsave("evolequigV2.png",p)
p <- ggplot(data1, aes(x = Fonction, y =tpsExe, color = Fonction)) + 
  geom_jitter(size=2) + 
  ggtitle(" ") + theme_bw() +
  scale_color_discrete(labels=c("1/t^3","1/t","1/log(t)"))+
  facet_wrap(~k)+
  theme(axis.title=element_text(size=11,face="bold"))
p
test<-data1[data1$k==0 & data1$Fonction=="f3",]
str(test[test$Dist<=1421.7,])
mean(test$Iter)
min(test$Dist)
mean(test$Dist)
mean(test$tpsExe)


