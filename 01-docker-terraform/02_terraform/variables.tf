variable "credentials" {
  description = "My Credentials"
  default     = "./keys/creds_key.json"
}

variable "project" {
  description = "Project ID"
  default     = "skilled-nation-422203-s6"
}

variable "region" {
  description = "Project Region"
  default     = "us-central1"
}

variable "location" {
  description = "Project Location"
  default     = "US"
}

variable "bq_datase_name" {
  description = "My BQ Dataset Name"
  default     = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "Bucket Storage Bucket Name"
  default     = "skilled-nation-422203-s6-terra-demo-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}
