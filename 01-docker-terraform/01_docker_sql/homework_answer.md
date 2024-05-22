# [Module 1 HW](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2024/01-docker-terraform/homework.md)
## Docker & SQL
### Question 1 - Docker tags
**Steps**
```
docker --help
docker build --help
docker run --help
```

From lists of command above, we get information about the tags option we can use.
The text `Automatically remove the container when it exits` stands for tag `--rm` from command `docker run --help

### Question 2 - Docker 1st run
**Steps**
```
docker run -it --entrypoint bash python:3.9
```
- `docker run` starts a new Docker container
- `-it` stands for interactive terminal
- `--entrypoint` bash sets the entrypoint of the container to bash
- `python:3.9` specifies the Docker image to use

```
pip list
```
The version of the package `wheel` is 0.43.0

### Question 3 - Count records
```
select count(distinct index) as ttl_trips
from ny_taxi.public.green_tripdata_2019
where date(lpep_pickup_datetime) = '2019-09-18'
	and date(lpep_dropoff_datetime) = '2019-09-18'
;
```
On September 18, 2019, there were a total of 15,612 distinct green taxi trips in New York City. This count represents all trips that both started and ended on that particular day. 
This volume of trips can be used to assess the usage patterns of green taxis, inform city transportation planning, and understand the impact of green taxis on New York City's broader transportation ecosystem on that specific day.

### Question 4 - Longest trip for each day
```
select *
from ny_taxi.public.green_tripdata_2019
order by trip_distance desc
limit 1
;
```
On September 26, 2019, the green taxi with the longest recorded trip distance for that year began its journey. This specific day stands out as the date with the single longest trip recorded among all the green taxi rides in 2019. 

### Question 5 - Three biggest pick up Boroughs
```
select 
	tzl."Borough" ,
	sum(total_amount) as total_amount 
from ny_taxi.public.green_tripdata_2019 gt 
left join ny_taxi.public.taxi_zone_lookup tzl on tzl."LocationID" = gt."PULocationID" 
where date(lpep_pickup_datetime) = '2019-09-18'
	and tzl."Borough" != 'Unknown'
group by 1
having sum(total_amount)>50000
order by 2 desc
;
```