library(tidyverse)
library(janitor)
library(skimr)
library(ggplot2)

hotel_bookings <- read.csv("C:\\Nacho\\Data_Analytics\\hotel_bookings_C7W3.csv")

ggplot(data = hotel_bookings) +
  geom_point(mapping = aes(x=lead_time, y=children))

ggplot(data = hotel_bookings) +
  geom_point(mapping = aes(x=stays_in_weekend_nights, y=children))