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
On September 18, 2019, the three boroughs with the highest total fare amounts from green taxi pick-ups, each exceeding $50,000, **were Brooklyn, Manhattan, and Queens**. Here are the total fare amounts for each of these boroughs:
- Brooklyn: $96,333.24
- Manhattan: $92,271.30
- Queens: $78,671.71

This data indicates that Brooklyn, Manhattan, and Queens were the most lucrative areas for green taxi drivers on that particular day, highlighting significant taxi activity and passenger demand in these boroughs.

### Question 6 - Largest tip
```
select 
	gt."index" ,
	gt."PULocationID" ,
	puloc."Zone" as pu_zone,
	gt."DOLocationID" ,
	doloc."Zone" as do_zone,
	gt.tip_amount 
from ny_taxi.public.green_tripdata_2019 gt 
left join ny_taxi.public.taxi_zone_lookup puloc on puloc."LocationID" = gt."PULocationID" 
left join ny_taxi.public.taxi_zone_lookup doloc on doloc."LocationID" = gt."DOLocationID" 
where puloc."Zone" = 'Astoria'
order by 6 desc 
limit 1 
;
```
For passengers picked up in the zone named Astoria in September 2019, **the drop-off zone that received the largest tip was JFK Airport**. The largest tip amount recorded for such a trip was $62.31. This indicates that a trip from Astoria to JFK Airport resulted in the highest tip given during that period, suggesting a particularly generous gratuity for that specific route.

## Terraform Basic with Variables
### Question 7 - Creating Resources
Just finishied to create my resources using terraform. The resources are:
- Google Big Query Dataset
- Google Bucket

```
terraform apply
.
.
.
google_bigquery_dataset.demo_dataset: Creating...
google_storage_bucket.demo-bucket: Creating...
google_bigquery_dataset.demo_dataset: Creation complete after 1s [id=projects/skilled-nation-422203-s6/datasets/demo_dataset]
google_storage_bucket.demo-bucket: Creation complete after 1s [id=skilled-nation-422203-s6-terra-demo-bucket]
```
![image](https://github.com/Jomen034/data-engineering-zoomcamp2024/assets/71366136/0da025be-0ee7-4a87-9b5f-c9b29a6febd5)

```
terraform destroy
.
.
.
google_storage_bucket.demo-bucket: Destroying... [id=skilled-nation-422203-s6-terra-demo-bucket]
google_bigquery_dataset.demo_dataset: Destroying... [id=projects/skilled-nation-422203-s6/datasets/demo_dataset]
google_bigquery_dataset.demo_dataset: Destruction complete after 0s
google_storage_bucket.demo-bucket: Destruction complete after 2s
```
![Screenshot 2024-05-24 at 08 23 39](https://github.com/Jomen034/data-engineering-zoomcamp2024/assets/71366136/28f288df-8663-4c6e-8b9d-67b58517d98a)

#### Here is my key takes from the terraform basics
**Introduction to Terraform**

**Overview:** Terraform is an open-source infrastructure as code (IaC) tool that enables the management of infrastructure resources through code.

**Core Commands:**
init: Initializes a new or existing Terraform configuration.
plan: Generates an execution plan, showing what actions Terraform will take.
apply: Applies the changes required to reach the desired state of the configuration.
destroy: Destroys the infrastructure managed by the Terraform configuration.
T
**Terraform Basics**
- Configuration: Use HashiCorp Configuration Language (HCL) to define infrastructure resources in .tf files.
- State Management: Keeps track of resource states and allows for the consistent management of infrastructure.
- Modules: Encapsulate and reuse configurations.

**Terraform with Variables**
- Defining Variables: Use variable blocks to define inputs to your configurations.
- Assigning Values: Assign variable values through .tfvars files, environment variables, or CLI flags.
- Output Variables: Use output blocks to extract and display values after configuration is applied.

**Setting Up Environment on Google Cloud Platform (GCP)**
- GCP Integration: Use Terraform to manage GCP resources like Google BigQuery and Google Cloud Storage (buckets).
- Provider Configuration: Configure the GCP provider with appropriate credentials and project information.
- Resource Management:
  - Google BigQuery: Create datasets and tables.
  - Google Cloud Storage: Create and manage storage buckets.

**Key Takeaways**
- Automation: Terraform automates infrastructure provisioning and management.
- Scalability: Efficiently manage infrastructure at scale using reusable configurations and modules.
- Consistency: Ensure consistent environments by codifying infrastructure.
